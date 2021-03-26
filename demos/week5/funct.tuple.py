#program that imitates a small databasein the sense that it can:
#insert new student and their marks
#keep continually add students
#print out student's name and their mark
#average mark of all students
#find max mark among all students

def generate_stds():
  print("Enter a name:" )
  name=input()
  print("Enter the grade: ")
  grade = int(input())
  return name, grade

def all_stds():
  all_students = []
  while True:
    all_students.append(generate_stds())
    print("to stop adding students, type 0")
    x = input()
    if x == "0":
      break
  return all_students

print(all_stds())

def print_students(lista):
  for std in lista:
    print(f"{std[0]} earnd a grade {std[1]}. ")



def avr_mark(lista):
  total = 0
  for std in lista:
    total += std[1]
  return total/len(lista)

print(avr_mark(all_stds()))

