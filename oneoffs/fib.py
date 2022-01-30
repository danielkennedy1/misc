fib = [1, 1]
for i in range(1, int(input("How many terms?"))):
    fib.append(fib[i] + fib[i-1])
    print(f"{i}: {fib[i + 1]}")
