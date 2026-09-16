# 与c++不同的是，python不需要显示给出数据类型，即弱类型语言（对语言类型不敏感）

a = 1.0

# python不需要显示规定main函数

print(a)
print(type(a))

c = a + 1
print(c)

# c++的运算手段更多

print(2**6) #求幂过程
print(5//3)
print(5%3)

a = 'str'
b = "str"
print(a+b+"SJTU")

# python的bool

a = False
print(a)

# 更复杂的运算

a = 1
print(a >= 0.5)

b = a > 0 and a < 1
b = not b
print(b)

# 怎么写注释
"""
build-in Data structure
"""

# 特有的数据结构list
a = [1,2]
a.append(0.3)
print(a)
print(type(a[0]))
a.pop(1) #stack的数据结构功能实现
print(a)
print(len(a))

print(a[-1])
print(a[-2])

# advanced list
lst = [1,2,3,4,5,6,7,8]
print(lst[0:2]) # slice
print(lst[0:-1:2])

# Dict
my_dict = {'bob':18,'alice':19} #键值对
print(my_dict['bob'])

my_dict['tom'] = 20
print(my_dict['tom'])

print(my_dict)

my_dict['tom'] = 12
print(my_dict['tom'])
















