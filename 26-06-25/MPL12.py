#bar graph
'''
import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y= np.array([3,8,1,10])
plt.bar(x,y)
plt.show()

#bar graph - horizontal
import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y= np.array([3,8,1,10])
plt.barh(x,y)
plt.show()'''
#bar graph - colors
import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y= np.array([3,8,1,10])
plt.bar(x,y,color = 'hotpink',width=0.1)
plt.show()