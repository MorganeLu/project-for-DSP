import math

class dft():
    def __init__(self, Num, data):
        '''
        :param Num: dft点数,即离散取样点数
        '''
        super().__init__()
        self.Num = Num
        self.data = data
        self.xk = []  # 存放dft计算结果
        self.K = list(range(0, self.Num, 1))  # 时域序列横坐标，采样

    def Xk(self):
        # 计算频域中的频率自变量值
        W = []
        for x in self.K:
            W.append(x * 2 * math.pi / len(self.K))
        ## 遍历频率自变量
        for f in W:
            p = 0
            # 遍历时间序列，得到累加和
            for k in self.K:
                p = self.data[k] * math.e ** (-1j * f * k) + p
            self.xk.append(p)  # 对应每一个自变量频率的因变量值


if __name__ == '__main__':
    import numpy as np
    import scipy.io as scio
    from matplotlib import pyplot as plt

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    length = 2048
    dataFile_100 = 'dataset/100-2-3.mat'
    data_100 = scio.loadmat(dataFile_100)
    Y_100 = data_100['y']

    T = 1 #fs
    N = 200
    Y_100_2 = []
    for i in range(0,length,T):
        Y_100_2.append(Y_100[i])

    # 原信号
    plt.subplot(221)
    plt.title("原信号")
    plt.plot(range(0,len(Y_100_2)), Y_100_2)
    # plt.plot(range(0, len(Y_100), T), Y_100_2)

    # 频谱
    DFT = dft(N, Y_100_2)
    DFT.Xk()
    plt.subplot(222)
    plt.title("频谱")
    plt.plot(DFT.K, DFT.xk)
    A=np.array(DFT.xk)
    # plt.plot(range(0, len(Y_100), T), DFT.xk)

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