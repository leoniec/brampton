#Leonie Citron
#2.02.18
#timestablesgrid
print("Print a times tables grid")
print("Do you want the grid to be up to 12,13,14,15 or 16?")
answer = int(input())
#if statement triggers code based on input
#each input has a set of code
#loop multiplies numbers based on range specified in for loop
#numbers are printed and end is output
if answer == 12:
    for no in range(1, 13):
        for no1 in range(1, 13):
            print(no * no1, "", end="")
        print()
    print("End")
elif answer == 13:
    for no in range(1, 14):
        for no1 in range(1, 14):
            print(no * no1, "", end="")
        print()
    print("End")
elif answer == 14:
    for no in range(1, 15):
        for no1 in range(1, 15):
            print(no * no1, "", end="")
        print()
    print("End")
elif answer == 15:
    for no in range(1, 16):
        for no1 in range(1, 16):
            print(no * no1, "", end="")
        print()
    print("End")
elif answer == 16:
    for no in range(1, 17):
        for no1 in range(1, 17):
            print(no * no1, "", end="")
        print()
    print("End")
else:
    print("Out of range")



