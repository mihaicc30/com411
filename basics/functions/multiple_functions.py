def display_ladder(steps):
  print(" *** \n | |\n" * steps)
  


def create_ladder():
  print("How many remaining steps?")
  steps = int(input())
  print(" | | ")
  display_ladder(steps)


create_ladder()