
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np

# x=[1,8,13,45]
# y=[5,3,20,56]

# plt.plot(x,y,'o--')
# plt.plot(x,y,'o:')
# plt.plot(x,y,'o-.')
# plt.plot(x,y,'.-.')
# plt.plot(x,y,'x-')
# plt.plot(x,y,'p-r') #p for polygon r for red 
# plt.plot(x,y,'p-r',ms=20,mec='b',mfc='g')
# font1={'family':'tahoma','color':'blue','size':20}
# font2={'family':'tahoma','color':'green','size':15}
# font3={'family':'tahoma','color':'black','size':10}
# plt.title('My-Chart',fontdict=font2)
# plt.xlabel('x-axis',fontdict=font1)
# plt.ylabel('y-axis',fontdict=font1)
# plt.text(10,40,' MyText',fontdict=font3,bbox=dict(facecolor='red',alpha=0.5))
# # plt.grid()
# plt.grid(axis='x',color='pink')
# plt.savefig('chart1')# is saved in our folder
# plt.show()


#=============================================PART 2
# x=np.linspace(0,10,10 )
# y=np.linspace(0,10,10 )
# plt.plot(x,y,'o-')
# plt.show()


# x=[1,8,13,45]
# y=[5,3,20,56]
# plt.plot(x,y,'o-')
# plt.show()


# x=np.linspace(-2,2,100 )
# y=x**2
# plt.plot(x,y)
# plt.show()

# x=np.linspace(-2,2,100 )
# y=x**3
# plt.plot(x,y)
# plt.show()
#========================Subplots==================================

# x=np.linspace(-2,2,100 )
# y=x**2
# plt.subplot(2,3,1)
# plt.plot(x,y)

# x=np.linspace(-2,2,100 )
# y=x**3
# plt.subplot(2,3,2)
# plt.plot(x,y)

# plt.subplot(2,3,2)
# y=x**4
# plt.subplot(2,3,3)
# plt.plot(x,y)

# plt.show()


# x=np.linspace(0,2*np.pi,100)
# y=np.sin(x)
# print(x)
# print(y)
# plt.plot(x,y)
# plt.show()



# x=np.linspace(0,2*np.pi,100)
# y=np.cos(x)
# plt.subplot(1,2,2)


# plt.plot(x,y)

# plt.show()


#=============Scatter================

# x=np.linspace(-2,2,40 )
# y=x**3
# # plt.scatter(x,y)
# plt.scatter(x,y,color='green')
# plt.show()


# x=np.linspace(-2,2,40 )
# y=x**3
# plt.scatter(x,y,color='blue')

# x=np.linspace(-2,2,40 )
# y=x**2

# plt.scatter(x,y,color='red')
# plt.show()



#==========Bar chart
# x=np.array(['2018','2019','2020','2021'])
# y=np.array([500,600,700,900])
# plt.bar(x,y)
# plt.show()

# x=np.array(['2018','2019','2020','2021'])
# y=np.array([500,600,700,900])
# plt.bar(x,y,color='green')
# plt.show()

#====================Pie Chart=================

# y=np.array([23,5,2,60,10])
# plt.pie(y)
# plt.show()


y=np.array([20,50,10,15,5])
colors=['green','pink','black','red','purple']
labels=['Andy','George','Mark','Daniel','David']
# plt.pie(y,colors=colors,labels=labels)
# plt.pie(y,colors=colors,labels=labels,shadow=True)
plt.pie(y,colors=colors,labels=labels,shadow=True,startangle=90)
plt.show()



























