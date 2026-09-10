'''import pandas as pd

s = pd.Series([88, 92, 76, 85], index=["小明","小红","小李","小张"])
print(s)
print(s["小红"]) # 通过索引取值

data = {
    "姓名":["小明","小红","小李"],
    "年龄":[19,18,19],
    "分数":[88,92,76]
}
df = pd.DataFrame(data)
print(df)

print(df.head(2))     # 看前2行，默认head()看前5行
print(df.info())      # 查看类型、有没有缺失值
print(df.describe())  # 数值列：均值、最大最小、标准差（数据探查必用）
print(df.columns)     # 获取所有列名
print(df.shape)       # (行数,列数) 和numpy的shape很像

# 取单列
print(df["姓名"])
# 取多列，传列表
print(df[["姓名","分数"]])

# iloc：数字位置索引（和numpy一样，从0开始）
print(df.iloc[0])        # 第0行全部
print(df.iloc[0:2, [0,2]]) # 前两行，第0、2列

# loc：按行标签名取（按索引名字）
print(df.loc[0, "分数"])

# 筛选分数>80的学生
mask = df["分数"] > 80
res = df[mask]
print(res)

# 写入csv
df.to_csv("student_score.csv", index=False, encoding="utf-8-sig")
# index=False 不把pandas自动行号保存进文件

# 读取csv
df_read = pd.read_csv("student_score.csv", encoding="utf-8-sig")
print(df_read)

df["等级"] = ["良好","优秀","良好"]
print(df)
'''
import pandas as pd
date = {"姓名":["小明","小红","小刚","小丽"],"年龄":[19,18,20,19],"成绩":[85,93,78,89]}
df = pd.DataFrame(date)
print(df)
print(df.shape)
print(df.head(3))
print(df.describe())
print(df.columns)
print(df["成绩"])
print(df[["姓名","成绩"]])
print(df.iloc[[0,2]])
mask = df["成绩"] >80
print(df[mask])
df["pass"] = df["成绩"].apply(lambda x: "及格" if x >= 60 else "不及格")
print(df)
df.to_csv("student.csv",index=False,encoding="utf-8-sig")
df_read = pd.read_csv("student.csv",encoding="utf-8-sig")
print(df_read)
mask2 = (df_read["成绩"] > 85) & (df_read["年龄"] == 19)
print(df_read[mask2])