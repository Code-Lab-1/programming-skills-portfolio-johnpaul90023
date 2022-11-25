#The price of the ticket is determined by the input on the age.

prompt = "How old are you? \n"
prompt += "Enter 'exit' once you are complete. \n"

while True:
    age = input(prompt)
    if age == 'exit':
        break
    age = int(age)

    if age < 3:
        print("  You get a free ticket. \n")
    elif age < 13:
        print("  Your ticket costs $10. \n")
    else:
        print("  Your ticket costs $15. \n")


