from pymysql import connect
import os

connection = connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    db = os.getenv('MYSQL_DATABASE'),
    charset = 'utf8mb4'
)

loop = 0
loop1 = 0
loop2 = 0
while loop == 0:
    try:
        menu = int(input("Enter 1 to create an account, 2 to deposit money, 3 to withdraw money, 4 to show your account details and 5 to exit: "))
        if menu == 1:
            name = input("Enter name: ")
            password = input("Enter password: ")
            try:
                with connection.cursor() as cursor:
                    query = 'insert into account (name, password) values("' + name + '", "' + password +'");'
                    cursor.execute(query)
                connection.commit()
            finally:
                pass
            print("Thank you for creating your account with us.")
        elif menu == 2:
            while loop1 == 0:
                try:
                    deposit = float(input("Enter amount of money to be deposited: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                while loop2 == 0:
                    sure = input("Are you sure?(Y/N)")
                    if sure == 'Y':
                        try:
                            with connection.cursor() as cursor:
                                query = 'insert into money (deposit) values("' + str(deposit) + '")'
                                cursor.execute(query)
                            connection.commit()     
                        finally:
                            pass                   
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
                    print("Please enter a valid number.")
                    continue
                while loop2 ==0:
                    sure = input("Are you sure?(Y/N)")
                    if sure == 'Y':
                        try:
                            with connection.cursor() as cursor:
                                query = 'insert into money (withdrawal) values("' + str(withdrawal) + '")'
                                cursor.execute(query)
                            connection.commit()
                        finally:
                            pass
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
            try:
                with connection.cursor() as cursor:
                    query = 'select * from account;'
                    cursor.execute(query)
                    result = cursor.fetchall()
                    print(result)
            finally:
                pass
        elif menu == 5:
            connection.close()
            break
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")
