def fibonacci(number):
    try:
        val = int(number)
    except ValueError:
        print("Et heltall, prøv igjen\n")
        return None
    if val <= 0:
        print("Et positivt tall, skjerpings\n")
        return None
    else:
        fib=[0]*(val+1)
        fib[1] = 1
        for i in range(2, val+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[val]

n = input("Gi meg et nummer!:\n")
fibnum = fibonacci(n)
if fibonacci(n) == None:
    fibonacci(n)
print("Det "+ str(n) + ". fibonaccitallet er: " + str(fibnum))