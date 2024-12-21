def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        print("DIV is not possible")
    return a / b
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
pi = 3.14
