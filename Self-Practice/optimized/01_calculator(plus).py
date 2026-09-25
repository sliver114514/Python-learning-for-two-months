# 复刻的上面的简易版,并加入全局循环
def get_number(prompt):
    while True:
        user_input = input(prompt) # 注意！！！
        try:
            return float(user_input) # 注意！！！
        except ValueError:
            print("error")

while True:
    print("new ========")
    number1 = get_number("first number:")
    number2 = get_number("second number:")

    valid_operation = ["add", "subtract", "multiply", "divide"]
    while True:
        operation = input("choose operation: ").lower()
        if operation in valid_operation:
            break
        else:
            print("error")

    if operation == "add":
        result = number1 + number2 # 注意
    elif operation == "subtract":
        result = number1 - number2 # 注意
    elif operation == "multiply":
        result = number1 * number2 # 注意
    elif operation == "divide":
        while True:
            if number2 != 0:
                result = number1 / number2
                break
            else:
                print("error")
                number2 = get_number("second again!")

    print(f"the operation is {operation},first is {number1}, second is {number2}, and result is {result}")
    again = input( "again?(yes/no)").lower()
    if again != "yes":
        print("Bye！！！")
        break
