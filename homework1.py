import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体，避免中文显示为方框
plt.rcParams['font.sans-serif'] = ['SimHei']

# 定义高斯分布参数
mu = 0      # 均值
sigma = 1   # 标准差

# 生成 x 数据
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# 计算高斯分布概率密度函数
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# 绘制高斯分布曲线
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f'μ={mu}, σ={sigma}', color='blue')

# 添加标题和标签
plt.title('高斯分布曲线')
plt.xlabel('x')
plt.ylabel('概率密度')
plt.grid(True)
plt.legend()

# 显示图形
plt.show()
