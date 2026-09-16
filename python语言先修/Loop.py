# python 没有语句块
# 通过SPACE缩进控制语句快

my_data = 1.0

# if else switch

if my_data < 2.0:
    print('my_data is less than 2.0')
elif my_data <3.0:
    print('my_data is less than 3.0')

# else:
   # print('my_data is less than 2.0')

a = 12 if my_data < 1 else 2
print(a)

# --- Loop
index = 0
new_list = [1,2,3,4,5]

while index < 3:
    new_list[index] *= 2
    index += 1
print(new_list)

for index in range(0,3):
 print(index)

for c in new_list[0:5:2]:
 print(c)





