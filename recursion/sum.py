#returns sum up to input i.e. n + (n-1) + (n-2) ... + 1)
t = 0
def sum(x):
    global t
    t += x
    if(x > 0):
        return sum(x-1)
    else:
        return t
print(sum(int(input("type number-"))))