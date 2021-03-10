def identify():
  print("What lies before us?")
  x = str(input())
  if x == "a large boulder":
    print("Its time to run!")
    print("What should we do?!")
    escape_by()
  else:
    print("Its going to be fine.")




def escape_by():
  plan = str(input())
  if plan == "jumping over":
    print("We cannot escape that way! The boulder is too big!")
  elif plan == "running around":
    print("We cannot escape that way! The boulder is moving too fast!")
  elif plan == "going deeper":
    print("That might just work! Let's go deeper!")
  else:
    print("We cannot escape that way! The boulder is in the way!")

identify()
