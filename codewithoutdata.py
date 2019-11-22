loop = 0
loop1 = 0
loop2 = 0
while loop == 0:
    menu = int(input("Enter 1 to create an account, 2 to deposit money, 3 to withdraw money, 4 to show your account details and 5 to exit: "))
    if menu == 1:
        name = input("Enter name: ")
        password = input("Enter password: ")
        print("Thank you for creating your account with us.")
    elif menu == 2:
        while loop1 == 0:
            try:
                deposit = float(input("Enter amount of money to be deposited: "))
            except ValueError:
                print("Please enter a valid number")
                continue
            while loop2 == 0:
                sure = input("Are you sure?(Y/N)")
                if sure == 'Y':
                    print("Thank you. Your money has been deposited.")
                    break
                elif sure == 'N':
                    break
                else:
                    print("Please enter a valid response.")
                    continue
            if sure == 'Y':
                break
    elif menu == 3:
        while loop1 == 0:
            try:
                withdrawal = float(input("Enter amount of money to be withdrawn: "))
            except ValueError:
                print("Please enter a valid number")
                continue
            while loop2 ==0:
                sure = input("Are you sure?(Y/N)")
                if sure == 'Y':
                    print("Thank you. Your money has been withdrawn.")
                    break
                elif sure == 'N':
                    break
                else:
                    print("Please enter a valid response.")
                    continue
            if sure == 'Y':
                break
    elif menu == 4:
        print("Here are your account details: ")
    elif menu == 5:
        break
    else:
        print("Please enter a valid number.")
