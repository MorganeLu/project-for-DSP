import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from DFT import dft

# 生成已知数据点集 (x,y)，需插值的数据点集 xnew
x = np.linspace(0, 2048, 2048)  # 生成已知数据点集的 x
dataFile_100 = 'dataset/100-2-3.mat'
data_100 = scio.loadmat(dataFile_100)
Y_100 = data_100['y']
y = Y_100.squeeze()
xnew = np.linspace(0, 2048, 2048*2)  # 需插值的数据点集


f5 = interp1d(x, y, kind="cubic")  # 三次样条插值
print(f5(1))

Y_100=f5

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

length = 2048
T = 1 #fs
N = 200
Y_100_2 = []
for i in range(0,length,T):
    Y_100_2.append(Y_100[i])

# 原信号
plt.subplot(221)
plt.title("原信号")
# plt.plot(range(0,len(Y_100_2)), Y_100_2)
plt.plot(range(0, len(Y_100), T), Y_100_2)

# 频谱
DFT = dft(N, Y_100_2)
DFT.Xk()
plt.subplot(222)
plt.title("频谱")
plt.plot(DFT.K, DFT.xk)

# 幅度谱
plt.subplot(223)
plt.title("幅度谱")
plt.stem(DFT.K, np.abs(DFT.xk))

# 相位谱
plt.subplot(224)
plt.title("相位谱")
angle_ = np.angle(DFT.xk)
plt.stem(DFT.K, 180 * angle_ / np.pi)

plt.show()
