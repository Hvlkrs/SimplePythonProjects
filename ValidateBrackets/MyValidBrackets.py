# isValid function
def isValid(myinput):
	stack = [] 

	for bracket in myinput:
		if bracket in ["(", "{", "["]:

			stack.append(bracket) #stack just have ( or { or [
        
		else:
            
            #If stack is not empty
			if stack:

			# To pop an item in the stack, use the stack function pop stack.pop()
			    current_bracket = stack.pop()   
			    if current_bracket == '(' and bracket != ")":
				    return False
			    if current_bracket == '{' and bracket != "}":
				    return False
			    if current_bracket == '[' and bracket != "]":
				    return False

	# Check Empty Stack
	if stack:
		return False
	return True #If stack is empty return true


print("This code is about writing a function that given a string containing just the characters (, ), {, }, [ and ], determines if the input string is valid or not!")
myinput = input("Enter a combination of brackets: ") #myinput is an array

# Main code
if __name__ == "__main__":

# Call the Function
	if isValid(myinput):
		print("Valid")
	else:
		print("Not Valid")


