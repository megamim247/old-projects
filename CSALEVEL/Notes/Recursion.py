def fibonacii(n:int):
    if n<=1:
        return n
    else:
        return fibonacii(n-1)+fibonacii(n-2)
    
print(fibonacii(4))

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

def power(N,n):
    if n==1:
        return N
    else:
        return N*power(N,n-1)

print(power(5,3))