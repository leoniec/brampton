#Leonie Citron
#05/02/2018
#Pizza Order program

#DECLARE Order : STRING
#DECLARE OrderNo : INTEGER
#DECLARE Base : STRING
#DECLARE Choice : STRING
#DECLARE Again : STRING
#DECLARE TopCount : INTEGER
#DECLARE Index : INTEGER
#DECLARE ShopOpen : BOOLEAN
#DECLARE EndOrder : BOOLEAN

Order =""
OrderNo = 1
Base = ""
Choice = ""
Again = ""
TopCount = 0
Index = 0
ShopOpen = True
EndOrder = False

#DECLARE TopName : Array [0..9] of STRING
TopName = ["","","","","","","","","",""]
TopName[0] = "Cheese"
TopName[1] = "Ham"
TopName[2] = "Pepperoni"
TopName[3] = "Pineapple"
TopName[4] = "Mushroom"
TopName[5] = "Cherry tomatoes"
TopName[6] = "Chicken"
TopName[7] = "Peppers"
TopName[8] = "Olives"
TopName[9] = "Jalapenos"
#DECLARE TopAmnt : Array [0..9] of INTEGER
TopAmnt = ["","","","","","","","","",""]
TopAmnt[0] = 10
TopAmnt[1] = 10
TopAmnt[2] = 10
TopAmnt[3] = 10
TopAmnt[4] = 10
TopAmnt[5] = 10
TopAmnt[6] = 10
TopAmnt[7] = 10
TopAmnt[8] = 10
TopAmnt[9] = 10

print("0", TopName[0],TopAmnt[0])
print("1", TopName[1],TopAmnt[1])
print("2", TopName[2],TopAmnt[2])
print("3", TopName[3],TopAmnt[3])
print("4", TopName[4],TopAmnt[4])
print("5", TopName[5],TopAmnt[5])
print("6", TopName[6],TopAmnt[6])
print("7", TopName[7],TopAmnt[7])
print("8", TopName[8],TopAmnt[8])
print("9", TopName[9],TopAmnt[9])

print("Would you like a thin or pan pizza base?")
base = input()
while base != "P" and base !="T":
    print("Pleae enter P or T")
    base = input()
Order = Order + base





