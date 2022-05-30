# python program to convert milliseconds to hour, minutes and seconds
# Get input from user
time = int(input("Input time in milliseconds: "))
# Unit Test to see printing, print(time) shows us we can get the input
# print(time)

#I found this function on a web page
# convert seconds to day, hour, minutes and seconds // means dividing * means multiple
# milliseconds = time
# hour = time // (24 * 3600)
# minute = time // 3600
# second = time // 60
# milliseconds = time

# I wrote this function myself to based on this: 1hour=60minutes=60x60seconds=3600seconds=3600x1000milliseconds=3.600.000milliseconds
milliseconds = time
second = milliseconds // 1000
minute = second // 60
hour = minute // 60

# print hour, minutes, seconds and milliseconds
print('Milliseconds', milliseconds)
print('Seconds', second)
print('Minutes', minute)
print('Hours', hour)

#Output will be 
# Input time in milliseconds: 3600000
# Milliseconds 3600000
# Seconds 3600
# Minutes 60
# Hours 1