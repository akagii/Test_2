from cgitb import text
import glob
import os

total_1 = 0
total_3 = 0
total_5 = 0
total_7 = 0
total_9 = 0

total = 0

for f in glob.glob('./OneDrive/学校/領域実習/ryoiki/sample/kitamura_*1_kgu.txt'):
    with open(os.path.join(os.getcwd(), f), 'r') as p:
        text = p.read()

        try:
            num = int(text)
        except ValueError as e:
            continue
        total_1 += num

for f in glob.glob('./OneDrive/学校/領域実習/ryoiki/sample/kitamura_*3_kgu.txt'):
    with open(os.path.join(os.getcwd(), f), 'r') as p:
        text = p.read()

        try:
            num = int(text)
        except ValueError as e:
            continue
        total_3 += num

for f in glob.glob('./OneDrive/学校/領域実習/ryoiki/sample/kitamura_*5_kgu.txt'):
    with open(os.path.join(os.getcwd(), f), 'r') as p:
        text = p.read()

        try:
            num = int(text)
        except ValueError as e:
            continue
        total_5 += num

for f in glob.glob('./OneDrive/学校/領域実習/ryoiki/sample/kitamura_*7_kgu.txt'):
    with open(os.path.join(os.getcwd(), f), 'r') as p:
        text = p.read()

        try:
            num = int(text)
        except ValueError as e:
            continue
        total_7 += num

for f in glob.glob('./OneDrive/学校/領域実習/ryoiki/sample/kitamura_*9_kgu.txt'):
    with open(os.path.join(os.getcwd(), f), 'r') as p:
        text = p.read()

        try:
            num = int(text)
        except ValueError as e:
            continue
        total_9 += num

total = total_1 + total_3 + total_5 + total_7 + total_9

print(total)