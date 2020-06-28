## 循环即遍历执行
# for in 循环
first = 0
for i in range(1,51):
    first += i
print(first) # 即为区间 1 ~ 50 内值相加 range() 类似于数学中集合
print(i,'str') # 循环定义的变量外部也能访问

# 经典乘法口诀表
for x in range(1,10):
    for y in range(1,x + 1):
        print(f'{x}*{y}={x * y}', end='\t')
    print()

# while 循环
import random # 引入随机函数 c 语言模块

"""
random.randint 随机整数 (0,3)
random.random 随机实数 (0,3)
random.randrange 随机数 (0,3)
random.choice() 随机字符 'str'
random.sample()，多个字符中选取特定数量的字符
random.uniform()，随机浮点数
random.shuffle（传入参数），洗牌功能
"""
num = random.randint(1, 10)
count = 0
while True:
    count += 1
    number = int(input('请输入：'))
    if number < num:
        print('请大一点')
    elif  number > num:
        print('请小一点')
    else:
        print('猜对了')
        break
