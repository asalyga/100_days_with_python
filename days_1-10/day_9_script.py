import day_9_assets

print(day_9_assets.logo)


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
    print(day_9_assets.logo)

    number1 = int(input("What's the first number? :"))

    for operation in operations:
        print(operation)
    continnue = True

    while continnue:
        oper_symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        calc_function = operations[oper_symbol]
        answer = calc_function(number1, number2)

        print(f"{number1} {oper_symbol} {number2} = {answer}")
        if input(
                f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ").lower() == 'y':
            number1 = answer
        else:
            continnue = False
            calculator()


calculator()
