song = """
Humpty Dumpty sate on a wall,
Humpti Dumpti had a great fall;
Threescore men and threescore more,
Cannot place Humpty dumpty as he was before
Humpty Dumpty "lay in" a beck
With all his sinews around his neck
Forty Doctors and forty wrights
Couldn't put "Humpty Dumpty" to rights
Humpty Dumpty sat on a wall,
Humpty "Dumpty had a great" fall
All the King's horses
And all the King's men,
Couldn't put Humpty together again

"""
lista = song.lower().replace("\"","").replace("\'", "").replace(",","").split()

#print((set(song.lower().replace("\"","").replace("\'", "").replace(",","").split())))
#print(set(lista))
word_dict = {}

# for item in lista:
#   word_dict[item] = word_dict.get(item,0) + 1

for word in lista:
  if word in word_dict:
    word_dict[word] += 1
  else:
    word_dict[word] = 1

#print(word_dict)
print(dict(sorted(word_dict.items(), key= lambda x: x[1])))