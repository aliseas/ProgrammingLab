"""
import numpy as np

mean_list = np.mean([24.93,24.72,24.41,24.14,24.17,25.57,25.64,25.71,25.39,25.20,25.29,25.99,25.82,25.74,26.16,26.70,27.04,26.63,25.78,26.10,25.96,25.41,25.13,25.02])

print(mean_list)
"""
"""
line = "                 una linea   ."
line = line.strip()
print(line)
"""

import numpy as np

a = [24.93,24.72,24.41,24.14,24.17,25.57,25.64,25.71,25.39,25.20,25.29,25.99,25.82,25.74,26.16,26.70,27.04,26.63,25.78,26.10,25.96,25.41,25.13,25.02]

print(sum(a)/len(a))
print(np.mean(a))
print(np.average(a))