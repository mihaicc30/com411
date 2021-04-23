import os
path = os.getcwd()
print(path)

for file in os.listdir(path):
  print(file)