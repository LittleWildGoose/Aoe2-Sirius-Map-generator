from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils import *
from FFA_v0 import *

input_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\blank.aoe2scenario"

output_path = "C:\\Users\\ramse\\Games\\Age of Empires 2 DE\\76561198098693108\\resources\\_common\\scenario\\parserTestOutput.aoe2scenario"

scenario = AoE2DEScenario.from_file(input_path)

map_manager = scenario.map_manager
trigger_manager = scenario.trigger_manager

MAP_SIZE = 120 


map_manager.map_size = MAP_SIZE


generateTrees(trigger_manager, map_manager, MAP_SIZE)
generateBound(trigger_manager,map_manager, MAP_SIZE)

spawn_array_x = [1,1,1,1,1,1,1,1]
spawn_array_y = [1,2,3,4,5,6,7,8]



scenario.write_to_file(output_path)


