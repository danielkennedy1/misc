#recursive definition of fibbonacci series,
#atttempts to define up to the 200th value (won't get there)
i = 0
n = 0
def fib (n):
    if(n > 1):
        return fib(n-1) + fib(n-2)
    else:
        return n
for i in range(200):
    print("{} : {}".format(i, fib(i)))
