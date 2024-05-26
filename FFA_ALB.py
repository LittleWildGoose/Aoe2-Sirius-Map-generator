from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils import *

input_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\blank.aoe2scenario"

output_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\parserTestOutput.aoe2scenario"

#  13 7g 5s 6f 8s 3d
# 20 3d
# 30 3d

INIT_DEER =3 

BOUND_START = 120
BOUND_WIDTH = 20
MAP_SIZE = 280 

BLOCK_SIZE = 80

TREE_SQUARE = 5


BOUND_AREA_X1_LIST =[0,0,BOUND_START+BOUND_WIDTH,BOUND_START+BOUND_WIDTH]
BOUND_AREA_X2_LIST =[BOUND_START,BOUND_START,MAP_SIZE,MAP_SIZE]

BOUND_AREA_Y1_LIST =[0,MAP_SIZE//2,0,MAP_SIZE//2]
BOUND_AREA_Y2_LIST =[MAP_SIZE//2,MAP_SIZE,MAP_SIZE//2,MAP_SIZE]

assert len(BOUND_AREA_X1_LIST) == len(BOUND_AREA_X2_LIST)
assert len(BOUND_AREA_X1_LIST) == len(BOUND_AREA_Y1_LIST)
assert len(BOUND_AREA_X1_LIST) == len(BOUND_AREA_Y2_LIST)

def onePlayerBlock(xOffset, yOffSet, directX = 1 ,directY =1):

    TC_CENTER_X = 30
    TC_CENTER_Y = 30
    
    xOffset = xOffset+TC_CENTER_X
    yOffSet = yOffSet+TC_CENTER_Y

    trigger = trigger_manager.add_trigger(f"Spawn player at" + str(xOffset) + str(yOffSet))

    for x in range(10):
        for y in range(5):
            addTree(map_manager, trigger, x-22, y -4 - x,xOffset, yOffSet,directX,directY)


    for x in range(10):
        for y in range(5):
            addTree(map_manager, trigger, x-22 , y +6 + x,xOffset, yOffSet,directX,directY)


    for x in range(5):
        for y in range(10):
            addTree(map_manager, trigger, x +15 , y -10,xOffset, yOffSet,directX,directY)

    addAny(map_manager, trigger, 0, 0, TC_ID,xOffset, yOffSet)
    addAny(map_manager, trigger, 0, 1, VIL_ID,xOffset, yOffSet)
    addAny(map_manager, trigger, 0, 2, VIL_ID,xOffset, yOffSet)
    addAny(map_manager, trigger, 0, 3, VIL_ID,xOffset, yOffSet)

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

    for i in range(4) :
        for j in range(2) :
            addGold(map_manager, trigger, 10 +i , j+5 -i , xOffset, yOffSet,directX,directY)

    for i in range(INIT_STONE) :
        addStone(map_manager, trigger, -5 , i+15, xOffset, yOffSet,directX,directY)


    for i in range(2) :
        for j in range(2) :
            addGold(map_manager, trigger, -10 +i , j-15 -i , xOffset, yOffSet,directX,directY)


def generateBound():
    trigger = trigger_manager.add_trigger(f"Spawn Bound")
    trigger.looping=False
    trigger.new_condition.timer(
        timer=1
    )
    for x in range(BOUND_WIDTH):
        for y in range(MAP_SIZE):
            addBound(map_manager, trigger, x +BOUND_START ,y, BOUND_ID, EARTH_MOTHER)

    for x in range(MAP_SIZE):
        for y in range(BOUND_WIDTH):
            addBound(map_manager, trigger, x ,y +60, BOUND_ID, EARTH_MOTHER)

    for x in range(MAP_SIZE):
        for y in range(BOUND_WIDTH):
            addBound(map_manager, trigger, x ,y +140, BOUND_ID, EARTH_MOTHER)

scenario = AoE2DEScenario.from_file(input_path)

map_manager = scenario.map_manager
trigger_manager = scenario.trigger_manager


map_manager.map_size = MAP_SIZE

for player in range(1,9):
    trigger = trigger_manager.add_trigger(f"Rename player" +str(player))
    trigger.looping=False
    trigger.new_condition.timer(
        timer=2
    )
    trigger.new_effect.change_player_name(
        source_player=player,
    )



for player in range(1,9):
    trigger = trigger_manager.add_trigger(f"Remove player" +str(player))
    trigger.looping=False

    trigger.new_condition.player_defeated(
        source_player=player,
    )
    trigger.new_effect.kill_object(
        source_player=player,
    )
    trigger.new_effect.remove_object(
        source_player=EARTH_MOTHER,
        area_x1 = BOUND_AREA_X1_LIST[(player-1)//2],
        area_x2 = BOUND_AREA_X2_LIST[(player-1)//2],
        area_y1 = BOUND_AREA_Y1_LIST[(player-1)//2],
        area_y2 = BOUND_AREA_Y2_LIST[(player-1)//2]
    )



for player in range(1,9):
    trigger = trigger_manager.add_trigger(f"Remove Bound For final" +str(player))
    trigger.looping=False
    if player <=4:
        for i in range(1,5):
            if i != player:
                trigger.new_condition.player_defeated(
                    source_player=i,
                )
    else:
        for i in range(5,9):
            if i != player:
                trigger.new_condition.player_defeated(
                    source_player=i,
                )


    trigger.new_effect.remove_object(
        source_player=EARTH_MOTHER,
        area_x1 = 0,
        area_x2 = BOUND_START + BOUND_WIDTH //2,
        area_y1 = 0,
        area_y2 = MAP_SIZE
    )



onePlayerBlock(0,0,1,1)

onePlayerBlock(60,0,-1,-1)


onePlayerBlock(120,0,1,1)

onePlayerBlock(160,0,-1,-1)


onePlayerBlock(0,160,1,1)

onePlayerBlock(40,160,-1,-1)


onePlayerBlock(120,160,1,1)

onePlayerBlock(160,160,-1,-1)

generateBound()
scenario.write_to_file(output_path)

