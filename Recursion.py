def show(n):
    if n == 0: # base case where to stop recursion
        return 0
    else:
        print(n)
        show(n - 1)

show(9)

# WA recursive function to calculate factorial of no
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return  n * factorial(n - 1)

print("Factorial :", factorial(5))

# WA recursive function to calculate sum of first n natural no
def cal_sum(n):
    if n == 0:
        return 0
    else:
        return n + cal_sum(n - 1)
    
print("Sum :", cal_sum(10))

#WA recursive function to calculate nth fibonacci no
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

