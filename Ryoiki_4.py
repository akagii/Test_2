from logging import captureWarnings
import tkinter as tk
from turtle import width

root = tk.Tk()
root.geometry("400x400")

# Canvasの作成
canvas = tk.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tk.BOTH, expand=True)

# 胴
dou = canvas.create_line(200, 100, 200, 200, width=3)

# 腕

ude_1 = canvas.create_line(200, 150, 130, 120, width=3)
ude_2 = canvas.create_line(200, 150, 270, 120, width=3)

# 足

asi_1 = canvas.create_line(200, 200, 260, 260, width=3)
asi_2 = canvas.create_line(200, 200, 140, 260, width=3)

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
root.mainloop()  # 表示