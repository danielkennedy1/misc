checkprime = lambda x : prime(x, x)
def prime(n, a):
    if(a==n):
        return prime(n-1, a)
    elif(n > 0 and a % n != 0):
        return prime(n-1, a)
    elif(n == 1):
        return True
    elif(a % n == 0):
        return False
while(True):
    print(checkprime(int(input("Type number-"))))