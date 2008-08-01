#! /usr/bin/env python2.4

import os

# set path to WNS
import wnsrc

# ... because the module WNS unit test framework is located there.
import pywns.WNSUnit

testSuite = pywns.WNSUnit.TestSuite()

# create a system test
senderTest = pywns.WNSUnit.ProbesTestSuite(sandboxPath = os.path.join('..', '..', '..', 'sandbox'),
                                           executeable = "wns-core",
                                           configFile = 'config.py',
                                           shortDescription = 'Channel Sounder)',
                                           disabled = True,
                                           disabledReason = "PyWNS cannot parse the new table probe bus output",
                                           requireReferenceOutput = False,
                                           maximumRelativeError = 0.0)

testSuite.addTest(senderTest)

if __name__ == '__main__':
    # This is only evaluated if the script is called by hand

    # if you need to change the verbosity do it here
    verbosity = 1

    pywns.WNSUnit.verbosity = verbosity

    # Create test runner
    testRunner = pywns.WNSUnit.TextTestRunner(verbosity=verbosity)

    # Finally, run the tests.
    testRunner.run(testSuite)
