# 随机密码生成器
import string
import random

# 定义字符集
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_letters = letters + digits + symbols

# 获取密码长度并验证
length = input("Enter the length of password: ")
try:
    length = int(length)
    if length < 8 or length > 128:
        print("Invalid length, please enter a number between 8 and 128")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()

# 生成密码
password = ""

for i in range(length):
    password += random.choice(all_letters)

# 打印密码
print(f"Your password is: {password}")