from math import log
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

j = int(input())

# for j in range (3, 40):
#    if log(10 ** j) == log(10 ** j - 1):
#        print(j)
#        break

result = log(10 ** j) == log(10 ** j - 1)
print(str(result))

# print('finished')

