print("Program Started!")
print("Please enter an ASCII code:")
x = int(input())

if x in range(32, 126):
   print(f"The ASCII code for {x} is: {chr(x)}")
   print("Program Ended!")
else:
  print("Character is not in range.")


