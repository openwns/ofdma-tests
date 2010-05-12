#! /usr/bin/env python
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

import os
import sys

# Append the python sub-dir of WNS--main--x.y ...
sys.path.append(os.path.join('..', '..', '..', 'sandbox', 'default', 'lib', 'python2.4', 'site-packages'))

import pywns.WNSUnit

testSuite = pywns.WNSUnit.TestSuite()

manhattanTest = pywns.WNSUnit.ProbesTestSuite(sandboxPath = os.path.join('..', '..', '..', 'sandbox'),
                                           configFile = 'config.py',
                                           shortDescription = 'Manhattan Scenario',
                                           disabled = False,
                                           disabledReason = "",
                                           requireReferenceOutput = False,
                                           maximumRelativeError = 0.0)

ituInHTest = pywns.WNSUnit.ProbesTestSuite(sandboxPath = os.path.join('..', '..', '..', 'sandbox'),
                                           configFile = 'configITUInH.py',
                                           shortDescription = 'Calibration for InH',
                                           disabled = False,
                                           disabledReason = "",
                                           requireReferenceOutput = True,
                                           maximumRelativeError = 0.06)

ituUMiTest = pywns.WNSUnit.ProbesTestSuite(sandboxPath = os.path.join('..', '..', '..', 'sandbox'),
                                           configFile = 'configITUUMi.py',
                                           shortDescription = 'Calibration for UMi',
                                           disabled = False,
                                           disabledReason = "",
                                           requireReferenceOutput = True,
                                           maximumRelativeError = 0.06)

ituUMaTest = pywns.WNSUnit.ProbesTestSuite(sandboxPath = os.path.join('..', '..', '..', 'sandbox'),
                                           configFile = 'configITUUMa.py',
                                           shortDescription = 'Calibration for UMa',
                                           disabled = False,
                                           disabledReason = "",
                                           requireReferenceOutput = True,
                                           maximumRelativeError = 0.06)

ituRMaTest = pywns.WNSUnit.ProbesTestSuite(sandboxPath = os.path.join('..', '..', '..', 'sandbox'),
                                           configFile = 'configITURMa.py',
                                           shortDescription = 'Calibration for RMa',
                                           disabled = False,
                                           disabledReason = "",
                                           requireReferenceOutput = True,
                                           maximumRelativeError = 0.06)

ituSMaTest = pywns.WNSUnit.ProbesTestSuite(sandboxPath = os.path.join('..', '..', '..', 'sandbox'),
                                           configFile = 'configITUSMa.py',
                                           shortDescription = 'Calibration for SMa',
                                           disabled = False,
                                           disabledReason = "",
                                           requireReferenceOutput = True,
                                           maximumRelativeError = 0.06)

testSuite.addTest(manhattanTest)
testSuite.addTest(ituInHTest)
testSuite.addTest(ituUMiTest)
testSuite.addTest(ituUMaTest)
testSuite.addTest(ituRMaTest)
testSuite.addTest(ituSMaTest)

if __name__ == '__main__':
    # This is only evaluated if the script is called by hand

    # if you need to change the verbosity do it here
    verbosity = 1

    pywns.WNSUnit.verbosity = verbosity

    # Create test runner
    testRunner = pywns.WNSUnit.TextTestRunner(verbosity=verbosity)

    # Finally, run the tests.
    testRunner.run(testSuite)
