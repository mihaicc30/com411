# print("The letter '@' in the ASCII table is represented by {}".format(ord('@')))

# print("The letter '@' in the ASCII table is represented by {}".format((hex(ord('@')))))
#---------------------------------------------------------------
# # #defining my own function to calculate area of a triangle
# def calculate_area(h, b):
#   area = 0.5 * h * b
#   print(area)

# print("Enter height and base of triangle")
# h = float(input())
# b = float(input())

# #call the function
# calculate_area(h, b)
# #parameter = a value that you plug into a function
# ---------------------------------------------------------------

def calculate_area(h = 10 , b = 5):
  area = 0.5 * h * b
  return(area)
# h = 10
# b = 5
# calculate_area()

def run():
  x = calculate_area(4, 5)
  x+=1
  print(f"The area of triangle is {x}")

print(calculate_area())
x = calculate_area(12,5)
print(x+1)


calculate_area(5)
calculate_area(b = 20)
calculate_area(13, 7)


run()