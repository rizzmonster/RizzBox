#!/usr/bin/python3
#standard fibbonaci sequence program

#welcome message
print("Hi there!\nWelcome to the fibbonaci sequence generator!\nThis will generate the fibbonaci sequence indefinitely...\n")

#Get user input for later
InEndI = input("How many steps?: ")

#make a function so I don't have to recode this 
#mess as I clean it up and progress to later steps of development
def fibbsequence(endI):
	#initialize sequence
	a, b, c, counter = 0, 1, 0, 0
	while counter < endI:
		c = a + b
		a = b
		b = c
		print(a)
		counter += 1
	#print string for debugging flow
	print("Out of loop?")

#call fibb function
fibbsequence(InEndI)