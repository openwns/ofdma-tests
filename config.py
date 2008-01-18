import random
random.seed(42)
import wns.WNS
import wns.Node
import rise.Mobility
import winprost.support.Transceiver
import ofdmaphy.Station
import ofdmaphy.OFDMAPhy

from testScenarios import manhattan as scenario

class Config:
    bsPowerPerSubBand = "2.83 dBm"
    velocity = 10
    numMS = 50
    maxSimTime = 10.0
    rxpProbeName = "Scanner_RxPwr"
    sinrProbeName = "Scanner_SINR"

    xMax = scenario.getXMax()
    yMax = scenario.getYMax()
    bsPositions = [ pos for pos,grp in scenario.getPositions()['BS'] ]
    numBS = len(bsPositions)

WNS = wns.WNS.WNS()
WNS.maxSimTime = Config.maxSimTime
WNS.outputStrategy = wns.WNS.OutputStrategy.DELETE

riseConfig = WNS.modules.rise
riseConfig.debug.transmitter = True
riseConfig.debug.receiver = True
riseConfig.debug.main = True

ofdmaPhyConfig = WNS.modules.ofdmaPhy
ofdmaPhySystem = ofdmaphy.OFDMAPhy.OFDMASystem('OFDMA')
ofdmaPhySystem.Scenario = scenario

ofdmaPhyConfig.systems.append(ofdmaPhySystem)

mobilityObstructions = scenario.getMobilityObstructions()

myShadowing = scenario.getShadowing(scenario = ofdmaPhySystem.Scenario,
                                    wallAttenuation = 11.8,
                                    smoothingSteps = 10)

# inject shadowing model into propagation config
winprost.support.Transceiver.Propagation.ap2ap.shadowing = myShadowing
winprost.support.Transceiver.Propagation.ap2frs.shadowing = myShadowing
winprost.support.Transceiver.Propagation.ap2ut.shadowing = myShadowing
winprost.support.Transceiver.Propagation.frs2ut.shadowing = myShadowing
winprost.support.Transceiver.Propagation.ut2ut.shadowing = myShadowing

# Construct simple Sender Node
class BS(wns.Node.Node):
    mobility = None
    sender = None

    def __init__(self, name, mobility):
        super(BS, self).__init__(name)
        self.mobility = rise.Mobility.Component(self,
                                                "Mobility Component",
                                                mobility)
        self.mobility.mobility.logger.enabled=False
        self.sender = ofdmaphy.Station.Sender(self, name, [winprost.support.Transceiver.APTransmitter()])
        self.sender.txPower = Config.bsPowerPerSubBand


# Construct simple Receiver / Measurer Node
class MS(wns.Node.Node):
    mobility = None
    scanner = None

    def __init__(self, name, mobility):
        super(MS, self).__init__(name)
        self.mobility = rise.Mobility.Component(self,
                                                "Mobility Component",
                                                mobility)
        self.mobility.mobility.logger.enabled=False
        self.scanner = ofdmaphy.Station.Scanner(self, name, [winprost.support.Transceiver.UTReceiver()])
        self.scanner.rxpProbeName = Config.rxpProbeName
        self.scanner.sinrProbeName = Config.sinrProbeName


stationCounter = 0
for ii in xrange(Config.numBS):
    noMobility = rise.Mobility.No(Config.bsPositions[ii])
    WNS.nodes.append( BS("BS" + str(stationCounter), noMobility) )
    stationCounter += 1

utPositions = []
for ii in xrange(Config.numMS):
    aMobility = rise.Mobility.BrownianRect([0, 0, Config.xMax, Config.yMax], mobilityObstructions)
    aMobility.userVelocityDist = wns.Distribution.Fixed(Config.velocity)
    aMobility.moveTimeStep = 1.0
    utPositions.append(aMobility.coords)
    WNS.nodes.append( MS("MS" + str(stationCounter), aMobility) )
    stationCounter += 1

# register the probes
import Probes
Probes.buildProbes(Config, WNS)

# suppress output of (empty) winprost Probes
from speetcl.probes import ProbeModding
for (k,v) in WNS.modules.winprost.probes.items():
    ProbeModding.doIgnore(v)
