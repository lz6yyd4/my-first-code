import numpy as np
# 样本：x数据
x = np.array([1,2,3,4,5])
# 真实标签y
y = np.array([2.2, 2.9, 4.1, 4.9, 6.2])

# 构造矩阵X：第一列全1（截距w0），第二列是x（w1）
X = np.stack([np.ones(len(x)), x], axis=1)
print("X矩阵：")
print(X)

# 伪逆求解权重
X_pinv = np.linalg.pinv(X)
w = X_pinv @ y
print("\n求得权重 [w0, w1] = ", w)
print(f"拟合直线 y = {w[0]:.2f} + {w[1]:.2f} * x")

# 预测
y_pred = X @ w
print("预测值：", y_pred)

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 1.8, 3.3, 4.1, 4.9])
X = np.stack([np.ones(len(x)),x],axis=1)
print(x)
X_pinv = np.linalg.pinv(X)
w = X_pinv @ y
print(w)
print(f"y = {w[0]:.2f} + {w[1]:.2f} * x")
y_pred = X @ w
print(y_pred)