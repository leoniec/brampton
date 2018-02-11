#Leonie Citron
#File reading and writing
#07.02.18

#DECLARE answer as STRING
#DECLARE filename as STRING

filename = "LC_T3.txt"
fh = open("LC_T3.txt", "w")
#above line opens the text file for writing
print("What would you like the file to say?")
answer = input()
fh.write(answer)
#writes the user input into the file and closes the file
fh.close
