import random

print("This app generates password for you.")
entry = input("Enter your name all lowercase ")

name = entry.replace(" ", "")

letter1 = random.choice(name)
letter2 = random.choice(name)
letter3 = random.choice(name)

passwordnumber = random.randrange(1001, 9999, 4) 
passwordletter = (letter1 + letter2 + letter3)
print(passwordletter + str(passwordnumber))
