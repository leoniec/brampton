#3x3
#Leonie Citron + Yael Sheinman
#25.01.18
import random

#declare grid: array [0..3, 0..3] of integer
grid = [[0 for col in range(0,3)]for row in range(0,3)]

def exists(num):
    found = False
    for row in range(0,3):
        for col in range(0,3):
            if num == grid[row][col]:
                found = True
    return found

for row in range(0,3):
    for col in range(0,3):
            newNum = random.randint(1,9)
            if exists(newNum) != True:
                grid[row][col] = newNum
                added = True
            else:
                print('Already there... trying again')

print(grid)

# 2.1 input validation 1-9
num = int(input('enter a number 1-9'))
while num <1 or num > 9:
    print('number invalid')
    num = int(input('enter a number 1-9'))
# 2.2 start row loop
for row in range (0,3):
# 2.3    start col loop
    for col in range (0,3):
# 2.4        IF grid[row][col] == num
        if grid[row][col] == num:
# 2.5            output row and col
            print('found at ',row,col)
# 2.6        END IF
# 2.7    end loop
# 2.8 end loop