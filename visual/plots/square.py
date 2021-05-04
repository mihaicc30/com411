import matplotlib.pyplot as plt

def small():
  x = [3,4,4,3,3]
  y = [3,3,4,4,3]
  plt.plot(x, y, "o:r")


def large():
  x =[1,6,6,1,1]
  y = [1,1,6,6,1]
  plt.plot(x,y,"b-p")


def medium():
  x =[2,5,5,2,2]
  y = [2,2,5,5,2]
  plt.plot(x,y,"gs--")

  

large()
medium()
small()
plt.show()