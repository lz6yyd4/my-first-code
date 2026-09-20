import numpy as np

# 激活函数定义
def sigmoid(z):
    return 1/(1+np.exp(-z))#np.exp(x) 是 NumPy 里的指数函数，等价于数学里：exp(x)==e**x

def relu(z):
    return np.maximum(0, z)

# 单个神经元
x = np.array([1.2, 3.1])  # 输入特征
w = np.array([0.5, -0.3]) # 权重
b = 0.2                   # 偏置

z = np.dot(w, x) + b
a = relu(z)
print(f"加权求和 z = {z:.2f}")
print(f"神经元输出 a = {a:.2f}")
