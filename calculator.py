# Function that contain Five arthematic operator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error : Cannot Divide by Zero"
    return a/b
def avg(a,b):
    return (a+b)/2

while True:
    print("\nSelect an Operator :- ")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Average")
    print("6. Exit")

    try:
        S = int(input("Enter Your selection (1 to 6) :- "))

        if S == 6:
            print("Calculator Closed")
            break

        num1 = float(input("Enter first Number :- "))
        num2 = float(input("Enter second Number :- "))
        
        if S == 1:
            print(f"{num1} + {num2} = {add(num1,num2)}")
        
        elif S == 2:
            print(f"{num1} - {num2} = {sub(num1,num2)}")
            
        elif S == 3: 
            print(f"{num1} * {num2} = {multi(num1,num2)}")
        
        elif S == 4:
            print(f"{num1} / {num2} = {divide(num1,num2)}")
        
        elif S == 5:
            print(f"Average of {num1} and {num2} = {avg(num1,num2)}")
        
        else:
            print("Ivalid Operator")

    except ValueError:
        print("Invalid input! Please enter numbers only")