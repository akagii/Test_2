import json

from logging import captureWarnings
import tkinter as tk
from turtle import width

root = tk.Tk()
root.geometry("1500x1000")

# Canvasの作成
canvas = tk.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tk.BOTH, expand=True)

json_file = open('kabeposter/kabeposter_000000000000_keypoints.json', "r")

load = json.load(json_file)

pose_a = load["people"][0]["pose_keypoints_2d"]
pose_b = load["people"][1]["pose_keypoints_2d"]

print(pose_a[6], pose_a[7], pose_a[8], pose_a[15], pose_a[16], pose_a[17])
print(pose_b[6], pose_b[7], pose_b[8], pose_b[15], pose_b[16], pose_b[17])

kata_1 = canvas.create_line(
    pose_a[6], pose_a[7], pose_a[15], pose_a[16], width=3)
kata_2 = canvas.create_line(
    pose_b[6], pose_b[7], pose_b[15], pose_b[16], width=3)
root.mainloop()  # 表示