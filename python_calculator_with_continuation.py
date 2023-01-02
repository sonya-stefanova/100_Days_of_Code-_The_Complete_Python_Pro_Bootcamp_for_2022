from ascii_calculator import logo_calculator


def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    if n2==0:
        return f"Error. You cant divide by 0."
    else:
        return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print("Welcome to PythoCalculator!!!\nEnjoy the easy math!")
    print(logo_calculator)

    num_1 = float(input("Please, enter an input number: "))

    continue_calculation = True
    while continue_calculation:
        operation_symbol = input("Opt for an operation symbol as you need it: ")
        num_2 = float(input("Please, enter the next number: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_1, num_2)
        print(f'{num_1}{operation_symbol}{num_2}={answer}')
        restart_option = input("Do you want to keep on calculating? Opt for 'y' or 'n'.").lower()
        if restart_option == "y":
            num_1 = answer
        else:
            continue_calculation = False
            print("Goodbye! Thanks for experiencing the better calculations!")
            calculator()


calculator()