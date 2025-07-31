from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils import *
from AoE2ScenarioParser.datasets.trigger_lists import Age, Operation
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect, TS

input_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\代理人44_blank.aoe2scenario"

output_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\代理人44_打海给炮舰_ban三国dlc开树_25Jul9.aoe2scenario"

scenario = AoE2DEScenario.from_file(input_path)

trigger_manager = scenario.trigger_manager


# WOOD = 0
# FOOD = 1
# GOLD = 2
# STONE = 3w
Resource_str = ["food", "wood", "stone", "gold"]

MAR_TIME_LIMIT=1500
TIME_LIMIT=2100
FUHUO_TIME_LIMIT=1800
SANGUO_TIME_LIMIT=TIME_LIMIT+5

sanguo = [TechInfo.HEAVY_HEI_GUANG_CAVALRY.ID, TechInfo.MING_GUANG_ARMOR.ID, TechInfo.TUNTIAN.ID, TechInfo.ELITE_TIGER_CAVALRY.ID, TechInfo.SHU.ID, TechInfo.WU.ID]

huojian = [TechInfo.CHINESE.ID, TechInfo.KOREANS.ID, TechInfo.KHITANS.ID, TechInfo.JURCHENS.ID]

for player in [4,5]:
    trigger = trigger_manager.add_trigger(
        name = "open 炮舰 at" + str(player))
    trigger.new_condition.research_technology(
        source_player=player,
        technology=TechInfo.CHEMISTRY.ID)
    trigger.new_effect.enable_disable_object(
        source_player=player,
        object_list_unit_id=UnitInfo.CANNON_GALLEON.ID,
        enabled = True)
    trigger = 0;   

for player in [1,8]:


    # ban sea
    for _ in range(0,1):
        trigger = trigger_manager.add_trigger(
            name = "ban sea at" + str(player))


        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.GALLEON.ID,
            enabled = False)
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.WAR_GALLEY.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.FAST_FIRE_SHIP.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.HEAVY_DEMOLITION_SHIP.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.ELITE_CANNON_GALLEON.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.DRAGON_SHIP.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.FIRE_GALLEY.ID,
            enabled = False)
    
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.LOU_CHUAN.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.THIRISADAI.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.GALLEY.ID,
            enabled = False)

        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.CANNON_GALLEON.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.DEMOLITION_RAFT.ID,
            enabled = False)

        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.TURTLE_SHIP.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.LONGBOAT.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_object(
                source_player=player,
                object_list_unit_id=UnitInfo.TRANSPORT_SHIP.ID,
                enabled = False)

        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.CARAVEL.ID,
            enabled = False)

    trigger = 0;   
    # Ban市场开树 open市场
    for _ in range(0,1):
        trigger = trigger_manager.add_trigger(
            name = "ban 市场开树 at" + str(player))

        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.TRACTION_TREBUCHET.ID,
            enabled = False)

        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.TREBUCHET_PACKED.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.BALLISTA_ELEPHANT.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=BuildingInfo.MARKET.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.ONAGER.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.HEAVY_ROCKET_CART.ID,
            enabled = False)
        
        # open市场
        trigger = trigger_manager.add_trigger(
            name = "open 市场 at" + str(player))
        
        trigger.new_condition.timer(timer=MAR_TIME_LIMIT)

        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=BuildingInfo.MARKET.ID,
            enabled = True)
    

    trigger = 0;   

    # open弩象
    for _ in range(0,1):
        trigger = trigger_manager.add_trigger(
            name = "open nuxiang at" + str(player))
        
        trigger.new_condition.timer(timer=TIME_LIMIT)
        trigger.new_condition.research_technology(
            source_player=player,
            technology=TechInfo.KHMER.ID)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.BALLISTA_ELEPHANT.ID,
            enabled = True)
    

    trigger = 0;   

    # open kaishu
    for _ in range(0,1):
        trigger = trigger_manager.add_trigger(
            name = "open kaishu at" + str(player))
        
        trigger.new_condition.timer(timer=TIME_LIMIT)

        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.TREBUCHET_PACKED.ID,
            enabled = True)
        
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.ONAGER.ID,
            enabled = True)


    trigger = 0;   

    for huojianciv in huojian:
        trigger = trigger_manager.add_trigger(
            name = "Enable 火箭车 for player at" + str(player) + "when civ" + str(huojianciv))

        trigger.new_condition.timer(timer=SANGUO_TIME_LIMIT)
        trigger.new_condition.research_technology(
            source_player=player,
            technology=huojianciv)
        
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.ONAGER.ID,
            enabled = False)
        
        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=TechInfo.HEAVY_ROCKET_CART.ID,
            enabled = True)
        
        

    trigger = 0;   

    # open sanguo
    for sanguociv in sanguo:
        trigger = trigger_manager.add_trigger(
            name = "Enable xioabaoji for player at" + str(player) + "when civ" + str(sanguociv))
            
        trigger.new_condition.timer(timer=SANGUO_TIME_LIMIT)
        trigger.new_condition.research_technology(
            source_player=player,
            technology=sanguociv)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.TRACTION_TREBUCHET.ID,
            enabled = True)
        
        trigger.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.TREBUCHET_PACKED.ID,
            enabled = False)


    trigger = 0;   



scenario.write_to_file(output_path)

