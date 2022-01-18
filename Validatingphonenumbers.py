#Input Format:
# The first line contains an integer N, the number of inputs.
# N lines follow, each containing some string.

# Output Format:
# For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.


# Code:
N=int(input())
lst=[]
for i in range(N):
    lst.append(input())

for i in range(N):
    if len(lst[i])==10 and lst[i].isnumeric()==True:
        if (lst[i][0]=='7' or lst[i][0]=='8' or lst[i][0]=='9'):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
