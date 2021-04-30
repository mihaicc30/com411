import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,2)

x = ["Poland","Romania","Bangladesh"]
y = [2, 17, 2]
y2 = [5,6,12]
y3 = [1,1,3]

axes[0,0].bar(x,y)
axes[0,1].plot(x,y2)
axes[1,1].pie(y3, labels=x)

plt.tight_layout()

plt.show()