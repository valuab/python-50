## 输出 100 - 1000 区间的水仙花数
# 取百位数
# 取十位数
# 取个位数
for x in range(100,1000):
    hundred = x // 100
    ten = x % 100 // 10
    unit = x % 100 % 10
    if x == hundred ** 3 + ten ** 3 + unit ** 3:
        print(x ,hundred,ten,unit)

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num,low,mid,high,num // 10)

# 整数倒序  123456789 => 987654321
# 思路 利用取余，取最后一位，原有值向前十倍递增
print(num)
# 这里重新赋值
num = int(input('num = '))
reversed_num = 0
count = 0
while num > 0:
    count += 1
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
    print(reversed_num,num)
print(reversed_num,count,10 % 10)

#### 例子：百钱百鸡问题。
"""
百钱百鸡是我国古代数学家[张丘建](https://baike.baidu.com/item/%E5%BC%A0%E4%B8%98%E5%BB%BA/10246238)在《算经》一书中提出的数学问题：鸡翁一值钱五，
鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""

# 这里重新设置
# 设 x 为鸡翁的数目
for x in range(0,21):
    # 设 y 为 鸡母的数量
    for y in range(0,34):
        if 5 * x + 3 * y + (100 - x - y) / 3 == 100:
           print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {100 - x -y}只')
# 答案 
# 使用穷举法
"""
0 25 75
4 18 78
8 11 81
12 4 84
"""

# 经典 斐波拉契数  => 前两个数之和为后一个数 起始值为 1 1
# 输入一个正整数，输出这个数范围内的斐波拉契数
num = int(input('请输入要计算的范围：'))
a , b = 1 , 1
print(a,b)
while a + b < num:
    print(a+b)
    a = a + b
    b = a

# #### 例子：CRAPS赌博游戏。
"""
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
"""

# 使用随机模块
import random
user = True
father = True
count = 0
while user and father:
    num = random.randint(0,13) #摇色子结果
    count += 1
    if count == 1 :
        first = num
        if first == 7 or first == 11:
            father = False
        elif first == 2 or first == 3 or first == 12:
            user = False
    else:
        if num == 7 :
            user = False
        elif num == first:
            father = False
print()


# 例子5：打印素数。
"""
**说明**：素数指的是只能被1和自身整除的正整数（不包括1）。
"""

max = int(input('输入最大范围，输出素数：'))

for x in range(2,max):
    is_false = True
    for y in range(2,x):
        if x % y == 0:
            is_false = False
            break
    if is_false:
        print(x)

