# take input + store name as variable 5/30
name = input("Enter Your Name: ")
age = input("Enter Your Age:")

#Give direct output
print ("Hello " + name)
print ("Your age is: " + age)

# Verify Name
if name == 'Admin':
    print ("Welcome Administrator!")
else:
    print ("Welcome to the program")

# Verify Age
if age >= '18':
    print ("Access Granted")
    #input
    noun = input('Enter a noun: ')
    noun2 = input('Enter another noun: ')
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')

    #Output
    print (f"Today I found a wild {noun}.")
    input ("Press enter to continue")
    print (f"Most people are afraid of {noun}, but they should really be afraid of {noun2}")
    input("Press enter to continue")
    print (f"Unfortunately, {noun2} can't stop {verb} innocent people")
    input("Press enter to continue")
    print (f"If people like to deal with more {verb}, they are certainly {adjective} and possibly afraid of {noun}")
    input("Press enter to continue")

else:
    print ("Access Denied")
    print("You're too young to play!")