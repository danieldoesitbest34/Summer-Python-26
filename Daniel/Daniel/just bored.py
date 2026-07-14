def multiplication(x, y):
    total = 0
    total = x * y
    return total

def subtraction(x,y):
    total = 0
    total = x - y
    return total

def addition(x,y):
    total = 0
    total = x + y
    return total

def divison(x, y):
    total = 0
    total = x / y
    return total


def main():
    print("-------Calcuator.-------")


    x = int(input("What is your x value?"))
    y = int(input("What is your y value?"))


    operation = input("What order of operation do you want to do?")
    if operation == "+":
        print(addition(x,y))

    elif operation == "-":
        print(subtraction(x,y))
    
    elif operation == "/":
        print(divison(x,y))

    elif operation == "*":
        print(multiplication(x,y))

main()





    

    
    