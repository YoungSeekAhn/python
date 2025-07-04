# File: python_test1.py
## This is a example of a Python code using Numpy and Matplotlib
# It generates a sine wave and plots it using Matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# 한글 폰트 설정 (예: Windows의 'Malgun Gothic')
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# Numpy를 이용한 데이터 생성
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='sin(x)')
plt.title('Numpy와 matplotlib 예제')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()