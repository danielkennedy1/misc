#returns a string backwards using recursion
string = input("String to be reversed - ")
reversed = ""
def reverse(x, y = 1):
    global reversed
    if y <= len(x):
        reversed += x[-y]
        return reverse(x, y+1)
    else:
        return reversed
print(reverse(string))