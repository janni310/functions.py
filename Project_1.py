users = {'matti@gmail.com' : 'matti',
        'antti@outlook.com' : 'antti',
        'satu@gmail.com' : 'satu'}

def login_or_create_account():
    """
    This is a simple login function.
    Asks the user if they already have a user account or not.
    """
   
    account = input("Do you have an account? y/n: ")
    if account == 'y':
        old_user()
            
    elif account == 'n':
        new_user()
            


def old_user():
    """
    If user already has an account, this function allows them to login.
    """

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users and users[email] == password:
        print("Login successful.")

    else:
        print("Wrong email or password.")
        
    


def new_user():
    """
    If user does not have an account, this function allows them to create one.
    """

    new_email = input("Enter your email: ")
    if new_email not in users:

        new_password = input("Enter your password: ")
        new_password2 = input("Confirm your password: ")

        if new_password != new_password2:
            print("Passwords don't match!")

        else:
            users[new_email] = new_password
            print("User account created.")

    else:
        print("You already have an account.")


login_or_create_account()
