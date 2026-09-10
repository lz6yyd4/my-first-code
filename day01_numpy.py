import numpy as np#导入numpy函数

arr1 = np.array([1,2,3,4,5])#创建数组
print("arr1数组:",arr1)
print("arr1数组shape:",arr1.shape)#获取数组尺寸

my_list = [1,2,3,4,5]
arr2 = np.array(my_list)
print("arr2:",arr2)
#arr[start:end:step]

arr3 = np.arange(1,10)
print(arr3)

arr4 = np.array([[1,2,3],[4,5,6]])
print("二维矩阵arr4：")
print(arr4)
print("arr4的形状(行,列):",arr4.shape)

arr5 = np.array([1,2,3])
print("数组每个元素+2：", arr5 + 2)
print("数组每个元素*3：", arr5 * 3)

zer = np.zeros((3,3))#创建全零三行三列的数列
zer.astype(int)#转换数据类型
print(zer[:,1])#全部行，只取第一列
print(zer[:1])#取第一行
print(zer[1,2])#第一行第二列的元素
print(zer[:2])#前两行

lin = np.linspace(0,1,5)#创建区间零到一等间距分布的五个数
print(lin)

rad = np.random.rand(3,4)#创建三行四列的随机数组
print(f"rad:\n{rad}")

rad2 = np.random.randint(0,10,size=(3,4),dtype=int)#(最小值,最大值，size=(行,列),dtype=数据类型)
print(f"rad2:\n{rad2}")

#========数学运算=========
res = np.dot([1,2,3],[4,5,6])#.dot点成运算
print("res:",res)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = A.dot(B)
print(C)
print(A @ B)#@矩阵乘法
D = np.matmul(A,B)#矩阵乘法
print(D)

arr6 = np.array([1,2,3])
sq = np.sqrt(arr6)#求平方根
print(sq)
s = np.sin(arr6)#求正弦
c = np.cos(arr6)#求余弦
print(s,c)
l = np.log(arr6)#求对数
p = np.power(arr6,2)#求指数
print(l,p)
print(arr6.min())
print(arr6.max())
print(arr6.argmin())
print(arr6.argmax())
#  .sum()求和   .mean() .median()返回平均值 .var()方差 .std()标准差

arr7 = np.array([[2,5],[1,4]])
print(np.sum(arr7,axis=0))#axis参数决定维度0纵向 1横向
print(np.sum(arr7,axis=1))

# 广播示例1：数组 + 标量
a = np.array([1,2,3])
b = 2
print("例1 数组+标量：")
print(a + b)

# 广播示例2：二维数组 + 一维数组
A = np.array([[1,2,3],
              [4,5,6]])
B = np.array([10,20,30])
print("\n例2 二维+一维：")
print(A + B)

# 广播示例3 (3,1) + (2,)
arr1 = np.array([[1],[2],[3]]) # shape (3,1)
arr2 = np.array([10,20])       # shape (2,)
res = arr1 + arr2
print("\n例3 (3,1)+(2,)")
print(res)
print("结果形状：", res.shape)

arr = np.arange(12)
arr1 = arr.reshape(3,4)#.reshape()函数将数组重新排列成指定的形状
arr2 = arr.reshape(-1,4)#-1表示自动计算行数
print(arr1)
print(arr2)

arr2.flatten()#将多维数组降为一维数组 返回全新数组
print(arr2.flatten())
arr2.ravel()#将多维数组降为一维数组，返回的是视图
print(arr2.ravel())

arr3 = arr2.T#转置 等价于arr3 = np.transpose(arr2)
print(arr3)

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

v_stack = np.vstack([arr1,arr2]) # 上下合并
h_stack = np.hstack([arr1,arr2]) # 左右合并
print("垂直堆叠：")
print(v_stack)
print("水平堆叠：")
print(h_stack)
d_stack = np.dstack([arr1,arr2]) # 深度合并
print("深度堆叠：") 
print(d_stack)
print("深度堆叠形状：", d_stack.shape) # (2, 2, 2)

arr1 = np.ones((2,3))
arr2 = np.ones((2,3))
print(np.vstack([arr1,arr2]).shape)
print(np.hstack([arr1,arr2]).shape)
print(np.dstack([arr1,arr2]).shape)

arr = np.array([1,33,24,2,53,3,63])
mask = arr > 10
print(mask)
res = arr[mask]
print(res)

nums = np.array([10,20,30,40,50,60])
a1,a2,a3 = np.split(nums,3)
print(f"a1: {a1}")
print(f"a2: {a2}")
print(f"a3: {a3}")