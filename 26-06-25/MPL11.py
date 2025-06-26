#creating Scatter Plots 
'''With pyplot you can use the scatter() function to draw a '''
#creating scatter plot
'''
import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,7,4,2,1])
y=np.array([6,9,10,15,21])
plt.scatter(x,y)
plt.show()
###########################
import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,7,4,2,1])
y=np.array([6,9,10,15,21])
plt.scatter(x,y,color="#a64ea0")
plt.show()'''
import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,7,4,2,1])
y=np.array([6,9,10,15,21])
colors =np.array([0,10,20,30,40])
plt.scatter(x,y, c=colors, cmap='viridis')
plt.show()