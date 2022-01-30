#returns a^b
def power(a, b):
    if(b != 1):
        return a * power(a, b-1)
    else:
        return a
print(power(3, 78))