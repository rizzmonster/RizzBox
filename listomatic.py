#!/usr/bin/python3
#list manager for theory practice

i = 0
counter = 0
thisArray = []

while i < 1:
	usrInput = raw_input("Type something here: ")
	
	if str(usrInput) == "quit":
		break
 	
	if  str(usrInput) == "slice":
		print(thisArray[:5])
		print(thisArray[counter-3:counter])

	else:
		thisArray = thisArray + [usrInput]
		print(thisArray)
		counter += 1
print("out of loop?")