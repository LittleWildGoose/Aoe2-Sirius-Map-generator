from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils import *
from AoE2ScenarioParser.datasets.trigger_lists import Age, Operation, DiplomacyState, VisibilityState
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect, TS
import random

input_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\blankda.aoe2scenario"

output_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\大逃杀_平山黑边.aoe2scenario"

scenario = AoE2DEScenario.from_file(input_path)

trigger_manager = scenario.trigger_manager
map_manager = scenario.map_manager

MAP_SIZE = map_manager.map_size


for x in range(0, MAP_SIZE):
    for y in range(0, MAP_SIZE):
        tile = map_manager.get_tile(x, y)
        tile.elevation=0


trigger_manager.remove_triggers(trigger_manager.trigger_display_order)

player_manager = scenario.player_manager
player_manager.active_players = 8

isTeam = False

for player in range(1,9):
    player_manager.players[player].wood=200+275
    player_manager.players[player].food=200 
    player_manager.players[player].stone=200 +100
    player_manager.players[player].gold=100
    player_manager.players[player].allied_victory=True

    if isTeam:
        for player2 in range(1,9):
            if player != player2:
                player_manager.players[player].set_player_diplomacy(player2, 0 if (player2 + player) % 2 == 0 else DiplomacyState.ENEMY )
    else:
        for player2 in range(1,9):
            if player != player2:
                player_manager.players[player].set_player_diplomacy(player2, DiplomacyState.ENEMY )

GAIA =0 
NPC = 8
DAMAGE_VALUE = 10
FLAG_ID = 600
BLACK_UUID = 306
WAIT_TIME = 300
FIRST_TIME = 600 

# WOOD = 0
# FOOD = 1
# GOLD = 2
# STONE = 3
Resource_str = ["food", "wood", "stone", "gold"]


age_str = ["dark", "FEUDAL", "castle", "IMPERIAL"]
age_code = [TechInfo.FEUDAL_AGE.ID, TechInfo.CASTLE_AGE.ID, TechInfo.IMPERIAL_AGE.ID, None]
age_quantity = [500, 800, 1000, 1500]

AGE_SIZE = 4
RESOURCE_SIZE = 4

UPLIMIT = 500
POP_HEAD = 200
displayStr = "小野鹅的大逃杀\n \n"

displayStr = displayStr + f"开局{(FIRST_TIME)/60}分钟后开始刷圈 \n\n圈出现{WAIT_TIME/60}分钟后会刷下一个 \n新圈出现后在旧圈外的会开始掉血 \n"


displayStr += "触发制作：小野鹅"
displayTrigger = trigger_manager.add_trigger(
    name = "display",
    short_description = displayStr,
    display_on_screen = True,
)
displayTrigger.new_condition.research_technology(
    source_player = player,
    technology = TechInfo.BRITONS.ID,
)    
displayTrigger.new_condition.research_technology(
    source_player = player,
    technology = TechInfo.FRANKS.ID,
)

trigger_toView = trigger_manager.add_trigger(
    name = " view all mapp " ,
    looping = 0)

for player in range(1,9):
    trigger_toView.new_effect.set_player_visibility(
        source_player = player,
        target_player = NPC,
        visibility_state = VisibilityState.VISIBLE)
    
    trigger_toView.new_effect.modify_resource(
        quantity = 1,
        tribute_list = 95,
        source_player = player,
        operation = Operation.SET)

    trigger_toView.new_effect.kill_object(
        source_player = NPC,
        area_x1 = 0,
        area_y1	= 0,
        area_x2 = MAP_SIZE -1,
        area_y2	= MAP_SIZE -1,
    )
    


X_MIN, Y_MIN = 0, 0

sizes = [MAP_SIZE-1, 60, 20]

start_size = MAP_SIZE -1
step = 20
min_size = 10

# 用 range 一行生成边长序列
sizes = list(range(start_size, min_size - 1, -step))
print(MAP_SIZE)
print(sizes)

# 存储结果
all_squares = []
all_rectangles = []

# 初始外层
cur_x1, cur_y1 = X_MIN, Y_MIN
cur_x2, cur_y2 = X_MIN + sizes[0], Y_MIN + sizes[0]


triggerForOut = trigger_manager.add_trigger(
    name = "Fisrt", 
    enabled = True)

triggerForOut.new_condition.timer(timer=FIRST_TIME)


for i in range(1, len(sizes)):
    parent_size = cur_x2 - cur_x1
    child_size = sizes[i]

    margin = child_size // 2  # 保证能放下小方块
    x = random.randint(cur_x1 + margin, cur_x2 - margin)
    y = random.randint(cur_y1 + margin, cur_y2 - margin)

    print([x,y,margin])

    half = child_size // 2
    inner_x1 = x - half
    inner_y1 = y - half
    inner_x2 = x + half
    inner_y2 = y + half

    # 保存正方形
    all_squares.append(((inner_x1, inner_y1), (inner_x2, inner_y2)))

    # 四个矩形（父正方形 - 子正方形）
    rects = [
        (cur_x1, inner_y2, cur_x2, cur_y2),   # 上
        (cur_x1, cur_y1, cur_x2, inner_y1),   # 下
        (cur_x1, inner_y1, inner_x1, inner_y2), # 左
        (inner_x2, inner_y1, cur_x2, inner_y2)  # 右
    ]
    all_rectangles.append(rects)

    # 更新当前正方形，作为下一轮的父正方形
    cur_x1, cur_y1, cur_x2, cur_y2 = inner_x1, inner_y1, inner_x2, inner_y2

    print(f"\n第{i}层正方形:", (inner_x1, inner_y1, inner_x2, inner_y2))

    trigger = trigger_manager.add_trigger(
        name = f"刷圈{i}", 
        enabled = False)

    
    triggerForOut.new_effect.activate_trigger(
        trigger.trigger_id,
    )
    

    for x111 in range(cur_x1, cur_x2, 3):
        trigger.new_effect.create_object(

            object_list_unit_id = FLAG_ID,
            source_player = NPC,
            location_x = x111,
            location_y = cur_y1,
        )
        trigger.new_effect.create_object(

            object_list_unit_id = FLAG_ID,
            source_player = NPC,
            location_x = x111,
            location_y = cur_y2,
        )
    for y111 in range(cur_y1, cur_y2, 3):
        trigger.new_effect.create_object(

            object_list_unit_id = FLAG_ID,
            source_player = NPC,
            location_x = cur_x1,
            location_y = y111,
        )
        trigger.new_effect.create_object(

            object_list_unit_id = FLAG_ID,
            source_player = NPC,
            location_x = cur_x2,
            location_y = y111,
        )

    triggerForOut = trigger_manager.add_trigger(
        name = f"刷圈{i}out", 
        enabled = False)
    
    triggerForOut.new_condition.timer(timer=WAIT_TIME)
    
    trigger.new_effect.activate_trigger(
        triggerForOut.trigger_id,
    )
    
    triggerForOut.new_effect.kill_object(
        source_player = NPC,
        area_x1 = 0,
        area_y1	= 0,
        area_x2 = MAP_SIZE -1,
        area_y2	= MAP_SIZE -1,
    )
    
    trigger = trigger_manager.add_trigger(
        name = f" die player{i}" ,
        enabled = False,
        looping = 1)

    delay = 2
    for rec in rects:

        delay += 1

        triggerTemp = trigger_manager.add_trigger(
            name = f"刷圈{i}outDelay{delay}", 
            enabled = False)

        triggerTemp.new_condition.timer(timer=delay)

        for x111 in range(rec[0], rec[2]+1):
            for y111 in range(rec[1], rec[3]+1):
                triggerTemp.new_effect.create_object(
                    object_list_unit_id = BLACK_UUID,
                    source_player = GAIA,
                    location_x = x111,
                    location_y = y111,
                )

        triggerForOut.new_effect.activate_trigger(
            triggerTemp.trigger_id,
        )


        for player in range(1,8):
            trigger.new_effect.damage_object(
                quantity = DAMAGE_VALUE,
                object_list_unit_id = None,
                source_player = player,
                area_x1 = rec[0],
                area_y1	= rec[1],
                area_x2 = rec[2],
                area_y2	= rec[3],
                object_group = None,
                object_type = None,
                selected_object_ids = None)
    
    triggerForOut.new_effect.activate_trigger(
        trigger.trigger_id,
    )
    




scenario.write_to_file(output_path)

