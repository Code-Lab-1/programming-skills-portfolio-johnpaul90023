#A shrinking list that removes the names on the list each time
names = ["John", "Jeff", "Joe"]
print( names[0], "You are invited to dinner at November 30 in Mc Donalds, 12:00 PM")
print( names[1], "You are invited to dinner at November 30 in Mc Donalds, 12:00 PM")
print( names[2], "You are invited to dinner at November 30 in Mc Donalds, 12:00 PM \n")

names.pop(2)
print("Joe is Unavaible at November 30, We should invite Jeffrey")
names.insert(1, "Jeffrey")
print( names[1], "You are invited to dinner at November 30 in Mc Donalds, 12:00 PM \n")

print("There is only two space left on the dinner table")
print( names[0], "Sorry but there is no space at the table \n")
People = names.pop(0)

print( names[0], "Please come to dinner at November 30 in Mc Donalds, 12:00 PM")
print( names[1], "Please come to dinner at November 30 in Mc Donalds, 12:00 PM \n")

del(names[0])
del(names[0])

print("This are the list of names", names)