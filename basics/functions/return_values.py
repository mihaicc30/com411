
def sum_weights(w1, w2):
  return w1+w2

def calc_avg_weight(w1, w2):
  return(w1 + w2) / 2

def run():
  print("What is the weight of Beep?")
  w1 = int(input())
  

  print("What is the weight of Bop?")
  w2 = int(input())
 

  print("What would you like to calculate (sum or average)?")
  z = str(input())
  x = str("sum")
  y = str("average")
  if z == x:
    print(f"The sum of Beep and Bop's weight is {sum_weights(w1, w2)}.")
  elif z == y:
    print(f"The average of Beep and Bop's weight is {calc_avg_weight(w1, w2)}.")


run()



#big pain to code this for some reason -_-