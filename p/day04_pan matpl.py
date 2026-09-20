import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams ["font.family"] = ["SimHei"]
plt.rcParams ["axes.unicode_minus"] = False

date = {"姓名":["小明","小红","小刚","小丽"],
        "年龄":[19,18,20,19],
        "成绩":[85,93,78,89]}
df = pd.DataFrame(date)
'''
# 柱状图
plt.bar(df["姓名"], df["成绩"]) # x轴：姓名，y轴：成绩
plt.title("学生成绩柱状图")    # 图标题
plt.xlabel("学生姓名")         # X轴标签
plt.ylabel("分数")             # Y轴标签
plt.ylim(0,100)                # y轴范围0~100
plt.show()                     # 显示图片

#折线图
plt.plot(df["姓名"], df["成绩"], marker='o', color='orange')
plt.title("成绩折线图")
plt.xlabel("学生姓名")
plt.ylabel("分数")
plt.ylim(70,100)
plt.grid(True) # 显示网格线
plt.show()

#直方图 Histogram
plt.hist(df["成绩"], bins=2, edgecolor="black")
plt.title("成绩分布直方图")
plt.xlabel("分数区间")
plt.ylabel("人数")
plt.show()

#散点图
plt.scatter(df["年龄"], df["成绩"], s=100, c='red')
plt.title("年龄-成绩散点图")
plt.xlabel("年龄")
plt.ylabel("成绩")
plt.show()
'''
data = {
    "姓名":["小明","小红","小刚","小丽"],
    "年龄":[19,18,20,19],
    "成绩":[85,93,78,89]
}
df = pd.DataFrame(data)

# 创建画布，2行2列子图
plt.figure(figsize=(10,8)) # 设置画布大小 宽10，高8

# 子图1：柱状图
plt.subplot(2,2,1)
plt.bar(df["姓名"], df["成绩"],color='skyblue')
plt.title("柱状图：学生成绩")
plt.ylim(0,100)

# 子图2：折线图
plt.subplot(2,2,2)
plt.plot(df["姓名"], df["成绩"], marker='o',c='black')
plt.title("折线图：学生成绩")

# 子图3：直方图
plt.subplot(2,2,3)
plt.hist(df["成绩"], bins=4, edgecolor="pink",color='red')
plt.title("直方图：成绩分布")

# 子图4：散点图
plt.subplot(2,2,4)
plt.scatter(df["年龄"], df["成绩"],s=100,c='green')
plt.title("散点图：年龄vs成绩")

plt.tight_layout() # 自动调整子图间距，防止文字重叠
plt.show()

