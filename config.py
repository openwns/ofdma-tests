###############################################################################
# This file is part of openWNS (open Wireless Network Simulator)
# _____________________________________________________________________________
#
# Copyright (C) 2004-2007
# Chair of Communication Networks (ComNets)
# Kopernikusstr. 16, D-52074 Aachen, Germany
# phone: ++49-241-80-27910,
# fax: ++49-241-80-22242
# email: info@openwns.org
# www: http://www.openwns.org
# _____________________________________________________________________________
#
# openWNS is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License version 2 as published by the
# Free Software Foundation;
#
# openWNS is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
import random
random.seed(42)
import openwns
import openwns.node
import openwns.distribution
import rise.Mobility
import ofdmaphy.Transmitter
import ofdmaphy.Receiver
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

    xMin = scenario.getXMin()
    yMin = scenario.getYMin()
    xMax = scenario.getXMax()
    yMax = scenario.getYMax()
    bsPositions = [ pos for pos,grp in scenario.getPositions()['BS'] ]
    numBS = len(bsPositions)

WNS = openwns.Simulator(simulationModel = openwns.node.NodeSimulationModel())
WNS.maxSimTime = Config.maxSimTime
WNS.outputStrategy = openwns.simulator.OutputStrategy.DELETE

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
id = rise.scenario.Propagation.DropInPropagation.getInstance().findId("DropIn")
rise.scenario.Propagation.DropInPropagation.getInstance().getPair(id, id).shadowing = myShadowing

# Construct simple Sender Node
class BS(openwns.node.Node):
    mobility = None
    sender = None

    def __init__(self, name, mobility):
        super(BS, self).__init__(name)
        self.mobility = rise.Mobility.Component(self,
                                                "Mobility Component",
                                                mobility)
        self.mobility.mobility.logger.enabled=False
        self.sender = ofdmaphy.Station.Sender(self, name, [ofdmaphy.Transmitter.TransmitterDropIn()])
        self.sender.txPower = Config.bsPowerPerSubBand


# Construct simple Receiver / Measurer Node
class MS(openwns.node.Node):
    mobility = None
    scanner = None

    def __init__(self, name, mobility):
        super(MS, self).__init__(name)
        self.mobility = rise.Mobility.Component(self,
                                                "Mobility Component",
                                                mobility)
        self.mobility.mobility.logger.enabled=False
        self.scanner = ofdmaphy.Station.Scanner(self, name, [ofdmaphy.Receiver.ReceiverDropIn()])
        self.scanner.rxpProbeName = Config.rxpProbeName
        self.scanner.sinrProbeName = Config.sinrProbeName


stationCounter = 0
for ii in xrange(Config.numBS):
    noMobility = rise.Mobility.No(Config.bsPositions[ii])
    WNS.simulationModel.nodes.append( BS("BS" + str(stationCounter), noMobility) )
    stationCounter += 1

utPositions = []
for ii in xrange(Config.numMS):
    aMobility = rise.Mobility.BrownianRect([Config.xMin, Config.yMin, Config.xMax, Config.yMax], mobilityObstructions)
    aMobility.userVelocityDist = openwns.distribution.Fixed(Config.velocity)
    aMobility.moveTimeStep = 1.0
    utPositions.append(aMobility.coords)
    WNS.simulationModel.nodes.append( MS("MS" + str(stationCounter), aMobility) )
    stationCounter += 1

# register the probes
import Probes
Probes.installDefaultProbes(WNS, Config)
openwns.setSimulator(WNS)
