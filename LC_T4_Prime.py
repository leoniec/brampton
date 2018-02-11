#user inputs a number
#program should print on screen all prime numbers less than or equal to that number

#Leonie Citron
#09/02/18

#user inputs the number that they want to test
number = int(input("What is the numbe you would like to see the prime string of?"))
for b in range(number):
    #tests numbers in range from 0 to inputted number to see if they give answers specified by conditions
    if b%2!=0 and b%3!=0 and b%5!=0 and b%7!=0 and b!=0 and b!=1 or b==2 or b==3 or b==5 or b==7:
        print(b)
    #as loop does not output the inputted number, additional if statement tests the actual number
if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0 and number != 0 and number != 1 or number == 2 or number == 3 or number == 5 or number == 7:
    print(number)
#takes 4s seconds to print each prime between 0 and 100000
answer = input("Are you ready to close the program, yes or no?")
while (answer == "no"):
    answer = input("Are you ready to close the program now?")
print("Okay, program will close")
