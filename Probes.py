from speetcl.probes.ProbesList import *
from speetcl.probes.AccessList import AccessList
from speetcl.probes.StatEval import *

def buildProbes(Config,WNS):
    # build empty probe container
    rxpProbe=Probe()
    rxpProbe.name = Config.rxpProbeName

    # build access Lists for the different IDNames
    msAccessList = AccessList(name = 'MSID')
    msAccessList.addRange(Config.numBS, Config.numBS+Config.numMS-1)
    bsAccessList = AccessList(name = 'BSID')
    bsAccessList.addRange(0, Config.numBS-1)
    xAccessList = AccessList(name = 'rise.scenario.mobility.x')
    xAccessList.unit= 'm'
    xAccessList.addRange(1, Config.xMax)
    yAccessList = AccessList(name = 'rise.scenario.mobility.y')
    yAccessList.unit= 'm'
    yAccessList.addRange(1, Config.yMax)

    # add empty sortingCriterion
    rxpProbe.addSortingCriterion()
    # configure the sorting criterion
    rxpProbe.sortingCriteria[0].addGroup(outputFormat = 'f',
                                         accessList = bsAccessList,
                                         idResolution = 1)

    # Configure the StatEval Object
    PDFconfig = PDFEval()
    PDFconfig.minXValue = -170
    PDFconfig.maxXValue = -40
    PDFconfig.resolution = 130

    # add it to the sortingCriterion
    rxpProbe.sortingCriteria[0].addStatEval(PDFconfig)

    # add another empty sortingCriterion for table output
    rxpProbe.addSortingCriterion()
    rxpProbe.sortingCriteria[1].addTableParameter(parameter = "mean", outputStyle="matlab")
    rxpProbe.sortingCriteria[1].addTableParameter(parameter = "maximum", outputStyle="matlab")
    rxpProbe.sortingCriteria[1].addTableParameter(parameter = "numtrials", outputStyle="matlab")

    rxpProbe.sortingCriteria[1].addGroup(outputFormat = 'c',
                                         accessList = xAccessList,
                                         idResolution = 10)
    rxpProbe.sortingCriteria[1].addGroup(outputFormat = 'r',
                                         accessList = yAccessList,
                                         idResolution = 10)
    rxpProbe.sortingCriteria[1].addGroup(outputFormat = 'f',
                                         accessList = bsAccessList,
                                         idResolution = 1)

    rxpProbe.sortingCriteria[1].addStatEval(MomentsEval())

    # write config to global probes dict
    WNS.globalProbesDict.update({ Config.rxpProbeName : rxpProbe })


    # build empty probe container
    sinrProbe=Probe()
    sinrProbe.name = Config.sinrProbeName

    # add empty sortingCriterion
    sinrProbe.addSortingCriterion()
    # configure the sorting criterion
    sinrProbe.sortingCriteria[0].addGroup(outputFormat = 'f',
                                         accessList = bsAccessList,
                                         idResolution = 1)

    # Configure the StatEval Object
    PDFconfig = PDFEval()
    PDFconfig.minXValue = -30
    PDFconfig.maxXValue = 30
    PDFconfig.resolution = 60

    # add it to the sortingCriterion
    sinrProbe.sortingCriteria[0].addStatEval(PDFconfig)

    # add another empty sortingCriterion for table output
    sinrProbe.addSortingCriterion()
    sinrProbe.sortingCriteria[1].addTableParameter(parameter = "mean", outputStyle="matlab")
    sinrProbe.sortingCriteria[1].addTableParameter(parameter = "maximum", outputStyle="matlab")
    sinrProbe.sortingCriteria[1].addTableParameter(parameter = "numtrials", outputStyle="matlab")

    sinrProbe.sortingCriteria[1].addGroup(outputFormat = 'c',
                                         accessList = xAccessList,
                                         idResolution = 10)
    sinrProbe.sortingCriteria[1].addGroup(outputFormat = 'r',
                                         accessList = yAccessList,
                                         idResolution = 10)
    sinrProbe.sortingCriteria[1].addGroup(outputFormat = 'f',
                                         accessList = bsAccessList,
                                         idResolution = 1)

    sinrProbe.sortingCriteria[1].addStatEval(MomentsEval())


    # add another sortingCriterion for an overall Table
    sinrProbe.addSortingCriterion()
    sinrProbe.sortingCriteria[2].addTableParameter(parameter = "mean", outputStyle="matlab")
    sinrProbe.sortingCriteria[2].addTableParameter(parameter = "maximum", outputStyle="matlab")
    sinrProbe.sortingCriteria[2].addTableParameter(parameter = "numtrials", outputStyle="matlab")
    sinrProbe.sortingCriteria[2].addGroup(outputFormat = 'c',
                                          accessList = xAccessList,
                                          idResolution = 10)
    sinrProbe.sortingCriteria[2].addGroup(outputFormat = 'r',
                                          accessList = yAccessList,
                                          idResolution = 10)
    sinrProbe.sortingCriteria[2].addStatEval(MomentsEval())


    # write config to global probes dict
    WNS.globalProbesDict.update({ Config.sinrProbeName : sinrProbe })
