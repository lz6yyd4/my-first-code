#======if else语句 for while循环======
name = str("mu")
age = int(19)
height = float(1.77)
print("我是", name, "今年", age, "岁", "身高", height, "米")

number1 = 50
if number1 >= 70:
    print("及格")
else:
    print("不及格")

number2 = int(input("输入数字"))
print("偶数") if number2 % 2 == 0 else print("奇数")
99
for i in range(11):
    print(i,end=" ")

for h in range(0,11,2):
    print(h,end=" ")

a = 1
while a < 11:
    print(a,end=" ")
    a += 1

for j in range(1,51):
     if j % 7 == 0:
        print(j,end=" ")

b = int(input("输入成绩"))
if b >= 90:
    print("A")
elif b >= 80:
    print("B")
elif b >= 70:
    print("C")
elif b >= 60:
    print("D")
elif 60 > b >= 0:
    print("E")
else:
    print("成绩非法")

sum = 0
for f in range(1,101):
    sum += f
print(sum)

ans = 7
while True:
    guess = int(input("猜数字"))
    if guess == ans:
        print("猜对了")
        break#break跳出整个循环 continue跳出本次循环
    elif guess < ans:
        print("小了")
    elif guess > ans:
        print("大了")
    else:
        print("输入的什么玩意")

#list列表 tuple元组 dict字典 set集合
# 第1题
# 创建列表 nums = [1,2,3,4,5]
# 打印整个列表；打印第1个元素；修改第3个元素为99；追加元素6
nums = [1,2,3,4,5]
print(nums)
print(nums[0])
nums[2] = 99
nums.append(6)
print(nums)

# 第2题
# 元组 t = (10,20,30)
# 打印元组；尝试理解：元组不能 t[0]=99 修改（写代码会报错，可以注释掉）
t = (10,20,30)
print(t)
# t[0] = 99  # 取消注释运行会报错，元组不可修改

# 第3题
# 字典 student = {"name":"小明", "age":19, "major":"计算机"}
# 打印name；修改age为20；新增键值对 "score":90
student = {"name":"小明", "age":19, "major":"计算机"}
print(student["name"])
student["age"] = 20
student["score"] = 90
print(student)

# 第4题
# 取出列表nums = [2,4,6,8,10] 的前3个元素（切片）
nums = [2,4,6,8,10]
print(nums[0:3])

# 第5题
# 遍历列表，逐个打印里面的每一项
lst = ["苹果","香蕉","橙子"]
for fruit in lst:
    print(fruit)

# 第6题
# 遍历字典，打印所有key和value
info = {"a":1, "b":2, "c":3}#.keys()返回字典所有的键, .values()只拿所有值
for k, v in info.items():#.items()把字典里每一对 key 和 value打包成 (键, 值) 的元组
    print(k, v)

# 第7题
# 列表内置方法：remove 删除元素 4
data = [1,3,4,5,7]
data.remove(4)
print(data)

# 第8题
# 列表推导式：生成 [1,4,9,16,25]（1~5每个数平方）
res = [i*i for i in range(1,6)]
print(res)

# 第9题
# 判断 "橙子" 是否在列表里，存在打印存在，否则不存在
fruits = ["苹果","葡萄","芒果"]
if "橙子" in fruits:
    print("存在")
else:
    print("不存在")

# 第10题
# 嵌套结构：people = [{"name":"A","age":18}, {"name":"B","age":20}]
# 取出B的年龄
people = [{"name":"A","age":18}, {"name":"B","age":20}]
print(people[1]["age"])
