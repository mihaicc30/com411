def search(file_name):
  print("Searching...")
  data = {}

  with open(file_name) as file:
    section_name = "" 

    for line in file: #reading the file contents
      if (line.startswith("Section")):  #if line starts with section
        parts = line.split(":")         #then split it at the : into 2, thats index 0 and 1
        section_name = parts[1].strip() #and then grab the 2nd half of the line and strip                                   the \u and add it to our string
      
      elif (section_name in data):      
        data[section_name].append(line.strip())

      else:
        data[section_name] = [line.strip()]
    
  print("Done!")
  return data

def run():
  data = search("data/files/txt/books.txt")

  with open("data/files/txt/generated.csv", "w") as file:
    for section, books in data.items():
      for book in books:
        file.write(f"{section},{book}\n")

run()