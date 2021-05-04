import matplotlib.pyplot as plt

fig,axes = plt.subplots(2,2)
x = range(0,10,1)
y = range(0,20,2)
axes[0,0].plot(x,y)
axes[1,1].plot(x,y)
plt.show()