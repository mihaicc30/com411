print("\u2701")


print("Please enter the number of lives.")
lives = int(input())
print("Please enter the energy level.")
energy = int(input())
print("Please enter the shield level.")
shield = int(input())

i = 0
o = 0
p = 0
print("\n")
print("Health has been set.")
print("\n")
print(f"Lives:  {'\u2764' * lives}")
print(f"Lives:  {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")

# remember to ask Piotr where the f and the {} come from