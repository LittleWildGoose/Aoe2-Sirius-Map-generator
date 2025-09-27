from AoE2ScenarioParser.datasets.terrains import TerrainId
import argparse
import sys
from pathlib import Path
from datetime import datetime


from pathlib import Path
from datetime import datetime
import sys

from pathlib import Path
from datetime import datetime
import hashlib

def content_hash(text: str) -> str:
    """对字符串内容做哈希，统一换行符为 \n"""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

def file_hash(path: Path) -> str:
    """读取文件内容并计算哈希（统一换行符）"""
    text = path.read_text(encoding="utf-8")
    return content_hash(text)


def clone_file(src_path: str):
    """
    复制指定文件并生成一个新的副本，
    并在副本中注释掉 clone_file 的导入和调用。
    """
    src = Path(src_path).resolve()
    if not src.exists():
        raise FileNotFoundError(f"源文件不存在: {src}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    tgt = src.with_name(f"小野鹅的{src.stem}_copy_{timestamp}.py")

    # 读取源文件
    lines = src.read_text(encoding="utf-8").splitlines()

    new_lines = []
    for line in lines:
        if "from utils import *" in line.strip():
            new_lines.append(f"# {line}")  # 注释掉
        elif "new_file = clone_file(__file__)" in line:
            new_lines.append(f"# {line}")  # 注释掉
        else:
            new_lines.append(line)


    new_content = "\n".join(new_lines) + "\n"

    # 计算新内容的 hash
    new_hash = content_hash(new_content)

    # 检查当前目录下是否已有相同内容的副本
    for f in src.parent.glob(f"*.py"):
        if file_hash(f) == new_hash:
            print(f"跳过生成，已有内容相同的文件: {f}")
            return f

    tgt.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


    return tgt


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
