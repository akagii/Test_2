total = 0

with open('./OneDrive/学校/領域実習/data.txt', 'r') as a:  # ファイルを開く
    for line in a.readlines():  # ファイルから一行読み出す
        try: #例題が発生しても終了せずに処理を継続
            num = int(line)  # 行を整数に変換する
        except ValueError as e:
            continue #ループの先頭に戻ってやり直す
        total += num  #整数の値を足していく
print(total)  #出力