def likelihood():
  likelihoods = (50, 38, 27, 99,4)
  return min(likelihoods), max(likelihoods)

def run():
  poss = likelihood()
  print(f"Minimum likelihood of falling: {poss[0]}%")
  print(f"Maximum likelihood of falling: {poss[1]}%")


run()