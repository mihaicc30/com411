def search(location):
  print("Searching...")
  # with open(location) as loc:
  #   for line in loc:
  #     print(f"Looked in {line}", end="")
  with open(location) as file:
    for line in file.readlines():
      print(f"looked in {line.strip()}")
    print("...Done!")

def run():
  search("data/files/txt/locations.txt")

run()