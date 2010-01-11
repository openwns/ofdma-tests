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

import nodecreators

import scenarios.builders
import scenarios.ituM2135

import openwns.geometry.position
import rise.scenario.Propagation

bsPlacer = scenarios.ituM2135.RuralMacroBSPlacer(numberOfCircles = 1)
uePlacer = scenarios.placer.CircularPlacer(numberOfNodes = 0, radius = 0.0)

for azimuth in [30.0, 150.0, 270.0]:
    azimuth = 2*3.14 * azimuth / 360.0
    bsAntennaCreator = scenarios.ituM2135.RuralMacroAntennaCreator(azimuth)

    scenario = scenarios.builders.CreatorPlacerBuilder(nodecreators.BSCreator("49.0 dBm", 800.0), bsPlacer, bsAntennaCreator, nodecreators.UECreator(800.0), uePlacer)

sm = openwns.simulator.getSimulator().rng.seed = 2714
sm = openwns.simulator.getSimulator().simulationModel
bsIDs = [node.nodeID for node in sm.getNodesByType("BS")]
ueIDs = [node.nodeID for node in sm.getNodesByType("UE")]

#for i in xrange(200):
ueCreator = nodecreators.UECreator(800.0)
ue = ueCreator.create()
ue.setPosition(openwns.geometry.position.Position(1000.0, 1000.0, 0.0))
openwns.simulator.getSimulator().simulationModel.nodes.append(ue)

for ue in  sm.getNodesByType("UE"):
    ue.mobility.mobility = scenarios.placer.hexagonal.createAreaScanMobility(100, 866.0, 35.0,  openwns.geometry.position.Position(5000.0, 5000.0, 0.0), 0.0)

id = rise.scenario.Propagation.DropInPropagation.getInstance().findId("DropIn")
rise.scenario.Propagation.DropInPropagation.getInstance().getPair(id, id).pathloss = rise.scenario.Pathloss.ITURMa()

import Probes
Probes.installDefaultProbesRMa(openwns.simulator.getSimulator(), xrange(len(bsIDs)), 3650.0, 6350.0, 3650.0, 6350.0)

openwns.simulator.getSimulator().maxSimTime = 1000.0
openwns.simulator.getSimulator().outputStrategy = openwns.simulator.OutputStrategy.DELETE

def plotMaps(simulator):
    import glob
    from scenarios.plotting.Plotting import *
    files = glob.glob("output/*.m")
    files = [f.replace(".m", "") for f in files]
    files = [f.split("_") for f in files]
    basefiles = []
    for f in files:
        f.remove(f[-1])
        basefiles.append("_".join(f))

    for f in basefiles:
        print "Creating png for %s" % f
        s = SingleMapCreator(f, 10, 1500.0, 1500.0, suffix=".m")
        plotMap(s)
    return True