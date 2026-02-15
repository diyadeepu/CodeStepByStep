# Write a function named longest_name that reads names typed by the user and 
# prints the longest name (the name that contains the most characters) in the 
# format shown below.

def longest_name(n) -> None:
    num = -100
    for i in range(1, n+1):
        name = input("name #" + str(i) + "? ")
        if (len(name) == num):
            vari = True
        else:
            vari = False
        if (len(name) > num):
            num = len(name)
            finalN = name
    print(finalN[0:1].upper() + finalN[1:].lower() + "'s name is longest")
    if (vari == True):
        print("(There was a tie!)")
