#initialise a set

#colours = {} #for dictionary

colours = set()
print(type(colours))

# initialise non empty set

colors = {"blue", "red", "yellow"}

print(type(colors))
print(colors)

#adding elements to a set
colors.add("purple")
colours.add("red")
colours.add("black")
colours.add("green")

print(colours)
print(colors)


#union - joining two sets

set1 = colours.union(colors)

print(set1)

#intersection - fining common elements

set2 = colours.intersection(colors)

print(set2)