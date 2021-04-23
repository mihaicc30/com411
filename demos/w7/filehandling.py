f1 = open("john.txt")
f2 = open("harry.txt")

for i in range(3):
  print(f"\033[92m John: {f1.readline()}\033[0m", end="")
  print(f"\033[93m Harry: {f2.readline()}\033[0m", end="")

#      \033[92m for text color

f1.close()
f2.close()