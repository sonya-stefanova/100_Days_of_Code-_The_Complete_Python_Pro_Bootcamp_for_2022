from ascii_calculator import logo_calculator
print("Welcome to PythoCalculator!!!\nEnjoy the easy math!")
print(logo_calculator)

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def devide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}

calculations_over = False
while not calculations_over:
    num_1 = float(input("Please, enter the first number: "))
    operation_symbol = input("Opt for an operation symbol as you need it: ")
    num_2 = float(input("Please, enter the second number: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num_1, num_2)
    print(f'{num_1}{operation_symbol}{num_2}={answer}')
    restart_option = input("Do you want to keep on calculating? Opt for yes or no.").lower()
    if restart_option == "no":
        calculations_over = True
        print("Goodbye! Thanks for experiencing the better calculations!")

