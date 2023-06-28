import tkinter as tk
from turtle import width

root = tk.Tk()
root.geometry("400x400")

# Canvasの作成
canvas = tk.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tk.BOTH, expand=True)

# 線の描画

# 胴
dou = canvas.create_line(200, 100, 200, 200, width=3)

# 腕

ude_1 = canvas.create_line(200, 150, 130, 120, width=3)
ude_2 = canvas.create_line(200, 150, 270, 120, width=3)

# 足

asi_1 = canvas.create_line(200, 200, 260, 260, width=3)
asi_2 = canvas.create_line(200, 200, 140, 260, width=3)

# 円の描画

# 頭

atama = canvas.create_oval(160, 30, 240, 100, width=3)

# 目

me_1 = canvas.create_oval(180, 50, 180, 60, width=3)
me_2 = canvas.create_oval(215, 50, 215, 60, width=3)

# 口

kuti = canvas.create_arc(165, 35, 235, 90, start=225, style=tk.CHORD, width=3)

# 帽子

cap = canvas.create_polygon(250, 10, 260, 45, 130, 45, fill="red")

canvas.lift(kuti, atama)
canvas.lift(me_1, atama)
canvas.lift(me_2, atama)


def move():  # 移動する関数
    canvas.move(dou, 2, 0)  # 1ずつ移動
    canvas.move(ude_1, 2, 0)  # 1ずつ移動
    canvas.move(ude_2, 2, 0)  # 1ずつ移動
    canvas.move(asi_1, 2, 0)  # 1ずつ移動
    canvas.move(asi_2, 2, 0)  # 1ずつ移動
    canvas.move(atama, 2, 0)  # 1ずつ移動
    canvas.move(me_1, 2, 0)  # 1ずつ移動
    canvas.move(me_2, 2, 0)  # 1ずつ移動
    canvas.move(kuti, 2, 0)  # 1ずつ移動
    canvas.move(cap, 2, 0)  # 1ずつ移動

    canvas.after(100, move)  # 100ミリ秒ごとに移動させる


move()

root.mainloop()  # 表示