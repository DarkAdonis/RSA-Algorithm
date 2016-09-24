
import math

def rsa(e, n):
    

    #find phi,
    prime1 = 0
    prime2 = 0
    primeFactors = primes(n)

    N   = primeFactors[0]*primeFactors[1]
    phi = (primeFactors[0]-1)*(primeFactors[1]-1)

    print (primeFactors)
    print (N)
    print (phi)

    d = 0
    possibleDs = []
    for i in range(0,phi):
        if ((i*e)%phi==1):
            d = i
            print((i*e))
            possibleDs.append(d)

    print("public key:")
    print([e,n])
    print("private key:")
    print([d,n])

    print("possible Ds")
    print(possibleDs)

    toDecrypt = [29314,28845,229545]

    for i in range(0,len(toDecrypt)):
        temp = (str)((toDecrypt[i]**d)%n)
        messageTemp = ''
        for j in range(0, len(temp)):
            messageTemp += encr((int)(temp[j:j+1]))
        print(messageTemp)

def encr(number):
    if(number==5):
        return 'A'
    elif(number==3):
        return 'D'
    elif(number==4):
        return 'E'
    elif(number==9):
        return '0'
    elif(number==1):
        return 'S'
    elif(number==7):
        return 'T'
    elif(number==6):
        return 'U'
    elif(number==8):
        return 'W'
    elif(number==2):
        return 'Y'

def isPrime(n):
    sqrtN = (int)(n**0.5)
    for i in range(2,sqrtN):
        if(n%i==0):
            return False
    return True

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
rsa(17,329467)
