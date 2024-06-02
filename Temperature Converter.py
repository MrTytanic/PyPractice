# temperature converter 6/1

while True:
# get input
    scale = input("Fahrenheit or Celsius?: ")
    temp = int(input("What is the temperature you are converting: "))

    if scale == "Fahrenheit":
        answer = round((temp - 32) * 5/9)
        print(f"The temperature converted to Celsius from {scale} is: {answer:.2f}.")
    elif scale == "Celsius":
        answer = round((temp * 5/9) + 32)
        print(f"The temperature converted to Fahrenheit from {scale} is: {answer:.2f}.")
    else:
        print("The input is invalid!")