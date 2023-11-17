#In the list there are sets of sandwhiched that were placed into messages using while and for statement

sandwich_orders = ['Big Mac', 'Big Tasty', 'Mc Chicken', 'Spicy Mc Chicken']
finishedsandwiches = []

while sandwich_orders:
    currentsandwich = sandwich_orders.pop()
    print(f"I am currently making your {currentsandwich} sandwich.")
    finishedsandwiches.append(currentsandwich)

print("\n")
for sandwich in finishedsandwiches:
    print(f"Your {sandwich} can now be served to you.")