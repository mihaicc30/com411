print("What is your name ?")
n = input()
#print("Do you have a dog? (types True or False)")
#dog = input()

if len(n) >= 9:
  print("You have a very long nameeeeee!")
  print ("Your name contains {} letters".format(len(n)))
elif len(n) > 6:
  print("Your name is a bit long. Consider a nickname.")
elif len(n) < 3:
  print("Your name is veryyyy short.")

else:
  print ("Your name is ok!")

print("This is the END of the program!")


#and statement
# t + t = true
# t + F = false
# f + f = false
# f + t = false

#or statement
# t + t = true
# t + F = true
# f + f = true
# f + t = false