import tkinter as tk
import json
import os
from constants import limbs

# JSONファイルのディレクトリパスを指定
directory = "./kabeposter"

# Tkinterウィンドウの作成
window = tk.Tk()
canvas = tk.Canvas(window, width=1800, height=1800)
canvas.pack()

# ファイルのリストを取得
file_list = os.listdir(directory)  # 指定されたディレクトリ内のファイルのリストを取得
file_index = 0  # ファイルリスト内の現在のインデックスを示すための変数の設定

def draw_skeleton():
    global file_index

    if file_index >= len(file_list):  # 最後のファイルまで処理が完了した場合
        return  # 描画を終了する

    # directoryとfile_list[file_index]を結合して現在のファイルパスを取得
    file_path = os.path.join(directory, file_list[file_index])

    # ファイルをテキストモードで開き、JSONファイルの読み込み
    with open(file_path, "r") as f:
        data = json.load(f)

    if "people" not in data or not data["people"]:
        # 人物の関節情報が存在しない場合
        file_index += 1
        return

    # 読み込んだJSONデータから、人物の関節座標の取得
    keypoints_1 = data["people"][0]["pose_keypoints_2d"]
    keypoints_2 = data["people"][1]["pose_keypoints_2d"]

    # キャンバスのクリア
    canvas.delete("all")

    # 関節の描画
    for i in range(len(limbs)):
        limb = limbs[i]
        joint_1 = limb[0]
        joint_2 = limb[1]

        x1 = int(keypoints_1[joint_1 * 3])
        y1 = int(keypoints_1[joint_1 * 3 + 1])
        x2 = int(keypoints_1[joint_2 * 3])
        y2 = int(keypoints_1[joint_2 * 3 + 1])

        if x1 == 0 or y1 == 0 or x2 == 0 or y2 == 0:
            continue

        canvas.create_line(x1, y1, x2, y2, width=3)
        
    # 関節の描画
    for i in range(len(limbs)):
        limb = limbs[i]
        joint_1 = limb[0]
        joint_2 = limb[1]

        x1 = int(keypoints_2[joint_1 * 3])
        y1 = int(keypoints_2[joint_1 * 3 + 1])
        x2 = int(keypoints_2[joint_2 * 3])
        y2 = int(keypoints_2[joint_2 * 3 + 1])

        if x1 == 0 or y1 == 0 or x2 == 0 or y2 == 0:
            continue

        canvas.create_line(x1, y1, x2, y2, width=3)

    file_index += 1  # 次のファイルへ移動

    # 100ミリ秒ごとに描画を更新
    window.after(100, draw_skeleton)

# 描画の開始
draw_skeleton()

# Tkinterウィンドウの更新
window.mainloop()

