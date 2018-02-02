#You have been asked to ensure that array indexes are validated before displaying or altering the cells in the 2D array
#Write the section of code which asks the user to enter the row and column numbers and makes sure they are within the
#valid range. Use a conditional loop to ensure that the user is continually asked until the values are valid.

print ("Input a row number")
rownumber = int(input())
while rownumber > 4 or rownumber <0:
    print("Enter a valid row number")
    rownumber = int(input())
print ("Input a column number")
colnumber = int(input())
while colnumber > 3 or colnumber <0:
    print("Enter a valid column number")
    colnumber = int(input())