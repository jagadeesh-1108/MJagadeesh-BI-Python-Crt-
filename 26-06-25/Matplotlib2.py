import numpy as np
import matplotlib as pyt
import matplotlib.pyplot as plt
print(np.version)
A=np.array([1,2,3,4])
B=np.array([2,4,6,8])
plt.plot(A,B)
plt.plot(A,B,marker='D',color='g')
plt.show()