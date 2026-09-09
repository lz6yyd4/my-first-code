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
        break
    elif guess < ans:
        print("小了")
    elif guess > ans:
        print("大了")
    else:
        print("输入的什么玩意")