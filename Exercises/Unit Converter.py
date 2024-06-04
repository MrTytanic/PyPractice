# temperature converter 6/1 - modified to be weight and temperature convertor 6/3

while True:
# get input
    choice = input("Are you converting Weight or Temperature?: ")

    if choice == "Weight":
        unit = input("Kilograms or Pounds?: ")
        mass = int(input("What is the object's weight?: "))

        if unit == "Kilograms":
            answer = round((mass / 2.205))
            print(f"The object's weight is {answer} in {unit}.")
        elif unit == "Pounds":
            answer = round((mass * 2.205))
            print(f"The object's weight is {answer} in {unit}.")
        else:
            print("Invalid unit! Please choose between 'Kilograms' or 'Pounds'.")
        break 
    elif choice == "Temperature":
        scale = input("Fahrenheit or Celsius?: ")
        temp = int(input("What is the temperature you are converting?: "))
     
        if scale == "Fahrenheit":
            answer = round((temp - 32) * 5/9)
            print(f"The temperature converted to Celsius from {scale} is: {answer:.2f}.")
        elif scale == "Celsius":
            answer = round((temp * 5/9) + 32)
            print(f"The temperature converted to Fahrenheit from {scale} is: {answer:.2f}.")
        else:
            print("The input is invalid!")
        break
    else:
        print("Invalid choice! Please choose between 'Weight' or 'Temperature'.")
