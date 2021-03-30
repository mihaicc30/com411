def observed():
  observations = []

  for i in range(7):
    observations.append(input())
  return observations

def run():
  print("Counting observations...")
  list_of_observations = observed()
  set_of_observations = set()

  for item in list_of_observations:
    t = ( item, list_of_observations.count(item))
    set_of_observations.add(t)
    
  for item in set_of_observations:
    print(f"{item[0]} observed {item[1]} times.")
    

run()