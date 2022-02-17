
import matplotlib.pyplot as plt
import numpy as np

x=[1,8,13,45]
y=[5,3,20,56]

# plt.plot(x,y,'o--')
# plt.plot(x,y,'o:')
# plt.plot(x,y,'o-.')
# plt.plot(x,y,'.-.')
# plt.plot(x,y,'x-')
# plt.plot(x,y,'p-r') #p for polygon r for red 
plt.plot(x,y,'p-r',ms=20,mec='b',mfc='g')
font1={'family':'tahoma','color':'blue','size':20}

plt.xlabel('x-axis',fontdict=font1)
plt.ylabel('y-axis',fontdict=font1)
plt.show()




















