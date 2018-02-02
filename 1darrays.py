#DECLARE myPetName : Array [0..3] of STRING
#myPetName [0] = "Dog"
#myPetName [1] = "Cat"
#myPetName [2] = "Bear"
#myPetName [3] = "Giraffe"
#for index <-- 0 to 3
#output myPetName [index]
#NEXT index
myPetName = ["","","",""]
myPetName [0] = "Dog"
myPetName [1] = "Cat"
myPetName [2] = "Bear"
myPetName [3] = "Giraffe"

print (myPetName)

