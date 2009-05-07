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
import math
import openwns
import rise.scenario.Hexagonal
import rise.scenario.Manhattan
import rise.scenario.Deployments

class hexConfig:
    center = openwns.Position(x=1000,y=1000)
    numOfCircles = 1
    clusterSize  = 3
    cellRadius   = 80 # [m]

    # Distance between co-channel APs!
    dAP_AP       = rise.scenario.Hexagonal.getInterfererDistance(clusterSize,cellRadius)
    dAP_RN       = dAP_AP / 2.0

    numAP        = rise.scenario.Hexagonal.numberOfBaseStationsForHexagonalScenario(numOfCircles)
    numRN        = 0

hexagon = rise.scenario.Hexagonal.Hexagonal(hexConfig.clusterSize,
                                            hexConfig.center,
                                            hexConfig.numOfCircles,
                                            hexConfig.cellRadius,
                                            hexConfig.numRN,
                                            0, # numUT
                                            hexConfig.dAP_AP,
                                            hexConfig.dAP_RN,
                                            # more parameters: see default list in Hexagonal.py
                                            )

class manhattanConfig:
    rows               = 4
    columns            = 4
    blockWidth         = 60
    blockHeight        = 60
    streetWidth        = 30
    velocity           = 100
    deploymentStrategy = rise.scenario.Deployments.WINNER_D_6_13_7()

# create Manhattan Scenario, Mobility and Shadowing
manhattan = rise.scenario.Manhattan.Manhattan(rows = manhattanConfig.rows,
                                              columns = manhattanConfig.columns,
                                              blockWidth = manhattanConfig.blockWidth,
                                              blockHeight = manhattanConfig.blockHeight,
                                              streetWidth = manhattanConfig.streetWidth,
                                              velocity = manhattanConfig.velocity,
                                              deploymentStrategy = manhattanConfig.deploymentStrategy)
