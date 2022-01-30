def fizzbuzz(pairs, max):
    for x in range(1, max + 1):
        msg = ""
        num = True
        for pair in pairs:
            if x % pair[0] == 0:
                msg += pair[1]
                num = False
        if num:
            msg = str(x)
        print(msg)

#Sample call
fizzbuzz([(3, "fizz"), (5, "buzz"), (7, "baz")], 105)