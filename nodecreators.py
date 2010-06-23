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

import ofdmaphy.OFDMAPhy
import ofdmaphy.Station
import scenarios.interfaces
import openwns.node
import rise.Mobility
import openwns.geometry.position

class BSCreator(scenarios.interfaces.INodeCreator):

    class BS(openwns.node.Node, scenarios.interfaces.INode):

        def __init__(self, transmitPower, centerFrequency):
            openwns.node.Node.__init__(self, "BS")
            self.setProperty("Type", "BS")
            self.name += str(self.nodeID)

            #self.setPosition(openwns.geometry.position.Position(0.0, 0.0, 0.0))
            #self.mobility.mobility.logger.enabled=False
            self.sender = ofdmaphy.Station.Sender(self, "BS", [ofdmaphy.Transmitter.TransmitterDropIn()], centerFrequency)
            self.sender.txPower = transmitPower

        def getPosition(self):
            self.mobility.getCoords()

        def setPosition(self, position):
            print "Setting BS position to %f, %f, %f" % (position.x, position.y, position.z)
            self.mobility = rise.Mobility.Component(node = self, name = "Mobility BS"+str(self.nodeID), mobility = rise.Mobility.No(position))

        def setAntenna(self, antenna):
            self.sender.antennas = [antenna]

        def setChannelModel(self, channelmodel):
            ## todo later
            pass

    def __init__(self, transmitPower, centerFrequency):
        ofdmaSystem = ofdmaphy.OFDMAPhy.OFDMASystem("ofdma")
        openwns.simulator.OpenWNS.modules.ofdmaPhy.updateSystem(ofdmaSystem)

        self.transmitPower = transmitPower
        self.centerFrequency = centerFrequency

    def create(self):
        return BSCreator.BS(self.transmitPower, self.centerFrequency)

class UECreator(scenarios.interfaces.INodeCreator):

    class UE(openwns.node.Node, scenarios.interfaces.INode):

        def __init__(self, centerFrequency):
            openwns.node.Node.__init__(self, "UE")
            self.setProperty("Type", "UE")
            
            self.name += str(self.nodeID)
            self.scanner = ofdmaphy.Station.Scanner(self, "UE" + str(self.nodeID), [ofdmaphy.Receiver.ReceiverDropIn()],  centerFrequency)
            self.scanner.receiver[0].receiverNoiseFigure = "7 dB"
            self.scanner.rxpProbeName = "RxPower"
            self.scanner.sinrProbeName = "SINR"
            self.scanner.pathlossProbeName = "Pathloss"
            self.scanner.maxRxpProbeName = "MaxRxPower"
            self.scanner.maxSINRProbeName = "MaxSINR"
            self.scanner.minPathlossProbeName = "MinPathloss"
            self.scanner.distanceProbeName = "Distance"

        def setAntenna(self, antenna):
            pass

        def getPosition(self):
            self.mobility.getCoords()

        def setPosition(self, position):
            print "Setting UE position to %f, %f, %f" % (position.x, position.y, position.z)
            self.mobility = rise.Mobility.Component(node = self, name = "Mobility UE"+str(self.nodeID), mobility = rise.Mobility.No(position))


        def setChannelModel(self, channelmodel):
            ## todo later
            pass

    def __init__(self, centerFrequency):
        self.centerFrequency = centerFrequency

    def create(self):
        return UECreator.UE(self.centerFrequency)

# Construct simple Receiver / Measurer Node
class MS(openwns.node.Node):
    mobility = None
    scanner = None

    def __init__(self, name, mobility):
        super(MS, self).__init__(name)
        self.setProperty("Type", "MS")
        self.mobility = rise.Mobility.Component(self,
                                                "Mobility Component",
                                                mobility)
        self.mobility.mobility.logger.enabled=False
        self.scanner = ofdmaphy.Station.Scanner(self, name, [ofdmaphy.Receiver.ReceiverDropIn()])
        self.scanner.rxpProbeName = Config.rxpProbeName
        self.scanner.sinrProbeName = Config.sinrProbeName


