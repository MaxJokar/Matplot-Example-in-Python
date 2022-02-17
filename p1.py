
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
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
font2={'family':'tahoma','color':'green','size':15}
font3={'family':'tahoma','color':'black','size':10}
plt.title('My-Chart',fontdict=font2)
plt.xlabel('x-axis',fontdict=font1)
plt.ylabel('y-axis',fontdict=font1)
plt.text(10,40,' MyText',fontdict=font3,bbox=dict(facecolor='red',alpha=0.5))
# plt.grid()
plt.grid(axis='x',color='pink')
plt.savefig('chart1')# is saved in our folder
plt.show()




















