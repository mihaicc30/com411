print("What is your name ?")
n = input()
print("Do you have a dog? (types true or false)")
dog = input()

if len(n) > 9 and dog == "True":
  print("You have a very long nameeeeee!")
  print("Your name contains {} letters".format(len(n)))
else:
  print ("Your name is ok!")

print("This is the END of the program!")



# t + t = true
# t + F = false
# f + f = false
# f + t = false
