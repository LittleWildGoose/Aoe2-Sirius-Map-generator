from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils import *
from AoE2ScenarioParser.datasets.trigger_lists import Age, Operation
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect, TS

input_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\精打细算-猫猫周赛-图3.aoe2scenario"

output_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\精打细算-猫猫周赛-图3-小野鹅.aoe2scenario"

scenario = AoE2DEScenario.from_file(input_path)

trigger_manager = scenario.trigger_manager

trigger_manager.remove_triggers(trigger_manager.trigger_display_order)

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

displayStr = ""
for player in range(1,9):
    displayStr = displayStr + "玩家 " + str(player) + "已经浪费了 <Variable " +str(player)+">\n"

displayStr += "触发制作：小野鹅 凛"
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

for player in range(1,9):
    for res in range(RESOURCE_SIZE):
        prev_trigger = None
        for age in range(AGE_SIZE):

            trigger = trigger_manager.add_trigger(
                name = age_str[age] +" age player at" + str(player) + " for " + Resource_str[res],
                looping = 1)
                
            triggerToRemove = trigger_manager.add_trigger(
                name = "set" + age_str[age] +" age player at" + str(player) + " for " + Resource_str[res],
                enabled = 0)
            
            triggerToRemove.new_effect.modify_resource(
                quantity= age_quantity[age],
                source_player = player,
                tribute_list = res,
                operation=Operation.SET,
            )


            trigger.new_condition.accumulate_attribute(
                quantity= age_quantity[age] + 1,
                source_player = player,
                attribute = res,
            )
            if age_code[age]:
                trigger.new_condition.research_technology(
                    source_player = player,
                    technology = age_code[age],
                    inverted = True,
                )
            trigger.new_effect.modify_variable_by_resource(
                source_player = player,
                tribute_list = res,
                operation=Operation.ADD,
                variable = player
            )
            trigger.new_effect.change_variable(
                quantity = age_quantity[age],
                operation=Operation.SUBTRACT,
                variable = player
            )
            trigger.new_effect.activate_trigger(
                triggerToRemove.trigger_id,
            )
            if prev_trigger:
                trigger.new_effect.deactivate_trigger(
                    prev_trigger.trigger_id,
                )
            prev_trigger = trigger




scenario.write_to_file(output_path)

