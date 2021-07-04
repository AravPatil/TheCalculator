
#Declaring Lists And Variables:-
subtraction_list = []
multiplication_list = []
print('''Hello Guys, this is Arav. This is my 1st PPP(Python Personal Projects).
So today I made a Calculator, a little bit more advanced one...
Which was Awesome.I can have future changes in this PPP:- 
Example-Adding GUI, Adding Library to make it #MoreEfficient and #LessLinesofCode''')

play_or_quit = input("Press 'p' to play and 'q' to quit The Calculator: ")

if play_or_quit == 'q' :
	print("Thanks for Having Me, have a nice day ahead,more Projects yet to come. ")
	exit()
elif play_or_quit == 'Q':
	print("You can write that in small_case -_-")
	print("Thanks for Having Me, have a nice day ahead,more Projects yet to come.")
elif play_or_quit == 'p' and 'P':
	print("Alright! Be Ready to Play!")
	input_number_of_numbers = int(input("Please Enter the Number of Numbers (Subtraction & Division only Works with two Numbers.):- "))
	print("Alright! NOW REAL GAME BEGINS:-")
	for i in range(0,input_number_of_numbers,1):
		numbers = int(input("Please Enter the Number:- "))
		#Command for Subtraction:-
		subtraction_list.append(numbers)
		multiplication_list.append(numbers)

	print("Now, the main Part, Enter the OPERATION:-")
	operation = input()

	#Addition
	addition_list = []
	if operation == '+':
		for i in range(input_number_of_numbers):
			addition_list.append(numbers)
		print("THE SUM OF TYPED NUMBER IS:",sum(addition_list))
		print("Thanks for Playing! ")

	#Subtraction
	if operation == '-':
		print("Ps:- It will only do Subtraction of First 2 Numbers Typed.")
		sub_result = subtraction_list[0] - subtraction_list[1]
		print("THE DIFFERENCE OF TYPED NUMBER IS:", sub_result)
		print("Thanks for Playing! ")
		
	#Multiplication

	if operation == '*':
		answer = multiplication_list[0]*multiplication_list[1]
		print("The Answre is:",answer)
	if operation == '/':
		answer = multiplication_list[0]/multiplication_list[1]
		answer = int(answer)
		print("The Answre is:",answer)


			

else:
	print("Please Enter a Valid key and Try Again!")
	exit()



	

