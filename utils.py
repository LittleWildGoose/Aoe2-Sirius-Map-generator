from AoE2ScenarioParser.datasets.terrains import TerrainId

TREE_ID = 399
GOLD_ID = 66
STONE_ID = 102
FRUIT_ID = 59
PIG_ID = 48
SHEEP_ID = 1243
DEER_ID = 65

WALL_ID = 155
TC_ID = 109
VIL_ID = 83

INIT_GOLD = 15
INIT_STONE = 5
INIT_FRUIT = 8
INIT_SHEEP = 8
INIT_PIG = 2
INIT_DEER = 4

BOUND_ID = 857
EARTH_MOTHER = 9

def changeElevation	(map_manager, x ,y,elevation, x_offSet =0, y_offSet =0,directX =1, directY =1):
    tile = map_manager.get_tile(directX*x+x_offSet, directY*y+y_offSet)
    tile.elevation = elevation


def addBound(map_manager, trigger, x ,y, itemToAdd, sourcePlayer):
    tile = map_manager.get_tile(x, y)
    tile.terrain_id = TerrainId.ROAD if itemToAdd == BOUND_ID else TerrainId.FOREST_PINE
    trigger.new_effect.create_object(
        object_list_unit_id=itemToAdd,
        source_player=sourcePlayer,
        location_x=x,
        location_y=y, 
    )


def addAny(map_manager, trigger, x ,y, itemId, x_offSet =0, y_offSet =0,directX =1, directY =1, player = EARTH_MOTHER):
    tile = map_manager.get_tile(directX*x+x_offSet, directY*y+y_offSet)
    tile.terrain_id = TerrainId.FOREST_PINE
    trigger.new_effect.create_object(
        object_list_unit_id=itemId,
        source_player=player,
        location_x=directX*x+x_offSet,
        location_y=directY*y+y_offSet,
    )

def addTree(map_manager, trigger, x ,y, x_offSet =0, y_offSet =0,directX =1, directY =1):
    addAny(map_manager, trigger, x ,y, TREE_ID, x_offSet, y_offSet,directX,directY)


def addGold(map_manager, trigger, x ,y, x_offSet =0, y_offSet =0,directX =1, directY =1):
    addAny(map_manager, trigger, x ,y, GOLD_ID, x_offSet, y_offSet,directX,directY)

def addStone(map_manager, trigger, x ,y, x_offSet =0, y_offSet =0,directX =1, directY =1):
    addAny(map_manager, trigger, x ,y, STONE_ID, x_offSet, y_offSet,directX,directY)

def addSheep(map_manager, trigger, x ,y, x_offSet =0, y_offSet =0,directX =1, directY =1):
    addAny(map_manager, trigger, x ,y, SHEEP_ID, x_offSet, y_offSet,directX,directY)

def addDeer(map_manager, trigger, x ,y, x_offSet =0, y_offSet =0,directX =1, directY =1):
    addAny(map_manager, trigger, x ,y, DEER_ID, x_offSet, y_offSet,directX,directY)

def addFruit(map_manager, trigger, x ,y, x_offSet =0, y_offSet =0,directX =1, directY =1):
    addAny(map_manager, trigger, x ,y, FRUIT_ID, x_offSet, y_offSet,directX,directY)

def addPig(map_manager, trigger, x ,y, x_offSet =0, y_offSet =0,directX =1, directY =1):
    addAny(map_manager, trigger, x ,y, PIG_ID, x_offSet, y_offSet,directX,directY)
