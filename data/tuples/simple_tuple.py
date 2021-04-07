def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods)

def run():
  LH = likelihood()
  print(f"Minimum likelihood of falling: {LH}%.")

run()