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
from openwns.evaluation import *

def installDefaultProbesInH(WNS, bsIds, xMin, xMax, yMin, yMax):

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -80,
                           maxXValue =  -20,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -10,
                           maxXValue = 60,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -100,
                           maxXValue = -40,
                           resolution = 130))

def installDefaultProbesUMi(WNS, bsIds, xMin, xMax, yMin, yMax):

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -120,
                           maxXValue =  0,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -10,
                           maxXValue = 20,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -140,
                           maxXValue = -40,
                           resolution = 130))


def installDefaultProbesUMa(WNS, bsIds, xMin, xMax, yMin, yMax):

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -120,
                           maxXValue =  0,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -30,
                           maxXValue = 30,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -140,
                           maxXValue = -50,
                           resolution = 130))

def installDefaultProbesRMa(WNS, bsIds, xMin, xMax, yMin, yMax):

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -80,
                           maxXValue =  0,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -10,
                           maxXValue = 20,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -130,
                           maxXValue = -50,
                           resolution = 130))

def installDefaultProbesSMa(WNS, bsIds, xMin, xMax, yMin, yMax):

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -90,
                           maxXValue =  -10,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -10,
                           maxXValue = 20,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -140,
                           maxXValue = -60,
                           resolution = 130))

def installDebugProbesUMi(WNS, bsIds, xMin, xMax, yMin, yMax):
    # Create a table generator for the evaluation
    table = Table(axis1 = 'rise.scenario.mobility.x', minValue1 = xMin, maxValue1 = xMax, resolution1 = (xMax-xMin)/10,
                  axis2 = 'rise.scenario.mobility.y', minValue2 = yMin, maxValue2 = yMax, resolution2 = (yMax-yMin)/10,
                  values = ['mean', 'max', 'trials'],
                  formats = ['MatlabReadable']
                  )

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.losProbability")
    node.appendChildren(PDF(name = "LosProbability",
                           description = 'LOS Probability',
                           minXValue = 0,
                           maxXValue = 1000,
                           resolution = 100))

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.shadowing")
    node.appendChildren(PDF(name = "Shadowing",
                           description = 'Shadowing [dB]]',
                           minXValue = -100,
                           maxXValue = 100,
                           resolution = 200))

    #node = openwns.evaluation.createSourceNode(WNS, "rise.antenna.ITUAntenna.gain")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = "rise.scenario.StationID", forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "RxPower")
    node.appendChildren(table)
    sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    sep.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -120,
                           maxXValue =  0.0,
                           resolution = 130))
    sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "Pathloss")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "Pathloss",
                           #description = 'Pathloss [dB]',
                           #minXValue = -140,
                           #maxXValue = -50,
                           #resolution = 130))
    #sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "SINR")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "SINR",
    #                       description = 'SINR [dB]',
    #                       minXValue = -30,
    #                       maxXValue = 30,
    #                       resolution = 60))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -120.0,
                           maxXValue =  0.0,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -10,
                           maxXValue = 20,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -140,
                           maxXValue = -40,
                           resolution = 130))

    node = openwns.evaluation.createSourceNode(WNS, "Distance")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Distance",
                           description = 'Distance [m]',
                           minXValue = 0,
                           maxXValue = 2000,
                           resolution = 100))

def installDebugProbesUMa(WNS, bsIds, xMin, xMax, yMin, yMax):
    # Create a table generator for the evaluation
    table = Table(axis1 = 'rise.scenario.mobility.x', minValue1 = xMin, maxValue1 = xMax, resolution1 = (xMax-xMin)/10,
                  axis2 = 'rise.scenario.mobility.y', minValue2 = yMin, maxValue2 = yMax, resolution2 = (yMax-yMin)/10,
                  values = ['mean', 'max', 'trials'],
                  formats = ['MatlabReadable']
                  )

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.losProbability")
    node.appendChildren(PDF(name = "LosProbability",
                           description = 'LOS Probability',
                           minXValue = 0,
                           maxXValue = 1000,
                           resolution = 100))

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.shadowing")
    node.appendChildren(PDF(name = "Shadowing",
                           description = 'Shadowing [dB]]',
                           minXValue = -100,
                           maxXValue = 100,
                           resolution = 200))

    #node = openwns.evaluation.createSourceNode(WNS, "rise.antenna.ITUAntenna.gain")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = "rise.scenario.StationID", forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "RxPower")
    node.appendChildren(table)
    sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    sep.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -120,
                           maxXValue =  0.0,
                           resolution = 130))
    sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "Pathloss")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "Pathloss",
                           #description = 'Pathloss [dB]',
                           #minXValue = -140,
                           #maxXValue = -50,
                           #resolution = 130))
    #sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "SINR")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "SINR",
    #                       description = 'SINR [dB]',
    #                       minXValue = -30,
    #                       maxXValue = 30,
    #                       resolution = 60))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -120.0,
                           maxXValue =  0.0,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -10,
                           maxXValue = 20,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -130,
                           maxXValue = -50,
                           resolution = 130))

    node = openwns.evaluation.createSourceNode(WNS, "Distance")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Distance",
                           description = 'Distance [m]',
                           minXValue = 0,
                           maxXValue = 2000,
                           resolution = 100))

def installDebugProbesRMa(WNS, bsIds, xMin, xMax, yMin, yMax):
    # Create a table generator for the evaluation
    table = Table(axis1 = 'rise.scenario.mobility.x', minValue1 = xMin, maxValue1 = xMax, resolution1 = (xMax-xMin)/10,
                  axis2 = 'rise.scenario.mobility.y', minValue2 = yMin, maxValue2 = yMax, resolution2 = (yMax-yMin)/10,
                  values = ['mean', 'max', 'trials'],
                  formats = ['MatlabReadable']
                  )

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.losProbability")
    node.appendChildren(PDF(name = "LosProbability",
                           description = 'LOS Probability',
                           minXValue = 0,
                           maxXValue = 2000,
                           resolution = 100))

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.shadowing")
    node.appendChildren(PDF(name = "Shadowing",
                           description = 'Shadowing [dB]]',
                           minXValue = -100,
                           maxXValue = 100,
                           resolution = 200))

    #node = openwns.evaluation.createSourceNode(WNS, "rise.antenna.ITUAntenna.gain")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = "rise.scenario.StationID", forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "RxPower")
    node.appendChildren(table)
    sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    sep.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -120,
                           maxXValue =  0.0,
                           resolution = 130))
    sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "Pathloss")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "Pathloss",
                           #description = 'Pathloss [dB]',
                           #minXValue = -140,
                           #maxXValue = -50,
                           #resolution = 130))
    #sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "SINR")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "SINR",
    #                       description = 'SINR [dB]',
    #                       minXValue = -30,
    #                       maxXValue = 30,
    #                       resolution = 60))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -120.0,
                           maxXValue =  0.0,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -30,
                           maxXValue = 30,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -140,
                           maxXValue = -50,
                           resolution = 130))

    node = openwns.evaluation.createSourceNode(WNS, "Distance")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Distance",
                           description = 'Distance [m]',
                           minXValue = 0,
                           maxXValue = 1000,
                           resolution = 100))

def installDebugProbesSMa(WNS, bsIds, xMin, xMax, yMin, yMax):
    # Create a table generator for the evaluation
    table = Table(axis1 = 'rise.scenario.mobility.x', minValue1 = xMin, maxValue1 = xMax, resolution1 = (xMax-xMin)/10,
                  axis2 = 'rise.scenario.mobility.y', minValue2 = yMin, maxValue2 = yMax, resolution2 = (yMax-yMin)/10,
                  values = ['mean', 'max', 'trials'],
                  formats = ['MatlabReadable']
                  )

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.losProbability")
    node.appendChildren(PDF(name = "LosProbability",
                           description = 'LOS Probability',
                           minXValue = 0,
                           maxXValue = 2000,
                           resolution = 100))

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.shadowing")
    node.appendChildren(PDF(name = "Shadowing",
                           description = 'Shadowing [dB]]',
                           minXValue = -100,
                           maxXValue = 100,
                           resolution = 200))

    #node = openwns.evaluation.createSourceNode(WNS, "rise.antenna.ITUAntenna.gain")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = "rise.scenario.StationID", forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "RxPower")
    node.appendChildren(table)
    sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    sep.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -90.0,
                           maxXValue = -10.0,
                           resolution = 130))
    sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "Pathloss")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "Pathloss",
                           #description = 'Pathloss [dB]',
                           #minXValue = -140,
                           #maxXValue = -50,
                           #resolution = 130))
    #sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "SINR")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "SINR",
    #                       description = 'SINR [dB]',
    #                       minXValue = -30,
    #                       maxXValue = 30,
    #                       resolution = 60))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -90.0,
                           maxXValue = -10.0,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -30,
                           maxXValue = 30,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -140,
                           maxXValue = -50,
                           resolution = 130))

    node = openwns.evaluation.createSourceNode(WNS, "Distance")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Distance",
                           description = 'Distance [m]',
                           minXValue = 0,
                           maxXValue = 1000,
                           resolution = 100))

def installDebugProbesInH(WNS, bsIds, xMin, xMax, yMin, yMax):
    # Create a table generator for the evaluation
    table = Table(axis1 = 'rise.scenario.mobility.x', minValue1 = xMin, maxValue1 = xMax, resolution1 = (xMax-xMin)/2,
                  axis2 = 'rise.scenario.mobility.y', minValue2 = yMin, maxValue2 = yMax, resolution2 = (yMax-yMin)/2,
                  values = ['mean', 'max', 'trials'],
                  formats = ['MatlabReadable']
                  )

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.losProbability")
    node.appendChildren(PDF(name = "LosProbability",
                           description = 'LOS Probability',
                           minXValue = 0,
                           maxXValue = 1000,
                           resolution = 100))

    node = openwns.evaluation.createSourceNode(WNS, "rise.scenario.pathloss.ITUPathloss.shadowing")
    node.appendChildren(PDF(name = "Shadowing",
                           description = 'Shadowing [dB]]',
                           minXValue = -100,
                           maxXValue = 100,
                           resolution = 200))

    #node = openwns.evaluation.createSourceNode(WNS, "rise.antenna.ITUAntenna.gain")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = "rise.scenario.StationID", forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "RxPower")
    node.appendChildren(table)
    sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    sep.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -80,
                           maxXValue =  -20,
                           resolution = 130))
    sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "Pathloss")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "Pathloss",
                           #description = 'Pathloss [dB]',
                           #minXValue = -140,
                           #maxXValue = -50,
                           #resolution = 130))
    #sep.appendChildren(table)

    #node = openwns.evaluation.createSourceNode(WNS, "SINR")
    #node.appendChildren(table)
    #sep = node.appendChildren(Separate(by = 'BSID', forAll = bsIds, format = "BSID%d"))
    #sep.appendChildren(PDF(name = "SINR",
    #                       description = 'SINR [dB]',
    #                       minXValue = -30,
    #                       maxXValue = 30,
    #                       resolution = 60))
    #sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, "MaxRxPower")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "RxPower",
                           description = 'Received Power [dBm]',
                           minXValue = -80.0,
                           maxXValue =  -20.0,
                           resolution = 120))


    node = openwns.evaluation.createSourceNode(WNS, "MaxSINR")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "SINR",
                           description = 'SINR [dB]',
                           minXValue = -10,
                           maxXValue = 60,
                           resolution = 300))

    node = openwns.evaluation.createSourceNode(WNS, "MinPathloss")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Minimum Pathloss",
                           description = 'Minimum Pathloss [dB]',
                           minXValue = -100,
                           maxXValue = -40,
                           resolution = 130))

    node = openwns.evaluation.createSourceNode(WNS, "Distance")
    node.appendChildren(table)
    node.appendChildren(PDF(name = "Distance",
                           description = 'Distance [m]',
                           minXValue = 0,
                           maxXValue = 100,
                           resolution = 100))

def installDefaultProbes(WNS, Config):
    # Create a table generator for the evaluation
    table = Table(axis1 = 'rise.scenario.mobility.x', minValue1 = 1, maxValue1 = Config.xMax, resolution1 = Config.xMax/10,
                  axis2 = 'rise.scenario.mobility.y', minValue2 = 1, maxValue2 = Config.yMax, resolution2 = Config.yMax/10,
                  values = ['mean', 'max', 'trials'],
                  formats = ['MatlabReadable']
                  )

    node = openwns.evaluation.createSourceNode(WNS, Config.rxpProbeName)
    node.appendChildren(table)
    sep = node.appendChildren(Separate(by = 'BSID', forAll = range(0, Config.numBS), format = "BSID%d"))
    sep.appendChildren(PDF(name = Config.rxpProbeName,
                           description = 'Received Power [dBm]',
                           minXValue = -170,
                           maxXValue = -40,
                           resolution = 130))
    sep.appendChildren(table)

    node = openwns.evaluation.createSourceNode(WNS, Config.sinrProbeName)
    node.appendChildren(table)
    sep = node.appendChildren(Separate(by = 'BSID', forAll = range(0, Config.numBS), format = "BSID%d"))
    sep.appendChildren(PDF(name = Config.sinrProbeName,
                           description = 'SINR [dB]',
                           minXValue = -30,
                           maxXValue = 30,
                           resolution = 60))
    sep.appendChildren(table)