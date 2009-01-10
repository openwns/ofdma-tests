import math
import openwns
import rise.scenario.Hexagonal
import rise.scenario.Manhattan
import rise.scenario.Deployments

class hexConfig:
    relInterfererDistance = { 1  : 1,
                              3  : 3 ,
                              4  : 3.464,
                              7  : 4.58,
                              12 : 5.6 } # from Walke, "Mobile Radio Networks"

    center = openwns.Position(x=1000,y=1000)
    numOfCircles = 1
    clusterSize  = 3
    cellRadius   = 80 # [m]

    # Distance between co-channel APs!
    dAP_AP       = cellRadius * math.sqrt(3.0) * relInterfererDistance[clusterSize]
    dAP_RN       = dAP_AP / 2.0

    numAP        = rise.scenario.Hexagonal.numberOfAccessPointsForHexagonalScenario(numOfCircles)
    numRN        = 0

hexagon = rise.scenario.Hexagonal.Hexagonal(hexConfig.center,
                                            hexConfig.numOfCircles,
                                            hexConfig.dAP_AP,
                                            hexConfig.dAP_RN,
                                            hexConfig.cellRadius,
                                            hexConfig.numRN
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
