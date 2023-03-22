# from art import logo

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1 - n2
                
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-" : subtract,
    "*": multiply,
    "/" : divide
}
def calculation():
    num1 = int(input("what is the first number?: "))


    for symbol in operation:
        print(symbol)

    should_continue = True
    while should_continue:
            
        operation_symbol = input("pick an operation from the line above: ")
        num2 = int(input("what is the second number?: "))
        calc_function = operation[operation_symbol]

        first_answer = calc_function(num1, num2)
        # answer = num1, operation_symbol, num2
        print(f"{num1} {operation} {num2} = {first_answer}")

        if input(f"Type 'y' to continue calculating with {first_answer} or Type 'n' to exit: ")=="y":
            num1 = first_answer
        else:
            should_continue = False
            calculation()
calculation()



        # operation_symbol = input("pick an operation from the line above: ")
        # num3 = int(input("what is the second number?: "))
        # calc_function = operation[operation_symbol]

        # second_answer =calc_function( calc_function(num1, num2), num3)
        # # answer = num1, operation_symbol, num2
        # print(f"{first_answer} {operation} {num3} = {second_answer}")

