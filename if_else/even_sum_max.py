# Write a function named even_sum_max that prompts the user for many integers
# and print the total even sum and maximum of the even numbers. You may assume
# that the user types at least one non-negative even integer.

def even_sum_max() -> None:
    num = int(input("how many integers? "))
    i = 0
    sum = 0
    max = 0
    while i < num:
        nextVal = int(input("next integer? "))
        if (nextVal % 2 == 0):
            sum += nextVal
            if (nextVal > max):
                max = nextVal
        i+=1
    print("even sum =",str(sum))
    print("even max =",str(max))
