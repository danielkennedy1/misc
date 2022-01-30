#counts up to given value
def countup(i, n):
    print(i)
    if(i<n):
        return countup(i+1, n)
    else:
        return
countup(0, 5)