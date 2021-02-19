'''Generate a 3x3 matrix with 9 random prime numbers.
Use for loop!'''

import random

'''CODE-PART1:
To prepare a list of prime numbers.'''

# IMPORTANT NOTE:
# This code is designed to work only for the range of 0-667
# which is until 667 = 23 * 29
# since this code is prepared manually dividing given numbers 
# by first prime numbers in 0-20 range.

# (SUGGESTED VALUES:)
# (minpPrime: 0)
# (maxPrime: 667)

'''It is decided for prime numbers to be in the range of 0-100.'''

# So minPrime and maxPrime are not required.

#minPrime = int(input("Enter a value you want to start for prime numbers: "))
#if minPrime < 0:
#    print("NEGATIVE VALUE! Try again!")

#maxPrime = int(input("Enter a value as your maximum limit for prime numbers: "))
#if maxPrime < 0:
#    print("NEGATIVE VALUE! Try again!")
#elif maxPrime < minPrime:
#    print("Oops! Think bigger! (at least bigger than the first value you entered)")

primelist = []

for i in range(0, 100): #for i in range(minPrime, maxPrime):
    if i == 0 or i == 1:
        continue
    if i%2 == 0:
        if 2 in range(0, 100) and i == 2: # range(minPrime, maxPrime)
            primelist.append(2)
        continue
    elif i%3 == 0:
        if 3 in range(0, 100) and i == 3: # range(minPrime, maxPrime)
            primelist.append(3)
        continue
    elif i%5 == 0:
        if 5 in range(0, 100) and i == 5: # range(minPrime, maxPrime)
            primelist.append(5)
        continue
    elif i%7 == 0:
        if 7 in range(0, 100) and i == 7: # range(minPrime, maxPrime)
            primelist.append(7)
        continue
#    elif i%11 == 0:
#        if 11 in range(minPrime, maxPrime) and i == 11:
#            primelist.append(11)
#        continue
#    elif i%13 == 0:
#        if 13 in range(minPrime, maxPrime) and i == 13:
#            primelist.append(13)
#        continue
#    elif i%17 == 0:
#        if 17 in range(minPrime, maxPrime) and i == 17:
#            primelist.append(17)
#        continue
#    elif i%19 == 0:
#        if 19 in range(minPrime, maxPrime) and i == 19:
#            primelist.append(19)
#        continue
    else:
        primelist.append(i)

#print(primelist) # to check if the list is working / inactivate later

'''CODE-PART2:
To create the matrix by random numbers from primelist.'''



# If it is wanted to ask rowsxcolumns of matrix;

#m = int(input("How many rows would you like in your matrix?: "))
#n = int(input("How many columns would you like in your matrix?: "))

#k = m * n
#l = 0
#matlist = []

#while l != k:
#    matlist.append(random.choice(primelist))
#    l += 1

matlist = []

# since 3x3 matrix will have 9 elements
# while will iterate for 9 times 
i = 0
while i in range(9):
    matlist.append(random.choice(primelist))
    i += 1

#print(matlist) # to check if the list is working / inactivate later

pri_mat = [[0,0,0],
          [0,0,0,],
          [0,0,0]]

k = 0
for i in range(3):
    for j in range(3):
        pri_mat[i][j] = matlist[k]
        k += 1

print(pri_mat)

#print(type(pri_mat)) 

# I could not find a way to make the type matrix,
# without using numpy.
