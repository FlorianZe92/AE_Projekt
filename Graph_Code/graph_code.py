import matplotlib.pyplot as plt
import pandas as pd

#Output wird eingelesen und anschließend graphisch dargestellt.
data_x = pd.read_csv('x.csv', header = None, sep = '\t')
data_y = pd.read_csv('y.csv', header = None, sep = '\t')

plt.plot(data_x,data_y,'bs')
plt.xlim((-5, 105))
plt.ylim((-5, 105))
plt.tight_layout()
plt.show()
