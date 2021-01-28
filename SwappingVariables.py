# Swap two Variables:

a = 5
b = 6

# Method 1:
temp = a
a = b
b = temp

# Instead of wasting a variable:
#Method 2:
a = a+b
a = a-b 
a = a-b 

# Still a bit is wasted as 11 is a 4 bit numbers and 5 & 6 are 3 bit numbers:
#Method 3: use XOR to avoid this
a = a^b 
b = a^b 
a = a^b 

#Method 4: the simplest way
a,b = b,a # uses the concept of ROT_two() in python.
