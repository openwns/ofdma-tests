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

    # Need this to get the scenario size
    shad = scenario.getShadowing(0, 1)

    xMin = 0
    yMin = 0
    xMax = scenario.sizeX
    yMax = scenario.sizeY
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
ofdmaPhySystem = ofdmaphy.OFDMAPhy.OFDMASystem('ofdma')
ofdmaPhySystem.Scenario = scenario

ofdmaPhyConfig.systems.append(ofdmaPhySystem)

mobilityObstructions = scenario.getMobilityObstructions()

myShadowing = scenario.getShadowing(wallAttenuation = 11.8,
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
        self.sender = ofdmaphy.Station.Sender(self, name, [ofdmaphy.Transmitter.TransmitterDropIn()], 5000.0)
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
        self.scanner = ofdmaphy.Station.Scanner(self, name, [ofdmaphy.Receiver.ReceiverDropIn()], 5000.0)
        self.scanner.rxpProbeName = Config.rxpProbeName
        self.scanner.sinrProbeName = Config.sinrProbeName
        self.scanner.pathlossProbeName = "Pathloss"
        self.scanner.maxRxpProbeName = "MaxRxPower"
        self.scanner.maxSINRProbeName = "MaxSINR"
        self.scanner.minPathlossProbeName = "MinPathloss"
        self.scanner.distanceProbeName = "Distance"


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
