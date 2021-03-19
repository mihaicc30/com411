def get_fruits():
  fruits = []
  n = int(input())

  for i in range(n):
    print("Type in the next fruit")
    fruits.append(input())

  #print all items
  print("Your fruits are {}".format(fruits))

  #print only few items by slicing
  print(f"Sliced list: {fruits[0:5:2]}")

  #print few items with negative index
  print(f"Negative index: {fruits[-2:0:-1]}")

get_fruits()






# #define a list
# fruits = []
# #define a list with items
# vegetables = ["carrot", "Peas"]

# print(vegetables)

# #add items to the END OF list
# fruits.append("Apple")
# fruits.append("Banana")
# fruits.append("Tomato")
# fruits.append("Banana")

# print(fruits)

# #remove an item from the list
# fruits.remove("Banana")

# print(fruits)

# #remove item by index
# del fruits[1]
# print(fruits)

# #insert a value not at the end

# #add a pineapple at index 1
# fruits.insert(1, "Pineapple")
# print(fruits)

# #print only the item at index 0
# print(fruits[0])

