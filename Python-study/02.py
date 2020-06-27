"""
1. int 整型 即整数 包括二进制 （如`0b100`，换算成十进制是4）、八进制（如`0o100`，换算成十进制是64）、十进制（`100`）和十六进制（`0x100`，换算成十进制是256）的表示法。
输出 <class 'int'>

2.浮点型 包含带小数
<class 'float'>

3.字符串类型
<class 'str'>

4.布尔型
true and false
<class 'bool'>
"""
num = 6
print(type(num))

flo = 6.6
print(type(flo))

string = 'hello world'
print(type(string))

fou = False
print(type(fou))


"""
类型转换
int() 转换成整型  将一个数值或字符串转换成整数
float() 字符串转换为浮点数
str() 将指定的对象转换成字符串形式，可以指定编码
chr() 将整数转换成该编码对应的字符串（一个字符）。
ord() 与 chr() 相反 将字符转成整数 (Python中字符和字符串表示法相同)
"""
print(int(flo))
# print(int(string)) #invalid literal for int() with base 10: 'hello world'
print(int(fou)) # False 转为整型为0，True 为 1

print(float(num)) #6.0
# print(float(string)) #ValueError: could not convert string to float: 'hello world'
print(float(fou)) # 0.0
print(float(True)) # 1.0

print(type(str(num))) #6 #<class 'str'>
print(type(str(flo))) #6.6 #<class 'str'>
print(type(str(fou))) #False #<class 'str'>
print(type(str(True))) #True #<class 'str'>


print(chr(num)) # =
print(ord(chr(num))) # 6