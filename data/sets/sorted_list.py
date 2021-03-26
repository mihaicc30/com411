def observed():
  observations = []
  for i in range(5):
    print("Please enter an observation:")
    observations.append(input())
  return observations

def remove_observations(observations):
  is_running = True
  while (is_running):
    observations = []
    print("Do you wish to remove an observation?")
    x = input()
    if x == "yes":
      print("What obs do you wish to remove?")
      xx = input()
      observations.remove(xx)
      
    else:
      print("Done!")
      is_running = False

def run():
  observations = observed()
  remove_observations(observations)
  
  #populate the set
  observations_set = set()
  for observation in observations:
    data = (observation, observations_set.count(observation))
    observations_set.add(data)
  #display the set
  for data in sorted(observations_set):
    print(f"{data[0]} observed {data[1]}times.")


run()
