# 验证输入值，并计算，简单的计算机,实验一
def get_number(prompt):
    while True:
        # 获取输入值
        user_input = input(prompt)
        # 使用 try 来捕捉浮点转换过程中的错误
        try:
            return float(user_input) # 试着把输入值转换成浮点值
        except ValueError:
            print("Invalid input, Please enter a valid number.")

# 获取并验证用户输入的第一和的第二个数
number1 = get_number("Please enter the first number:")
number2 = get_number("Please enter the second number:")

# 列出有效的操作
valid_operations = ["add", "subtract", "multiply", "divide"]
while True:
    # 获取用户的操作输入值
    operation = input("Please choose an operation (add , subtract , multiply , divide): ):").lower()
    # 检查操作是否有效
    if operation in valid_operations:
        break
    else:
        # 无效错误操作
        print("Invalid operation. Please choose one of the following: add, subtract, multiply, divide.")

# 使用 if 检查执行的操作并保存以备后用
if operation == "add":
    result = number1 + number2
elif operation == "subtract":
    result = number1 - number2
elif operation == "multiply":
    result = number1 * number2
elif operation == "divide":
    # 解决除零的操作
    while True: # 若被除数为零，则重新输入第二个数
        if number2 != 0:
            result = number1 / number2
            break
        else:
            print("undefined (cannot divide by zero)")
            number2 = get_number("Please enter the second number:")

# 展示结果
print(f"The result of {operation}ing is {number1} and {number2} is {result}")