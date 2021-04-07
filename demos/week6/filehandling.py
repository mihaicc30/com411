file = open("gaga.txt")
#file.write("this a an example\nit makes no sense\nbecause i run out of ideas")
for i in file.readlines(0):
  print(i, end="")

file.close()