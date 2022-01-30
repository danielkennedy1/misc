#Recursively multiplies two numbers
x = int(input("1st number"))
y = int(input("2nd number"))
def multi(a, b):
    if(b != 1):
        return a + multi(a, b-1)
    else:
        return a
print(multi(x, y))