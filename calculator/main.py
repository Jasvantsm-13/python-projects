
import art
#TODO write out the outer function - add, subtract, multiply, and divide
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#TODO add this 4 function in dictionary as the values. key =  "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#TODO  use the dictionary operations to perform the calculation. multiply 4 * 8 using the dictionary.
# print(operations["*"](4, 8))

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("what is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation: ")
        num2 = float(input("what is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
