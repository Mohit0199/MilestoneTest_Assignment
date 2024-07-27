def addition(a, b):
    return f"Addition of {a} and {b} is {a+b}"

def substraction(a, b):
    return f"Substraction of {a} and {b} is {a-b}"

def multiplication(a, b):
    return f"Multiplication of {a} and {b} is {a*b}"

def division(a, b):
    if b==0:
        return "Can not divide by 0"
    else:
        return f"Division of {a} and {b} is {a/b}"