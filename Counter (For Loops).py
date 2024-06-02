#for loop lesson 6/2
#for loops = execute a block of code a fixed number of times.
#you can iterate over a range, string, sequence, etc.

while True:
    direction = input("Counting Up or Down?: ")
    start = (int(input("Starting Value: ")))
    end = (int(input("Ending Value: ")))
    if direction == 'Down' or 'down':
        for counter in reversed(range(start, end+1)):
            print(counter)
    elif direction == "Up" or 'up':
        for counter in (range(start, end+1)):
            print(counter)
    else:
        print("The input is invalid!")