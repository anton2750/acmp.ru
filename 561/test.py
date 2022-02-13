from math import log
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

t = np.linspace(1, 100)
# s = np.log(2 * t)
# s1 = np.log(99 * t)
# s2 = np.log(99 * np.log(2, t))
# s2 = np.log(t)
# s3 = np.log(t) * (5 * log(2))
# s4 = np.log(t) * (5 * log(2)) * (5 * 5 * log(2))
s1 = np.log(t * (1 + np.log(99 * (1 + np.log(2)))))  # red
s2 = np.log(t * (1 + np.log(2 * (1 + np.log(2 * (2 + np.log(2 * (2 + np.log(2)))))))))  # aqua
s3 = np.log(t * (1 + np.log(2 * (1 + np.log(2 * (2 + np.log(99 * (2 + np.log(2)))))))))  # green
# s4 = np.log(3 * t)
# s5 = np.log(3 * t)

fig, ax = plt.subplots()
# ax.plot(t, s)
# ax.plot(t, s1, color='red')
# ax.plot(t, s2, color='red')
# ax.plot(t, s3)
# ax.plot(t, s4)
ax.plot(t, s1, color='red')
ax.plot(t, s2, color='aqua')
ax.plot(t, s3, color='green')

ax.grid(True, linestyle='-.')

plt.show()
