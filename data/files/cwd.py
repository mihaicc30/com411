def cwd():
  import os
  path = os.getcwd()
  print(f"Current working dir: {path}.\n")

  print(f"The directory contains the following:\n")
  for file in os.listdir(path):
    print(file)

cwd()
