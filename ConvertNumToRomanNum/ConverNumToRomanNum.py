ConverNumToRomanNum
#  Function to change number with Roman system
# Firstly i defined a function with the def keyword. The function name is followed by parameter in (). And in this example mine is num

def Romansystem(num):
  
    # i for ones like 3-6, x for tens like 23-35, c for hundreds like 107-564, m for thousands like 1400-6798
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  
    # Converting numbers to roman number. 23 % 10 is 3, 23//10 is dividing and result is 2
    # 23 % 10 is 3, 23//10 is dividing and result is 2. For 2 it goes to x's 2 on the row and for 3 it goes to i's 3 on the row.
    # Dont be confused [] means array and arrays start with 0,1,2,3...

    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
    # Here we sum all digits for example 32; tens:3 ones:2
    a = (thousands + hundreds +
           tens + ones)
    #Why we use return here; best explain is that if your wife says you buy a Wine. We went to store and bought a wine.
    #But in the we have to go home(return), if we do not return she can not have the wine.
    return a
  

#We can use an if __name__ == "__main__" block to allow or prevent parts of code from being run when the modules are imported. 

if __name__ == "__main__":
   # I used three commented lines below for testing, it is Unit Test(developers do it to see their code is working) I used 1 to test my code
   # num = 1
   # x = int(num)
   # print(Romansystem(x))
   # I got input from the user with "Enter a number" message
    user_input = int(input("Enter a number: "))
   # I printed the result
    print("".join([a for a in Romansystem(user_input)]))