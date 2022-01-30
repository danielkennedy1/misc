#counts down from inputted value
def countdown(n):
    print(n)
    if(n > 0):
        return countdown(n-1)
    else:
        return
countdown(int(input("Countdown from ->")))