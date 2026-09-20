#======def======
def my_max(a,b):
    if a>b:
        return a
    else:
        return b
print(my_max(9,15))

def calc_area(r):
    area = 3.14*r*r
    return area
print(calc_area(5))

def show_info(name,age):
    return f"我叫{name},今年{age}岁"
print(show_info("小明",18))

def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count
print(count_even([1,2,3,4,5,6,7,8]))

def introduce(name, hobby="编程"):
    return f"我叫{name},我的爱好是{hobby}"
print(introduce("小明"))

def multiply(*num):
    result = 1
    for n in num:
        result *= n
    return result
print(multiply(2,3,4))

a = 10
def func():
    a = 20
    print("函数内a=",a)

func()
print("函数外a=",a)

def get_avg_score(score_list):
    total = sum(score_list)
    avg = total / len(score_list)
    return avg
scores = [85, 90, 78, 92, 88]
print("平均分:", get_avg_score(scores))

def join_name(first,last):
    return f"{first}{last}"
print(join_name("张","三"))


with open("test.txt","w",encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("今天天气不错。\n")

with open("test.txt","a",encoding="utf-8") as f:
    f.write("这是追加的内容。\n")

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

try:
    # 可能会报错的代码
    num = 10 / 0
except ZeroDivisionError:
    print("错误：不能除以0")
except Exception as e:
    print("发生未知错误：", e)
else:
    # 没有异常才执行
    print("代码正常运行")
finally:
    # 无论有没有报错，一定会执行
    print("程序结束")

try:
    open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("错误：文件不存在")

