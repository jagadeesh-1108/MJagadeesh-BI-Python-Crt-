# pie chart 
'''
import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,55])
plt.pie(y)
plt.show()'''

#names or labels 
# pie chart 
import matplotlib.pyplot as plt
import numpy as np
y=np.array([10,10,15,20,12,13,20])  
mylabels=['Java','Python','SQL','Numpy','C++','C','Pandas']
myexplode =[0,0.2,0,0,0,0,0]
plt.pie(y,labels=mylabels,startangle=360,explode=myexplode,shadow=True)    
plt.legend(title="Programming Languages")
plt.show()