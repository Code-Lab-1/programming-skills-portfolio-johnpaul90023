#The same with exercise 4 but removed a sandwhich in the order list and added an apology

sandwich_orders = [
    'Big Mac', 'Big Tasty', 'Mc Chicken', 'Spicy Mc Chicken', 'Pastarami',
    'Spicy Mc Chicken', 'Pastarami', 'Pastarami', 'Big Tasty', 'Spicy Mc Chicken']
finishedsandwiches = []

print("\n")
print("We're sorry, but we're out of Pastarami today.")
while 'Pastarami' in sandwich_orders:
    sandwich_orders.remove('Pastarami')

print("\n")
while sandwich_orders:
    currentsandwich = sandwich_orders.pop()
    print(f"I am currently making your {currentsandwich} sandwich.")
    finishedsandwiches.append(currentsandwich)

print("\n")
for sandwich in finishedsandwiches:
    print(f"Your {sandwich} sandwhich can now be served to you.")

print(sandwich_orders)