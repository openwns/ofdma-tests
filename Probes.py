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
