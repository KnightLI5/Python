import numpy as np

data = np.load(r'C:\Users\asus\Documents\Tencent Files\1419450900\FileRecv\TRAIN1500.npy', allow_pickle=True).item()
num = data[0]
print(type(num))
# for i in range(len(data)):
#     print('第' + str(i) + '个矩阵')
#     print(data[i])

