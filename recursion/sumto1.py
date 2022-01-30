#works backwards from given value, adding up sum of natural numbers to inputted value
#does the same thing as sum.py, but works backwards
t = 0
def sum(x):
    global t
    t += x
    if(x > 0):
        return sum(x-1)
    else:
        return t
print(sum(int(input("type number-"))))
