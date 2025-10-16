from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils import *
from AoE2ScenarioParser.datasets.trigger_lists import Age, Operation, DiplomacyState, VisibilityState
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect, TS
import random

from PIL import Image
import numpy as np

def mapGen(input_path, output_path, pic_path):

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
        player_manager.players[player].wood=200
        player_manager.players[player].food=200 
        player_manager.players[player].stone=200
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

    img = Image.open(pic_path).convert("RGB")

    # 转换为 NumPy 数组 (H, W, 3)
    rgb_array = np.array(img)

    print("RGB array shape:", rgb_array.shape)   # (height, width, 3)

    def resize_mean(rgb_array, new_h=240, new_w=240):
        """
        将 RGB array (H,W,3) 从大尺寸缩小为 (new_h, new_w, 3)，使用 mean pooling
        
        参数:
            rgb_array: numpy array, shape (H, W, 3)
            new_h, new_w: 输出的高度和宽度
        返回:
            new_array: numpy array, shape (new_h, new_w, 3)
        """
        H, W, C = rgb_array.shape
        assert C == 3, "必须是 RGB 图像 (H,W,3)"

        # 每个块的大小 (约 5.416...，不是整数)
        block_h = H / new_h
        block_w = W / new_w

        new_array = np.zeros((new_h, new_w, 3), dtype=np.uint8)

        for i in range(new_h):
            for j in range(new_w):
                # 当前块的边界
                y0 = int(i * block_h)
                y1 = int((i + 1) * block_h)
                x0 = int(j * block_w)
                x1 = int((j + 1) * block_w)

                # 防止丢掉边界像素
                y1 = min(y1, H)
                x1 = min(x1, W)

                # 取块并算均值
                block = rgb_array[y0:y1, x0:x1]
                mean_color = block.mean(axis=(0, 1))
                new_array[i, j] = mean_color.astype(np.uint8)

        return new_array



    def save_rgb_as_png(rgb_array, filename="output.png"):
        """
        将 (H,W,3) 的 numpy RGB array 保存为 PNG 文件
        """
        img = Image.fromarray(rgb_array.astype(np.uint8), mode="RGB")
        img.save(filename)

    def find_closest_rgb(target_rgb, rgb_array):
        """
        在 rgb_array 中找到最接近 target_rgb 的像素值
        距离使用欧几里得距离 (sqrt)
        
        参数:
            target_rgb: tuple/list (R, G, B)
            rgb_array: numpy array, shape (H, W, 3) 或 (N, 3)
        返回:
            (y, x), closest_rgb
        """
        target = np.array(target_rgb)

        # 确保输入是三维 (H, W, 3)
        arr = np.array(rgb_array)
        if arr.ndim == 2 and arr.shape[1] == 3:  # (N,3)
            diffs = arr - target
            dists = np.sqrt(np.sum(diffs ** 2, axis=1))
            idx = np.argmin(dists)
            return idx, arr[idx]
        elif arr.ndim == 3 and arr.shape[2] == 3:  # (H,W,3)
            diffs = arr - target
            dists = np.sqrt(np.sum(diffs ** 2, axis=2))
            y, x = np.unravel_index(np.argmin(dists), dists.shape)
            return (y, x), arr[y, x]
        else:
            raise ValueError("rgb_array 必须是 (H,W,3) 或 (N,3) 格式")
        

    def crop_diamond(rgb_array):
        """
        将 RGB array 裁剪成菱形，菱形内部保持原色，外部填充黑色
        使用 for 循环实现
        
        参数:
            rgb_array: (H,W,3) numpy array
        
        返回:
            diamond_img: (H,W,3) numpy array
        """
        H, W, C = rgb_array.shape
        assert C == 3, "必须是 RGB array"

        diamond_img = np.zeros_like(rgb_array)  # 初始化为黑色
        cx, cy = W // 2, H // 2
        half = min(H, W) // 2

        for i in range(H):
            for j in range(W):
                if abs(i - cy) + abs(j - cx) <= half:
                    diamond_img[i,j] = rgb_array[i,j]  # 保留菱形内部颜色

        return diamond_img


    tile_ids = [
        TerrainId.GRASS_1,
        TerrainId.WATER_SHALLOW,
        TerrainId.FOREST_JUNGLE,
        TerrainId.GRASS_1,
        TerrainId.DESERT_SAND,
    ]

    palette = np.array([
        [205, 241, 221],  # 浅绿
        [131, 213, 233],  # 浅蓝
        [178, 227, 203],  # 淡绿
        [144, 152, 144],  # 灰绿
        [242, 239, 227]   # 浅黄
    ])

    def map_image_to_palette(image_array, palette):
        """
        将整个 RGB 图像映射到调色板中的最近颜色（矢量化批量版本）
        
        参数:
            image_array: (H,W,3) numpy array
            palette: (N,3) numpy array 调色板
        返回:
            mapped_image: (H,W,3) numpy array, 映射后的图像
        """
        H, W, C = image_array.shape
        assert C == 3, "image_array 必须是 (H,W,3)"
        
        flat_img = image_array.reshape(-1, 3)  # (H*W,3)
        
        # 扩展维度计算欧几里得距离
        # flat_img: (M,1,3), palette: (1,N,3)
        diff = flat_img[:, None, :] - palette[None, :, :]  # (M,N,3)
        dist = np.linalg.norm(diff, axis=2)               # (M,N)
        
        idx = np.argmin(dist, axis=1)                     # 每个像素对应最近调色板索引
        mapped_flat = palette[idx]                        # (M,3)
        
        mapped_image = mapped_flat.reshape(H, W, 3)
        return mapped_image


    def extract_and_rotate_diamond_array(rgb_array):
        """
        提取菱形区域像素，并旋转 45°，返回 NumPy array
        
        参数:
            rgb_array: (H,W,3) numpy array，正方形图像，外部可能是黑色
        
        返回:
            rotated_array: (M,N,3) numpy array，二维 array，旋转后的菱形像素
        """
        H, W, C = rgb_array.shape
        assert C == 3, "必须是 RGB array"
        
        cx, cy = W // 2, H // 2
        half = min(H,W) // 2

        # 1. 提取菱形区域，按行收集
        diamond_pixels = []
        for i in range(H):
            row = []
            for j in range(W):
                if abs(i - cy) + abs(j - cx) <= half:
                    row.append(rgb_array[i,j])

            if i < H //2 and i != 0:
                diamond_pixels.append(row[: -1])
            diamond_pixels.append(row)
            if i == H /2:
                diamond_pixels.append(row)
                diamond_pixels.append(row)

            if i > H //2 and i != H -1 :
                diamond_pixels.append(row[: -1])
        
        # 用空数组填充
        rotated_array = np.zeros((H, H, 3), dtype=np.uint8)
        
        for x in range(H):
            for y in range(H):
                if x + y < H :
                    rotated_array[x, y] = diamond_pixels[ x  + y][x]
                else:
                    # print(x, y, len(diamond_pixels[ x  + y]), H)
                    rotated_array[x, y] = diamond_pixels[ x  + y][  H -y]

        # for r, row in enumerate(diamond_pixels):
        #     for c, pixel in enumerate(row):
        #         rotated_array[r -c, c] = pixel


        return rotated_array

    resized = resize_mean(rgb_array, MAP_SIZE, MAP_SIZE)

    mapped_img = crop_diamond(resized)
    save_rgb_as_png(mapped_img, "resized.png")


    mapped_img = map_image_to_palette(mapped_img, palette)

    save_rgb_as_png(mapped_img, "mapped_img.png")

    mapped_img = extract_and_rotate_diamond_array(mapped_img)
    save_rgb_as_png(mapped_img, "rotated_array.png")


    def save_rgb_array_txt(rgb_array, filename="output.txt"):
        """
        将 RGB array 保存为 TXT，每行一个像素 [R,G,B]
        """
        H, W, C = rgb_array.shape
        assert C == 3, "RGB array 必须是 (H,W,3)"
        
        with open(filename, "w") as f:
            for i in range(H):
                for j in range(W):
                    f.write(f"{rgb_array[i,j].tolist()}\n")


    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            t = map_manager.get_tile(MAP_SIZE - 1 - y,  x)
            color = mapped_img[ x,y]  # 获取映射后的颜色
            # 找到最近颜色在调色板中的索引
            diffs = palette - color
            dist = np.linalg.norm(diffs, axis=1)
            idx = np.argmin(dist)
            # 根据索引设置 terrain_id
            t.terrain_id = tile_ids[idx]


    scenario.write_to_file(output_path)



    # from sklearn.cluster import KMeans

    # def extract_top_colors_kmeans(rgb_array, n_colors=5):
    #     """
    #     用 K-means 从 RGB array 中提取 n_colors
    #     """
    #     H, W, C = rgb_array.shape
    #     assert C == 3

    #     flat_pixels = rgb_array.reshape(-1,3)
    #     kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(flat_pixels)
    #     return kmeans.cluster_centers_.astype(np.uint8)

    # top_colors = extract_top_colors_kmeans(resized, n_colors=5)
    # print(top_colors)







import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk   # pip install pillow

# Create main window
root = tk.Tk()
root.title("Click Counter + Image Viewer + Save")
root.geometry("550x600")

count = 0
current_image = None  # Store the opened PIL image
img_label = None      # For displaying the image

mapSel = False
picSel = False

mapPath = ""
picPath = ""

# Function: open and display an image
def select_file():
    global img_label, current_image, mapPath, picSel, mapSel, picPath
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png"), ("All files", "*.*")]
    )
    if not file_path:
        return

    # Load and show image
    current_image = Image.open(file_path)
    img = current_image.copy()
    img.thumbnail((400, 400))
    img_tk = ImageTk.PhotoImage(img)

    if img_label:
        img_label.destroy()

    img_label = tk.Label(root, image=img_tk)
    img_label.image = img_tk
    img_label.pack(pady=10)

    file_label_var.set(f"Selected: {file_path}")
    print("select_file", file_path)
    picPath = file_path
    picSel = True
    if mapSel:
        save_button.config(state="normal")  # Enable save button

# Function: open and display an image
def select_fileMap():
    global img_label, current_image, mapPath, picSel, mapSel, picPath
    file_path = filedialog.askopenfilename(
        title="Select an map",
        filetypes=[("Map files", "*.aoe2scenario"), ("All files", "*.*")]
    )
    if not file_path:
        return

    # Load and show image
    file_label_var.set(f"Selected: {file_path}")
    print("select_fileMap", file_path)

    mapPath = file_path

    mapSel = True
    if picSel:
        save_button.config(state="normal")  # Enable save button

# Function: save the current image
def save_image():
    global img_label, current_image, mapPath, picSel, mapSel, picPath
    if current_image is None:
        messagebox.showwarning("No Image", "Please select an image first!")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".aoe2scenario",
        filetypes=[("Map files", "*.aoe2scenario"), ("All files", "*.*")]
    )
    if save_path:
        mapGen(mapPath, save_path, picPath)

# Label for click count
label_var = tk.StringVar(value="小野鹅的地图生成")
label = tk.Label(root, textvariable=label_var, font=("Arial", 14))
label.pack(pady=10)

# File select and save buttons
file_button = tk.Button(root, text="选择初始地图", width=12, command=select_fileMap)
file_button.pack(pady=10)

# File select and save buttons
file_button = tk.Button(root, text="选择目标图片", width=12, command=select_file)
file_button.pack(pady=10)

save_button = tk.Button(root, text="生成地图", width=12, command=save_image, state="disabled")
save_button.pack(pady=5)

# Label for file info
file_label_var = tk.StringVar(value="No file selected")
file_label = tk.Label(root, textvariable=file_label_var, wraplength=450, fg="gray")
file_label.pack(pady=5)

# Run the app
root.mainloop()
