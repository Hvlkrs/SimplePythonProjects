#Find the Largest Number


#Unit Test 
#input1 = 1
#input2 = 2
#input3 = 3
#input4 = 4
#input5 = 5



print("Enter a 5 number and see which one is largest one!")


# I got inputs from the user with "Enter a number" message
input1 = int(input("Enter number1: "))
input2 = int(input("Enter number2: "))
input3 = int(input("Enter number3: "))
input4 = int(input("Enter number4: "))
input5 = int(input("Enter number5: "))

if (input1 >= input2) and (input1 >= input3) and (input1 >= input4) and (input1 >= input5):
   yourlargestnum = input1
elif (input2 >= input1) and (input2 >= input3) and (input2 >= input4) and (input2 >= input5):
   yourlargestnum = input2
elif (input3 >= input1) and (input3 >= input2) and (input3 >= input4) and (input3 >= input5):
   yourlargestnum = input3
elif (input4 >= input1) and (input4 >= input2) and (input4 >= input3) and (input4 >= input5):
   yourlargestnum = input4
else:
   yourlargestnum = input5



   # I printed the result
print("The largest number is that :", yourlargestnum)