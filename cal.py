val1 = float(input("Enter first number: "))
val2 = float(input("Enter second number: "))
opr  = float(input("Please Select the operation numbere:\n 1: Sum \n 2: Subtract \n 3: Multiply \n 4: Divide \n 5: Reminder \n Enter the number of the Operation: "))
sum = float(val1 + val2)
sub = float(val1 - val2)
mul = float(val1 * val2)
div = float(val1 // val2)
rem = float(val1 % val2)
if opr == 1:
	print("The Sum of these two numbers is: "+str(sum))
elif opr == 2 :
	print("The subtraction of these two numbers is: "+ str(sub))
elif opr == 3 :
	print("The Multiplication of the numbers is: "+str(mul))
elif opr == 4 :
	print("The Division of these two numbers is: "+str(div))
elif opr == 5 :
	print("The Reminder of these two numbers is: "+str(rem))
else:
	opr  = float(input("Please Select from the given:\n 1: Sum \n 2: Subtract \n 3: Multiply \n 4: Divide \n 5: Reminder \n Enter the number of the Operation: "))
	if opr == 1:
		print("The Sum of these two numbers is: "+str(sum))
	elif opr == 2 :
		print("The subtraction of these two numbers is: "+ str(sub))
	elif opr == 3 :
		print("The Multiplication of the numbers is: "+str(mul))
	elif opr == 4 :
		print("The Division of these two numbers is: "+str(div))
	elif opr == 5 :
		print("The Reminder of these two numbers is: "+str(rem))
	else:
		print("Your are not interssted so program is exited....")