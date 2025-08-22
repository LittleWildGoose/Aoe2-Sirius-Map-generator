from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils import *
from AoE2ScenarioParser.datasets.trigger_lists import Age, Operation, DiplomacyState
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect, TS

input_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\blank8.aoe2scenario"

output_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\2K人口-小野鹅.aoe2scenario"

scenario = AoE2DEScenario.from_file(input_path)

trigger_manager = scenario.trigger_manager

trigger_manager.remove_triggers(trigger_manager.trigger_display_order)

player_manager = scenario.player_manager
player_manager.active_players = 8

for player in range(1,9):
    player_manager.players[player].food=200
    player_manager.players[player].wood=200
    player_manager.players[player].stone=200
    player_manager.players[player].gold=100
    player_manager.players[player].allied_victory=True
    for player2 in range(1,9):
        if player != player2:
            player_manager.players[player].set_player_diplomacy(player2, 0 if (player2 + player) % 2 == 0 else DiplomacyState.ENEMY )

print(DiplomacyState.ENEMY)
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
displayStr = "自己杀死或者Del的单位不会消耗人口， 可用人口低于200之后会减少人口上限\n \n"
for player in range(1,9):
    displayStr = displayStr + "玩家 " + str(player) + "还有 <Variable " +str(player)+">\n"


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

TIME_LIMIT = 1

VAR2_OFFSET = 10
for player in range(1,9):
    prev_trigger = None

    trigger = trigger_manager.add_trigger(
        name = " die player at" + str(player) + " for " ,
        looping = 1)

    trigger.new_condition.timer(timer=TIME_LIMIT)

    trigger.new_effect.change_variable(
        quantity = UPLIMIT,
        operation=Operation.SET,
        variable = player
    )
    
    trigger.new_effect.modify_variable_by_resource(
        source_player = player,
        tribute_list = 154,
        operation=Operation.SUBTRACT,
        variable = player
    )


LEQ = 3
for player in range(1,9):
    prev_trigger = None

    trigger = trigger_manager.add_trigger(
        name = " die player at" + str(player) + " for " ,
        looping = 1)

    trigger.new_condition.timer(timer=TIME_LIMIT)

    trigger.new_condition.variable_value(
        quantity = 200,
        variable = player,
        comparison = LEQ
    )

    trigger.new_effect.modify_resource_by_variable(
        source_player = player,
        tribute_list = 32,
        operation=Operation.SET,
        variable =  player
    )





scenario.write_to_file(output_path)

