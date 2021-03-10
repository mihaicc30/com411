i=1
while i >0:
  print("Enter your word master!")
  x = str(input())


  print("1. Display in a Box – display the word in an ascii art box")
  print("2. Display Lower-case – display the word in lower-case e.g. hello")
  print("3. Display Upper-case – display the word in upper-case e.g. HELLO")
  print("4. Display Mirrored – display the word with its mirrored word e.g. Hello | olleH")
  print("5. Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")

  print("Choose an option!")
  option = int(input())

  def wrong_number():
    #lol, my 6th def XD still counts right?haha
    print("\n")
    print("You entered a wrong number dude.")
    print("You start again yes :).\n")
    print("\n")

  def fifth(x):
    print("How many times do you want it displayed?")
    b = int(input())
    print(  (x.lower()+x.upper()) * b   )

  def fourth():
    print(x[::-1])

  def third(x):
    print(x.upper())

  def second(x):
    print(x.lower())

  def first(x):

    print("-" * len(x) * 4)
    print("-" * len(x) * 4)
    print("-" * len(x) * 4)
    print("-" * len(x) * 4)
    print("-" * len(x) * 1, x, "-" * len(x) * 1)
    print("-" * len(x) * 4)
    print("-" * len(x) * 4)
    print("-" * len(x) * 4)
    print("-" * len(x) * 4)

  if option == 1:
    first(x)
  elif option == 2:
    second(x)
  elif option == 3:
    third(x)
  elif option == 4:
    fourth(x)
  elif option == 5:
    fifth(x)
  else:
    wrong_number()