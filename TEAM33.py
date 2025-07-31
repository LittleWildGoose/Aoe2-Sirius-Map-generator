from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils import *

input_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\blank.aoe2scenario"

output_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\parserTestOutput.aoe2scenario"

#  13 7g 5s 6f 8s 3d
# 20 3d
# 30 3d

INIT_DEER =3 

BOUND_START = 130
BOUND_WIDTH = 20
MAP_SIZE = 350 

ROUND_ONE_LIMIT = 90
ONE_MINUTE = 60

LEFT_SIZE =90

BOUND_AREA_X1_LIST =[0,0,BOUND_START+BOUND_WIDTH,BOUND_START+BOUND_WIDTH]
BOUND_AREA_X2_LIST =[BOUND_START,BOUND_START,MAP_SIZE,MAP_SIZE]

BOUND_AREA_Y1_LIST =[0,MAP_SIZE//2,0,MAP_SIZE//2]
BOUND_AREA_Y2_LIST =[MAP_SIZE//2,MAP_SIZE,MAP_SIZE//2,MAP_SIZE]

assert len(BOUND_AREA_X1_LIST) == len(BOUND_AREA_X2_LIST)
assert len(BOUND_AREA_X1_LIST) == len(BOUND_AREA_Y1_LIST)
assert len(BOUND_AREA_X1_LIST) == len(BOUND_AREA_Y2_LIST)

def onePlayerBlock(xOffset, yOffSet, directX = 1 ,directY =1, player =EARTH_MOTHER):

    TC_CENTER_X = 35
    TC_CENTER_Y = 45
    
    xOffset = xOffset+TC_CENTER_X
    yOffSet = yOffSet+TC_CENTER_Y

    trigger = trigger_manager.add_trigger(f"Spawn player at" + str(xOffset) + str(yOffSet))

    for x in range(10):
        for y in range(5):
            addTree(map_manager, trigger, x-25, y -7 - x,xOffset, yOffSet,directX,directY)


    for x in range(10):
        for y in range(5):
            addTree(map_manager, trigger, x-25 , y +10 + x,xOffset, yOffSet,directX,directY)


    for x in range(5):
        for y in range(10):
            addTree(map_manager, trigger, x +15 , y -10,xOffset, yOffSet,directX,directY)


    for i in range(10) :
        changeElevation(map_manager, x +20 , i-10,2, xOffset, yOffSet,directX,directY)
        changeElevation(map_manager, x +19 , i-10, 1, xOffset, yOffSet,directX,directY)
        changeElevation(map_manager, x +21 , i-10, 1, xOffset, yOffSet,directX,directY)

    addAny(map_manager, trigger, 0, 0, TC_ID,xOffset, yOffSet,1,1,player)
    addAny(map_manager, trigger, 0, 1, VIL_ID,xOffset, yOffSet,1,1,player)
    addAny(map_manager, trigger, 0, 2, VIL_ID,xOffset, yOffSet,1,1,player)
    addAny(map_manager, trigger, 0, 3, VIL_ID,xOffset, yOffSet,1,1,player)
    addPig(map_manager, trigger, 0, 4,xOffset, yOffSet)
    addPig(map_manager, trigger, 0, 5,xOffset, yOffSet)

    for i in range(INIT_SHEEP) :
        addSheep(map_manager, trigger, -1 , i, xOffset, yOffSet)


    for i in range(5) :
        addTree(map_manager, trigger, -2 , i, xOffset, yOffSet)

    for i in range(INIT_DEER) :
        addDeer(map_manager, trigger, -25 , i-5, xOffset, yOffSet,directX,directY)

    for i in range(INIT_DEER) :
        addDeer(map_manager, trigger, 15 , i+25, xOffset, yOffSet,directX,directY)

    for i in range(3) :
        for j in range(2) :
            addFruit(map_manager, trigger, 10 +j , i-15, xOffset, yOffSet,directX,directY)
            changeElevation(map_manager, 15 +j , i-20, 1, xOffset, yOffSet,directX,directY)


    for i in range(4) :
        for j in range(2) :
            addGold(map_manager, trigger, 10 +i , j+5 -i , xOffset, yOffSet,directX,directY)
            changeElevation(map_manager, 15 +i , j+10, 1, xOffset, yOffSet,directX,directY)


    for i in range(INIT_STONE) :
        addStone(map_manager, trigger, -5 -i , 15, xOffset, yOffSet,directX,directY)

    for i in range(INIT_STONE) :
        changeElevation(map_manager, -7 +i , 20,2, xOffset, yOffSet,directX,directY)
        changeElevation(map_manager, -7 +i , 19, 1, xOffset, yOffSet,directX,directY)
        changeElevation(map_manager, -7 +i , 21, 1, xOffset, yOffSet,directX,directY)

    for i in range(2) :
        for j in range(2) :
            addGold(map_manager, trigger, -10 +i , j-15 -i , xOffset, yOffSet,directX,directY)


    for i in range(2) :
        for j in range(2) :
            addGold(map_manager, trigger, -30 +i , j-30 -i , xOffset, yOffSet,directX,directY)

    for i in range(2) :
        for j in range(2) :
            addStone(map_manager, trigger, i , j-40 -i , xOffset, yOffSet,directX,directY)

    for i in range(2) :
        for j in range(2) :
            addStone(map_manager, trigger, -30 +i , j+30 -i , xOffset, yOffSet,directX,directY)

            
    for i in range(2) :
        for j in range(2) :
            addGold(map_manager, trigger, i , j+40 -i , xOffset, yOffSet,directX,directY)

scenario = AoE2DEScenario.from_file(input_path)

map_manager = scenario.map_manager
trigger_manager = scenario.trigger_manager


map_manager.map_size = MAP_SIZE


onePlayerBlock(MAP_SIZE//2 - 30,0,1,1, 1)

onePlayerBlock(MAP_SIZE //2 + 30,0,-1,-1, 2)





onePlayerBlock(MAP_SIZE//2 - 30,60,1,1,3)

onePlayerBlock(MAP_SIZE//2 + 30,60,-1,-1,4)

onePlayerBlock(MAP_SIZE//2 - 30 ,120,1,1,5 )

onePlayerBlock(MAP_SIZE//2 + 30,120,-1,-1,6)

# onePlayerBlock(BOUND_START + BOUND_WIDTH ,MAP_SIZE-LEFT_SIZE,1,1,7)

# onePlayerBlock(BOUND_START + BOUND_WIDTH + 60,MAP_SIZE-LEFT_SIZE,-1,-1,8)

scenario.write_to_file(output_path)

