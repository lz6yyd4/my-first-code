import numpy as np

arr1 = np.array([1,2,3,4,5])
print("arr1数组:",arr1)
print("arr1数组shape:",arr1.shape)

my_list = [1,2,3,4,5]
arr2 = np.array(my_list)
print("arr2:",arr2)

arr3 = np.array([0,1,2,3,4,5,6,7,8,9])
print("arr3 arange0-9:",arr3)

arr4 = np.array([[1,2,3],[4,5,6]])
print("二维矩阵arr4：")
print(arr4)
print("arr4的形状(行,列):",arr4.shape)

arr5 = np.array([1,2,3])
print("数组每个元素+2：", arr5 + 2)
print("数组每个元素*3：", arr5 * 3)