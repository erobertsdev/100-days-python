def format_name(f_name, l_name):
    # docstring
    """Capitalizes first letter of provided inputs"""
    if not f_name or not l_name:
        return "You provided garbage inputs that won't work sorrryyyyyyyy"
    return f"Name: {f_name.title()} {l_name.title()}"


# print(format_name(input("Enter first name: "), input("Enter last name: ")))

# Calculator project
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the options above: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start again: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()