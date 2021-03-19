def movements():
  path = ["move forward", 10, "move backward", 5, "move left", 3, "move right", 1]
  return path

def run():
  print("Moving...")
  path = movements()
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")
  print(f"{path[6]} for {path[7]} steps")


# def run():
#   print("Moving...")
#   path = movements()
#   for index in range(0, len(path), 2):
#     print(f"{path[index]} for {path[index+1]} steps"


run()