# Write a function named smallest_largest that asks the user to enter numbers, 
# then prints the smallest and largest of all the numbers typed in by the user. 
# You may assume the user enters a valid number greater than 0 for the number of
# numbers to read.

def smallest_largest() -> None:
    num = int(input("How many numbers do you want to enter? "))
    smallest = 1000
    largest = 0
    for i in range(1, num+1):
        a = int(input("Number "+ str(i) + ": "))
        if (smallest > a):
            smallest = a
        if (largest < a):
            largest = a
    print("Smallest = " + str(smallest))
    print("Largest = " + str(largest))
