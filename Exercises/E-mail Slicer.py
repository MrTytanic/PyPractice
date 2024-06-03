# email slicer string index 5/30

while True: #loops the project so you can re-enter ur email infinately
    email = input("Enter your email: ") #email

    index = email.find("@") #find index of @ symbol

    if index != -1: #slice the string
        username = email[:index]
        domain = email[index + 1:]
        print(f"Your username is: {username} and its domain is {domain}")
    else:
        print("Invalid email format! It does not contain @ symbol.")