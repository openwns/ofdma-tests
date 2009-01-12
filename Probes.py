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
