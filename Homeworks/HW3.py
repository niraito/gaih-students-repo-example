'''Two functions.
1. prime_first: press prime numbers between 0-500.
2. prime_second: press prime numbers between 500-1000.
Use these functions in for loop.'''

def prime_first():
    primelist1 = []
    
    for i in range(0, 500): 
        if i == 0 or i == 1:
            continue
        if i%2 == 0:
            if 2 in range(0, 500) and i == 2: 
                primelist1.append(2)
            continue
        elif i%3 == 0:
            if 3 in range(0, 500) and i == 3: 
                primelist1.append(3)
            continue
        elif i%5 == 0:
            if 5 in range(0, 500) and i == 5: 
                primelist1.append(5)
            continue
        elif i%7 == 0:
            if 7 in range(0, 500) and i == 7: 
                primelist1.append(7)
            continue
        elif i%11 == 0:
            if 11 in range(0, 500) and i == 11:
                primelist1.append(11)
            continue
        elif i%13 == 0:
            if 13 in range(500, 1000) and i == 13:
                primelist1.append(13)
            continue
        elif i%17 == 0:
            if 17 in range(500, 1000) and i == 17:
                primelist1.append(17)
            continue
        else:
            primelist1.append(i)
    
    print(primelist1) # to check if the list is working / inactivate


def prime_second():
    primelist2 = []
    
    for i in range(500, 1000): #for i in range(minPrime, maxPrime):
        if i%2 == 0:
            if 2 in range(0, 500) and i == 2: # range(minPrime, maxPrime)
                primelist1.append(2)
            continue
        elif i%3 == 0:
            if 3 in range(0, 500) and i == 3: # range(minPrime, maxPrime)
                primelist1.append(3)
            continue
        elif i%5 == 0:
            if 5 in range(0, 500) and i == 5: # range(minPrime, maxPrime)
                primelist1.append(5)
            continue
        elif i%7 == 0:
            if 7 in range(0, 500) and i == 7: # range(minPrime, maxPrime)
                primelist1.append(7)
            continue
        elif i%11 == 0:
            if 11 in range(0, 500) and i == 11:
                primelist1.append(11)
            continue
        elif i%13 == 0:
            if 13 in range(500, 1000) and i == 13:
                primelist2.append(13)
            continue
        elif i%17 == 0:
            if 17 in range(500, 1000) and i == 17:
                primelist2.append(17)
            continue
        elif i%19 == 0:
            if 19 in range(500, 1000) and i == 19:
                primelist2.append(19)
            continue
        elif i%23 == 0:
            if 23 in range(500, 1000) and i == 23:
                primelist2.append(23)
            continue
        elif i%29 == 0:
            if 29 in range(500, 1000) and i == 29:
                primelist2.append(19)
            continue
        elif i%31 == 0:
            if 31 in range(500, 1000) and i == 31:
                primelist2.append(31)
            continue
        else:
            primelist2.append(i)
    
    print(primelist2) # to check if the list is working / inactivate    

    
for i in range(1000+1):
    if i in range(500):
        prime_first(i)
    else:
        prime_second(i)
