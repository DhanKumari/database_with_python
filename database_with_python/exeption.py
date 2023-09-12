def factorial(n):
    #n! can be n*(n-1)
    if n <=1:
        return 1
    else:
        return n *factorial(n-1)
    
try:
    print(factorial(50))
except RecursionError:
    print("this programs calculates factorial of large no.")
    

print("programs terminating ")