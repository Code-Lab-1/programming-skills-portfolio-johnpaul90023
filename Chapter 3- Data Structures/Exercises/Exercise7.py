#Printing the places on the list in sorted, reverse sorted, and reverse order

places = ["Tokyo", "Paris", "New Zealand", "New York", "Salar de Uyuni "]

print(places, "\n")

print("Sorted Order ")
print(sorted(places))
print("Original Order")
print(places, "\n")

print("Reverse Sorted Order")
print(sorted(places, reverse=True))
print("Original Order")
print(places, "\n")

print("Reversed Order")
places.reverse()
print(places, "\n")

print("Original Order")
places.reverse()
print(places, "\n")

print("Sorted Order")
places.sort()
print(places, "\n")

print("Reversed Sorted Order")
places.sort(reverse=True)
print(places, "\n")


