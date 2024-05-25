from utils import *



BOUND_WIDTH = 8
FINAL_BOUND_OPEN_WIDTH = 16
HALF_BOUND_OPEN_WIDTH = 8

MAP_SIZE = 120 


FINAL_LOWER_BOUND = MAP_SIZE//3 - BOUND_WIDTH//2 -1
FINAL_UPPER_BOUND = MAP_SIZE*2//3 + BOUND_WIDTH//2 


def generateTrees(trigger_manager, map_manager, mapSize):
    TREE_SIZE = 20
    xBase = ((mapSize- 2*BOUND_WIDTH)//3 - TREE_SIZE) //2 

    trigger = trigger_manager.add_trigger(f"Spawn Tree")
    trigger.looping=False
    trigger.new_condition.timer(
        timer=1
    )
    
    for x in range(20):
        for y in range(20):
            addTree(map_manager, trigger, x +xBase, y)
            addTree(map_manager, trigger, mapSize -x -1 -xBase, y)
            addTree(map_manager, trigger, x + xBase, mapSize -y -1 )
            addTree(map_manager, trigger, mapSize -x -1 -xBase , mapSize -y -1)

    for y in range(INIT_STONE):
        addStone(map_manager, trigger, 0, y)
        addStone(map_manager, trigger, 0, mapSize-1 - y)
        addStone(map_manager, trigger, mapSize-1, y)
        addStone(map_manager, trigger, mapSize-1, mapSize-1 -y)

        addStone(map_manager, trigger, FINAL_LOWER_BOUND, y)
        addStone(map_manager, trigger, FINAL_LOWER_BOUND, mapSize-1 - y)
        addStone(map_manager, trigger, FINAL_UPPER_BOUND, y)
        addStone(map_manager, trigger, FINAL_UPPER_BOUND, mapSize-1 -y)


    for y in range(INIT_STONE, INIT_STONE + INIT_GOLD):
        addGold(map_manager, trigger, 0, y)
        addGold(map_manager, trigger, 0, mapSize-1 -y)
        addGold(map_manager, trigger, mapSize-1, y)
        addGold(map_manager, trigger, mapSize-1, mapSize-1 -y)

        addGold(map_manager, trigger, FINAL_LOWER_BOUND, y)
        addGold(map_manager, trigger, FINAL_LOWER_BOUND, mapSize-1 - y)
        addGold(map_manager, trigger, FINAL_UPPER_BOUND, y)
        addGold(map_manager, trigger, FINAL_UPPER_BOUND, mapSize-1 -y)

    for y in range(INIT_STONE + INIT_GOLD, INIT_STONE + INIT_GOLD + INIT_FRUIT):
        addAny(map_manager, trigger, 0, y,FRUIT_ID)
        addAny(map_manager, trigger, 0, mapSize-1 -y,FRUIT_ID)
        addAny(map_manager, trigger, mapSize-1, y,FRUIT_ID)
        addAny(map_manager, trigger, mapSize-1, mapSize-1 -y,FRUIT_ID)

        addAny(map_manager, trigger, 1, y,SHEEP_ID)
        addAny(map_manager, trigger, 1, mapSize-1 -y,SHEEP_ID)
        addAny(map_manager, trigger, mapSize-2, y,SHEEP_ID)
        addAny(map_manager, trigger, mapSize-2, mapSize-1 -y,SHEEP_ID)


        addAny(map_manager, trigger, FINAL_LOWER_BOUND, y,FRUIT_ID)
        addAny(map_manager, trigger, FINAL_LOWER_BOUND, mapSize-1 - y,FRUIT_ID)
        addAny(map_manager, trigger, FINAL_UPPER_BOUND, y,FRUIT_ID)
        addAny(map_manager, trigger, FINAL_UPPER_BOUND, mapSize-1 -y,FRUIT_ID)


        addAny(map_manager, trigger, FINAL_LOWER_BOUND-1, y,SHEEP_ID)
        addAny(map_manager, trigger, FINAL_LOWER_BOUND-1, mapSize-1 - y,SHEEP_ID)
        addAny(map_manager, trigger, FINAL_UPPER_BOUND+1, y,SHEEP_ID)
        addAny(map_manager, trigger, FINAL_UPPER_BOUND+1, mapSize-1 -y,SHEEP_ID)


    for y in range(INIT_STONE + INIT_GOLD+ INIT_FRUIT, INIT_STONE + INIT_GOLD + INIT_FRUIT + INIT_PIG):
        addAny(map_manager, trigger, 0, y,PIG_ID)
        addAny(map_manager, trigger, 0, mapSize-1 -y,PIG_ID)
        addAny(map_manager, trigger, mapSize-1, y,PIG_ID)
        addAny(map_manager, trigger, mapSize-1, mapSize-1 -y,PIG_ID)

        addAny(map_manager, trigger, FINAL_LOWER_BOUND, y,PIG_ID)
        addAny(map_manager, trigger, FINAL_LOWER_BOUND, mapSize-1 -y,PIG_ID)
        addAny(map_manager, trigger, FINAL_UPPER_BOUND, y,PIG_ID)
        addAny(map_manager, trigger, FINAL_UPPER_BOUND, mapSize-1 -y,PIG_ID)

    for x in range(1,1+INIT_DEER):
        addAny(map_manager, trigger, x, 0,DEER_ID)
        addAny(map_manager, trigger, x, mapSize-1,DEER_ID)
        addAny(map_manager, trigger, mapSize-1-x, 0,DEER_ID)
        addAny(map_manager, trigger, mapSize-1-x, mapSize-1,DEER_ID)

        addAny(map_manager, trigger, FINAL_LOWER_BOUND-x, 0,DEER_ID)
        addAny(map_manager, trigger, FINAL_LOWER_BOUND-x, mapSize-1,DEER_ID)
        addAny(map_manager, trigger, FINAL_UPPER_BOUND+x, 0,DEER_ID)
        addAny(map_manager, trigger, FINAL_UPPER_BOUND+x, mapSize-1,DEER_ID)

def generateBound(trigger_manager, map_manager,  mapSize):
    generateHalfBound(trigger_manager, map_manager,  mapSize)
    generateFinalBound(trigger_manager, map_manager,  mapSize)

def generateHalfBound(trigger_manager, map_manager,  mapSize):
    trigger = trigger_manager.add_trigger(f"Spawn Half Bound")
    trigger.looping=False
    trigger.new_condition.timer(
        timer=1
    )
    for i in range(1,3):
        for x in range(mapSize):
            itemToAdd = BOUND_ID
            xBase1 = mapSize//6
            xBase2 = mapSize - mapSize//6

            if x > xBase1 - HALF_BOUND_OPEN_WIDTH//2 and x < xBase1 +  HALF_BOUND_OPEN_WIDTH//2 :
                itemToAdd = WALL_ID

            if x > xBase2 - HALF_BOUND_OPEN_WIDTH//2 and x < xBase2 +  HALF_BOUND_OPEN_WIDTH//2 :
                itemToAdd = WALL_ID

            for y in range(BOUND_WIDTH):
                yBase = mapSize*i//3 - BOUND_WIDTH//2
                realY = yBase + y
                source_player = EARTH_MOTHER if itemToAdd == BOUND_ID else y%BOUND_WIDTH +1
                addBound(map_manager, trigger, x ,realY, itemToAdd, source_player)

def generateFinalBound(trigger_manager, map_manager,  mapSize):
    trigger = trigger_manager.add_trigger(f"Spawn Final Bound")
    trigger.looping=False
    trigger.new_condition.timer(
        timer=1
    )
    for i in range(1,3):
        xBase = mapSize*i//3 - BOUND_WIDTH//2

        for y in range(mapSize):
            itemToAdd = BOUND_ID
            if y > mapSize//2 - FINAL_BOUND_OPEN_WIDTH//2 and y < mapSize//2 +  FINAL_BOUND_OPEN_WIDTH//2 :
                itemToAdd = WALL_ID

            for x in range(BOUND_WIDTH):
                realX = xBase + x
                sourcePlayer = EARTH_MOTHER if itemToAdd == BOUND_ID else x%BOUND_WIDTH +1
                addBound(map_manager, trigger, realX ,y, itemToAdd, sourcePlayer)