import random
import time

rabbitX = 0 #現在のマス目
tortoiseX = 0
goal = 117 #ゴールのマス目
qwertyuiop = 0


def put():
    print()
    print(">" * qwertyuiop + "熊" + ">" * (goal - qwertyuiop))
    print(">" * qwertyuiop + "始祖鳥" + ">" * (goal - 4 - qwertyuiop))
    print(">" * qwertyuiop + "イグアノドン" + ">" * (goal - 10 - qwertyuiop))
    print(">" * qwertyuiop + "針葉樹林" + ">" * (goal - 6 - qwertyuiop))
    print(">" * rabbitX + "兎" + ">" * (goal - rabbitX))
    print(">" * tortoiseX + "亀" + ">" * (goal - tortoiseX))
print("動物レース開催!")
a = input("誰が勝つか予想しよう!!\n1. 熊\n2. 始祖鳥\n3. イグアノドン\n4. 針葉樹林\n")
while not (a == "1" or a == "2" or a == "3" or a == "4" or a == "熊" or a == "始祖鳥" or a == "イグアノドン" or a == "針葉樹林") :
    a = input("誰が勝つか予想しよう!!\n1. 熊\n2. 始祖鳥\n3. イグアノドン\n4. 針葉樹林\n")
m = input("お金を賭けよう!!(単位: 百万ドル)\n")
print(("=" * 118 + "\n") * 20)
put()
print("3...")
time.sleep(0.7)
print("2...")
time.sleep(0.7)
print("1...")
time.sleep(0.7)
print("GO!!")
time.sleep(0.4)
while True:
    rabbitX += random.randint(1, 6)
    if rabbitX >= goal:
        rabbitX = goal
        put()
        print("\n1. 兎\n2. 亀\n3. 熊, 始祖鳥, イグアノドン, 針葉樹林")
        print(m + ",000,000$失った...")
        break
    tortoiseX += random.randint(1, 6)
    if tortoiseX >= goal:
        tortoiseX = goal
        put()
        print("\n1. 亀\n2. 兎\n3. 熊, 始祖鳥, イグアノドン, 針葉樹林")
        print(m + ",000,000$失った...")
        break
    qwertyuiop += 1
    put()
    time.sleep(0.1)

print("enddddddddddddddd")