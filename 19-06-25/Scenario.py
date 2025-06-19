#1st question
import numpy as np
rev = np.array([20000,22000,21000,25000,24000])
ans=sum(rev)/len(rev)
print(ans)

#2nd question 
import numpy as np
temp=np.array([98.4,98.6,99.1,100.2,98.9,99.5,98.7])
max=temp.max()
min=temp.min()
print(f'Max {max}, min {min}')

#question
import numpy as np
prices=np.array([50,50,30])
qualities=np.array([2,2,3])
total=(prices*qualities)
total=total.sum()
print(total)

#question
import numpy as np
house_prices = np.array([45,50,48,52,47])
HP=house_prices+(house_prices*0.1)
print(HP)

#question 
import numpy as np
m=np.array([15.2,16.5,14.8,15.9,16.2,15.5])
#if m<15 :
   # print(m)

