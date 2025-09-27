from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils import *
from AoE2ScenarioParser.datasets.trigger_lists import Age, Operation, DiplomacyState, VisibilityState
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect, TS
import random


input_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\blankda.aoe2scenario"

output_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\大逃杀_随机缩圈_TC养鹅.aoe2scenario"

def make_parent(child_x1, child_y1, child_x2, child_y2, parent_size, MAP_SIZE):
    child_size = child_x2 - child_x1

    min_x1 = max(0, child_x2 - parent_size)
    max_x1 = min(MAP_SIZE - parent_size, child_x1)

    min_y1 = max(0, child_y2 - parent_size)
    max_y1 = min(MAP_SIZE - parent_size, child_y1)

    px1 = random.randint(min_x1, max_x1)
    py1 = random.randint(min_y1, max_y1)

    return px1, py1, px1 + parent_size, py1 + parent_size


def generate_squares(sizes, MAP_SIZE):
    sizes = sorted(sizes)  # 小到大

    # 随机最小圈
    child_size = sizes[0]
    x1 = random.randint(0, MAP_SIZE - child_size)
    y1 = random.randint(0, MAP_SIZE - child_size)
    x2, y2 = x1 + child_size, y1 + child_size
    squares = [(x1, y1, x2, y2)]

    # 逐层生成父圈
    for parent_size in sizes[1:]:
        x1, y1, x2, y2 = make_parent(x1, y1, x2, y2, parent_size, MAP_SIZE)
        squares.append((x1, y1, x2, y2))

    # 反转一下，保证顺序是从大到小（外圈→内圈）
    return list(reversed(squares))

new_file = clone_file(__file__)

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
GOOSE_ID = 1243
KEY_E_ID = 1007

FLAG_ID = 600
FLARE_ID = 274
FLARE_FOREVER_A_ID = 1689
BLACK_UUID = 306

FLARE_DIS = 5
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

trigger_toView.new_effect.kill_object(
    source_player = NPC,
    area_x1 = 0,
    area_y1	= 0,
    area_x2 = MAP_SIZE -1,
    area_y2	= MAP_SIZE -1,
)

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


    trigger_toView.new_effect.add_train_location(
        source_player=player,
        object_list_unit_id=GOOSE_ID,
        object_list_unit_id_2 = BuildingInfo.TOWN_CENTER.ID,
        button_location = 3,
        hotkey = KEY_E_ID)

    trigger_toView.new_effect.enable_disable_object(
        source_player=player,
        object_list_unit_id=GOOSE_ID,
        enabled = True)

    trigger_toView.new_effect.change_train_location(
        source_player=player,
        object_list_unit_id=GOOSE_ID,
        button_location = 3)

    trigger_toView.new_effect.change_object_description(
        source_player=player,
        object_list_unit_id=GOOSE_ID,
        message = "25肉养一只小野鹅，快捷键E")

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


pre_squares = generate_squares(sizes, MAP_SIZE)

for i in range(1, len(pre_squares)):
    cur_x1, cur_y1, cur_x2, cur_y2 = pre_squares[i-1]
    inner_x1, inner_y1, inner_x2, inner_y2 = pre_squares[i]

    # 保存正方形
    all_squares.append(((inner_x1, inner_y1), (inner_x2, inner_y2)))

    # 四个矩形（父正方形 - 子正方形）
    rects = [
        (cur_x1, inner_y2, cur_x2, cur_y2),      # 上
        (cur_x1, cur_y1, cur_x2, inner_y1),      # 下
        (cur_x1, inner_y1, inner_x1, inner_y2),  # 左
        (inner_x2, inner_y1, cur_x2, inner_y2)   # 右
    ]

    print(f"\n第{i}层正方形:", (inner_x1, inner_y1, inner_x2, inner_y2))

    trigger = trigger_manager.add_trigger(
        name = f"刷圈{i}", 
        enabled = False)

    
    triggerForOut.new_effect.activate_trigger(
        trigger.trigger_id,
    )
    
    localCount = 0
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

        localCount +=1
        if localCount % FLARE_DIS==0:
            trigger.new_effect.create_object(

                object_list_unit_id = FLARE_FOREVER_A_ID,
                source_player = NPC,
                location_x = x111,
                location_y = cur_y1,
            )
            trigger.new_effect.create_object(

                object_list_unit_id = FLARE_FOREVER_A_ID,
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

        localCount +=1
        if localCount % FLARE_DIS==0:
            trigger.new_effect.create_object(

                object_list_unit_id = FLARE_FOREVER_A_ID,
                source_player = NPC,
                location_x = cur_x1,
                location_y = y111,
            )
            trigger.new_effect.create_object(

                object_list_unit_id = FLARE_FOREVER_A_ID,
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

