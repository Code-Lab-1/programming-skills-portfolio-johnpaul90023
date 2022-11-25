#Asking the user on what topping to add on his pizza and enter exit when finished

prompt = "\nWhat topping would you like to add on your pizza? "
print("\n")
prompt += "\nThis are the list of toppings: "
prompt += "\nPepperoni, Sausage, Mushrooms, Bacon, Extra Cheese, Onions, Peppers, Chicken"
prompt += "\nEnter 'exit' when you are finished: "
while True:
    topping = input(prompt)
    if topping != 'exit':
        print(f"Okay I am going to add {topping} to your pizza.")
    else:
        break

