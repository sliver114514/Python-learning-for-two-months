# 更安全版的随机密码生成器，防黑客
import string
import secrets

# 定义字符集
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_characters = letters + digits + symbols

# 获取并验证长度
length = input("Enter the length of the password (8-128).")
try:
    length = int(length)
    if not (8 <= length <= 128 ):
        print("Please enter a length between 8 to 128.")
        exit()
except ValueError:
    print("Please enter a valid length.")
    exit()

# 进阶核心逻辑：使用secrets.SystemRandom()生成加密级随机数
rng = secrets.SystemRandom()

# 强制从每个类别中至少挑选一个(保证密码强度)
password_list = [
    rng.choice(letters), # 只少一个字母
    rng.choice(digits), # 至少一个数字
    rng.choice(symbols) # 至少一个符号
]

# 剩余的字符位(总长 - 3)从所有字符中随机补充
for _ in range(length - 3):
    password_list.append(rng.choice(all_characters))

# 彻底打乱顺序，防止前三位固定为"字母+数字+符号"的规律
rng.shuffle(password_list)

# 拼接并输出最终密码
final_password = ''.join(password_list)
print(f"Your secure password is: {final_password}")