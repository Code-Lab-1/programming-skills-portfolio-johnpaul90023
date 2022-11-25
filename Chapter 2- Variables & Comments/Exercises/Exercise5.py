#Calculating on how many USB sticks can the girl buy
money = int(input("Each USB stick costs £6, enter your money "))
cost = int(6)
solution = money//cost
confirm = int(1)
if solution == (8) :
    money = int(input("Purchasing 8 USB sticks cost 48, Do you want to purchase, enter 1 for yes and 2 for no "))
    if money == confirm: 
        print("You have purchased 8 USB sticks and your change is £2")
    else: 
        print("You have cancelled your transaction")
