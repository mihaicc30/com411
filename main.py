print("What is your name ?")
n = input()

if len(n) > 9:
  print("You have a very long nameeeeee!")
  print("Your name contains {} letters".format(len(n)))
else:
  print ("Your name is ok!")

print("This is the END of the program!")
