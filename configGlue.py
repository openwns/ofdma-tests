###############################################################################
# This file is part of openWNS (open Wireless Network Simulator)
# _____________________________________________________________________________
#
# Copyright (C) 2004-2009
# Chair of Communication Networks (ComNets)
# Kopernikusstr. 5, D-52074 Aachen, Germany
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

import openwns
import openwns.eventscheduler
import openwns.node
import openwns.distribution
import openwns.evaluation.default
import openwns.geometry.position

import ofdmaphy
import ofdmaphy.Station
import ofdmaphy.Receiver
import ofdmaphy.Transmitter
import ofdmaphy.OFDMAPhy

import rise.Mobility

import constanze.traffic
import constanze.node
import constanze.evaluation.default
import ip.Component

import ip
from ip.VirtualARP import VirtualARPServer
from ip.VirtualDHCP import VirtualDHCPServer
from ip.VirtualDNS import VirtualDNSServer
import ip
import ip.evaluation.default

import glue.support.Configuration
import glue.evaluation.acknowledgedModeShortCut


# These are the important configuration parameters:
class Configuration:
    maxSimTime = 0.5
    # must be < 250 (otherwise IPAddress out of range)
    numberOfStations = 4
    # 100 MBit/s
    speed = 100E6
    # 1500 byte
    fixedPacketSize = 1500 * 8
    # traffic generator will offer traffic with speed*load
    load = 0.5

configuration = Configuration()

# create an instance of the WNS configuration
# The variable must be called WNS!!!!
WNS = openwns.Simulator(simulationModel = openwns.node.NodeSimulationModel())
WNS.outputStrategy = openwns.simulator.OutputStrategy.DELETE
WNS.maxSimTime = configuration.maxSimTime # seconds

# The wireless system manager
ofdmaPhySystem = ofdmaphy.OFDMAPhy.OFDMASystem('ofdma')
WNS.modules.ofdmaPhy.systems.append(ofdmaPhySystem)

throughputPerStation = configuration.speed * configuration.load / configuration.numberOfStations

# specific station for this test with StopAndWait DLL
class Station(openwns.node.Node):
    phy = None
    dll = None
    nl = None
    load = None
    mobility = None

    def __init__(self, id, dataRate, xPos, txFreq, rxFreq):
        super(Station, self).__init__("node"+str(id))

        # Physical Layer

        phyStation = ofdmaphy.Station.OFDMAStation(
            [ofdmaphy.Receiver.ReceiverDropIn()], 
            [ofdmaphy.Transmitter.TransmitterDropIn()])
        phyStation.txFrequency = txFreq # MHz
        phyStation.rxFrequency = rxFreq # MHz
        self.phy = ofdmaphy.Station.OFDMAComponent(self, "phy", phyStation)

        # Data Link Layer
        self.dll = glue.support.Configuration.OFDMAShortCut(
            self,
            "ShortCut",
            self.phy.dataTransmission,
            self.phy.notification,
            dataRate)
            
        # Network Layer
        domainName = "node" + str(id) + ".glue.wns.org"
        self.nl = ip.Component.IPv4Component(self, domainName + ".ip",domainName)
        self.nl.addDLL(_name = "glue",
                       # Where to get my IP Address
                       _addressResolver = ip.AddressResolver.VirtualDHCPResolver("theOnlySubnet"),
                       # ARP zone
                       _arpZone = "theOnlySubnet",
                       # We can deliver locally
                       _pointToPoint = False,
                       # DLL service names
                       _dllDataTransmission = self.dll.unicastDataTransmission,
                       _dllNotification = self.dll.unicastNotification)

        # Traffic Generator
        self.load = constanze.node.ConstanzeComponent(self, "constanze")
        
        self.mobility = rise.Mobility.Component(node = self,
                                name = "mobility"+str(id),
                                mobility = rise.Mobility.No(openwns.geometry.position.Position(xPos))
                                )

# Create Nodes and components
for i in xrange(configuration.numberOfStations):
    # Switch Tx/Rx frequencies every second station creating a FDD config
    if(i % 2 == 0):
        isOdd = False
        isEven = True
    else:
        isOdd = True
        isEven = False
    
    txFreq = 5000 + int(isOdd) * 100
    rxFreq = 5000 + int(isEven) * 100
    print str(i) + " " + str(txFreq) + " " + str(rxFreq)
    station = Station(i, configuration.speed, i * 1000.0, txFreq, rxFreq)
    WNS.simulationModel.nodes.append(station)

for i in xrange(configuration.numberOfStations):
    cbr = constanze.traffic.CBR(0.01, throughputPerStation, configuration.fixedPacketSize)
    ipBinding = constanze.node.IPBinding(WNS.simulationModel.nodes[i-1].nl.domainName, WNS.simulationModel.nodes[i].nl.domainName)
    WNS.simulationModel.nodes[i-1].load.addTraffic(ipBinding, cbr)
    ipListenerBinding = constanze.node.IPListenerBinding(WNS.simulationModel.nodes[i-1].nl.domainName)
    listener = constanze.node.Listener(WNS.simulationModel.nodes[i-1].nl.domainName + ".listener")
    WNS.simulationModel.nodes[i-1].load.addListener(ipListenerBinding, listener)

# one Virtual ARP Zone
varp = VirtualARPServer("vARP", "theOnlySubnet")
WNS.simulationModel.nodes = [varp] + WNS.simulationModel.nodes

vdhcp = VirtualDHCPServer("vDHCP@",
                          "theOnlySubnet",
                          "192.168.0.2", "192.168.254.253",
                          "255.255.0.0")

vdns = VirtualDNSServer("vDNS", "ip.DEFAULT.GLOBAL")
WNS.simulationModel.nodes.append(vdns)

WNS.simulationModel.nodes.append(vdhcp)

# modify probes afterwards
glue.evaluation.acknowledgedModeShortCut.installEvaluation(WNS, range(1, configuration.numberOfStations + 1))

ip.evaluation.default.installEvaluation(sim = WNS,
                                        maxPacketDelay = 0.5,     # s
                                        maxPacketSize = 2000*8,   # Bit
                                        maxBitThroughput = 10E6,  # Bit/s
                                        maxPacketThroughput = 1E6 # Packets/s
                                        )

constanze.evaluation.default.installEvaluation(sim = WNS,
                                               maxPacketDelay = 1.0,
                                               maxPacketSize = 16000,
                                               maxBitThroughput = 100e6,
                                               maxPacketThroughput = 10e6,
                                               delayResolution = 1000,
                                               sizeResolution = 2000,
                                               throughputResolution = 10000)

openwns.evaluation.default.installEvaluation(sim = WNS)
openwns.setSimulator(WNS)