def cross_bridge():
  steps = 0
  while steps < 12:
    print("Crossed step.")
    steps += 1
    if steps > 4 and steps < 6:
      print("We must keep going!")
    elif steps > 11:
      print("The bridge is collapsing!")
    


cross_bridge()


