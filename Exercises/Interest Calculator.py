#interest calculator 5/31

Principal = 0
Rate = 0
Time = 0

while Principal <= 0:
    Principal = float(input("Principal Amount: "))
    Rate = float(input("Rate: "))
    Time = float(input("Time in years: "))
    if Principal <= 0:
        print("Principle cannot be less than or equal to zero")
    else:
        Total = Principal * pow((1 + Rate / 100), Time)
    print(f"Your final total after {Time} years is: {Total:.2f}")