from AoE2ScenarioParser.datasets.terrains import TerrainId

TREE_ID = 399
GOLD_ID = 66
STONE_ID = 102
FRUIT_ID = 59
PIG_ID = 48
SHEEP_ID = 1243
DEER_ID = 65

WALL_ID = 155

INIT_GOLD = 15
INIT_STONE = 5
INIT_FRUIT = 8
INIT_PIG = 2
INIT_DEER = 4

BOUND_ID = 857
EARTH_MOTHER = 9

def addBound(map_manager, trigger, x ,y, itemToAdd, sourcePlayer):
    tile = map_manager.get_tile(x, y)
    tile.terrain_id = TerrainId.BLACK if itemToAdd == BOUND_ID else TerrainId.FOREST_PINE
    trigger.new_effect.create_object(
        object_list_unit_id=itemToAdd,
        source_player=sourcePlayer,
        location_x=x,
        location_y=y, 
    )


def addAny(map_manager, trigger, x ,y, itemId):
    tile = map_manager.get_tile(x, y)
    tile.terrain_id = TerrainId.FOREST_PINE
    trigger.new_effect.create_object(
        object_list_unit_id=itemId,
        source_player=EARTH_MOTHER,
        location_x=x,
        location_y=y,
    )

def addTree(map_manager, trigger, x ,y):
    addAny(map_manager, trigger, x ,y, TREE_ID)


def addGold(map_manager, trigger, x ,y):
    addAny(map_manager, trigger, x ,y, GOLD_ID)

def addStone(map_manager, trigger, x ,y):
    addAny(map_manager, trigger, x ,y, STONE_ID)


