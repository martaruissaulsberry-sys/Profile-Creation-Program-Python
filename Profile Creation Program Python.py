def create_username(user_name: str):
    import random
    import string
    return user_name.lower()
def create_password(Password: str):
    import random
    import string
    return Password.lower()
def forgot_password():
    import random
    import string
    new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print(f"Your new password is: {new_password}")
def forgot_username():
    import random
    import string
    new_username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print(f"Your new username is: {new_username}")
def display_credentials(username: str, password: str):
    print(f"Username: {username}")
    print(f"Password: {password}")
def login(username: str, password: str):
    stored_username = "user123"
    stored_password = "pass123"
    if username == stored_username and password == stored_password:
        print("Login successful!")
def main():
    user_name = input("Enter your desired username: ")
    username = create_username(user_name)
    Password = input("Enter your desired password: ")
    password = create_password(Password)
    display_credentials(username, password)
    print("Profile created successfully!")
    login(username, password)
if __name__ == "__main__":
    main()
    