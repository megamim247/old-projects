#factorial
#power
#fibonacuii
def factorial(Number:int):
    if Number!=0:
        return Number*factorial(Number-1)
    else:
        return 1
print(factorial(4))

def power(Number:int,Power:int):
    if Power!=0:
        return Number*power(Number,Power-1)
    else:
        return 1

print(power(5,3))

def fibonaucii(Number:int):
    if Number>=2:
        return fibonaucii(Number-1)+fibonaucii(Number-2)
    else:
        return 1

print(fibonaucii(5))