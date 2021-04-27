def search(file):
  print("Searching...")
  sections = []
  books = []
  with open(file) as file:
    for line in file:
      if line.startswith("Section"):
        section_name = line.split(":")[1]
        sections.append(section_name.strip())
      else:
        books.append(line.strip())
  print("Done!")
  return (sections, books)

def save(fn, xtuple):
  print("Saving...")
  with open(fn, "w") as fn:
    fn.write(f"Sections: {xtuple[0]}\n")
    fn.write(f"Books: {xtuple[1]}\n")
  print("Done!")

def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt", data)

run()
