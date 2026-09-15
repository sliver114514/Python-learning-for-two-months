# 简单的一次性猜数字
# 导入随机模块
import random

# 生成一个介于0到100的随机整数
random_value = random.randint(0, 100)

# 征求用户意见，并验证反馈
user_input = input("enter you guess:")
try:
    user_input = int(user_input)
    if user_input < 0 or user_input > 100:
        print("please enter a number between 0 and 100")
        exit()

except ValueError:
    print("please enter a valid number.")
    exit()

# 显示结果是否接近、匹配或不匹配
if user_input - 10 < random_value < user_input + 10:
    if user_input == random_value:
        print(f"Congratulations！ You guessed the number {user_input} correctly!")
    else:
        print(f"Close! You guessed the number {user_input}, the actual answer was {random_value}.")
else:
    print(f"Sorry, you didn't guess the number.The actual answer was {random_value}.")