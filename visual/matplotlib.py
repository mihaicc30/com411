import matplotlib.pyplot as plt

x=[0,2,4,6,8,10,13,15,100]
y=[10,14,17.3,23,28,34,70,99,1]

plt.xlabel("Age")
plt.ylabel("Score")

plt.plot(x,y,"gD-")
#plt.step(x,y,"gD-")

#plt.plot(x,y)
plt.show()