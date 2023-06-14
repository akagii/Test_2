import json  # jsonモジュールをインポートする

with open('./OneDrive/学校/領域実習/catalog.json', 'r') as f:
    load = json.load(f)  # 開いたファイル(json_open)をjson.load関数でJSONにする

total = 0
max = 0
min = 1000000

for a in load:
    # for文は for 変数 in イテラブル: の形で書く (イテラブルとはfor文で繰り返し可能なオブジェクトのこと)

    if a['name'] == "jacket":
        total += 1

        if a['price'] > max:
            max = a['price']

        if a['price'] < min:
            min = a['price']


print(total, max, min)