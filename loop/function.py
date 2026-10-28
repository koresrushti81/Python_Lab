def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def calculator(c):
    return c(10,5)
print(calculator(add))
print(calculator(sub))
print(calculator(multi))
print(calculator(div))