def directions():
  directions = ["more forward", "move backward", "turn left", "turn right"]
  return directions

def menu():
  print("Please select a direction:")
  dirs = directions()
  for index in range(len(dirs)):
    print(f"{index}: {dirs[index]}")


def run():
  menu()

run()