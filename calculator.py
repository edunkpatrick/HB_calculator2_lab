"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

#repeat forever:
while True:
    # read input
    input_string = input("Calculate>> ")
    # tokenize input
    tokens = input_string.split(' ')

    operator = tokens[0]
    # num1 = float(tokens[1])
    # num2 = float(tokens[2])    
    

    if operator == "q":
        break

    # else:
    # #         (decide which math function to call based on first token)
    # #         if the first token is 'pow':
    # #               call the power function with the other two tokens

    # #         (...etc.)

    if tokens[0] =='+':
        print(add(float(tokens[1]), float(tokens[2])))
    
    #call the add function with the other two tokens

    #if the first token is 'subtract':
    if tokens[0] == "-":
        print(subtract(float(tokens[1]), float(tokens[2])))
        #call the subtract function with the other two tokens

    #if the first token is 'multiply':
        #call the multiply function with the other two tokens
    if tokens[0] == "*":
        print(multiply(float(tokens[1]), float(tokens[2])))


    #if the first token is 'divide':
        #call the divide function with the other two tokens
    if tokens[0] == "/":
        print(divide(float(tokens[1]), float(tokens[2])))

    #if the first token is 'square':
        #call the square function with the other two tokens
    if tokens[0] == "square":
        print(square(float(tokens[1])))

    #if the first token is 'cube':
        #call the cube function with the other two tokens
    if tokens[0] == "cube":
        print(cube(float(tokens[1])))

    #if the first token is 'power':
    #call the power function with the other two tokens
    if tokens[0] == "pow":
        print(power(float(tokens[1]), float(tokens[2])))

    #if the first token is 'mod':
        #call the mod function with the other two tokens
    if tokens[0] == "mod":
        print(mod(float(tokens[1]), float(tokens[2])))
