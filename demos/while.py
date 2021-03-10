#while loop (and also FOR loop ) can be used to have a repetition for a procedure in our code


print("How many times to print the symbol?")
x = int(input())

#i is a counter - it keeps track of how many times we went through the loop
i = 0

while i < x: #condition for repeteang the code as long as i is lower than x
  print("\u27BD", i) 
  i = i + 1 #new value of the counter is more than it used to be


print("We left the loop")