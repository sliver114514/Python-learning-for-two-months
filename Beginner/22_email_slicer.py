# 邮箱地址拆分器
while True:
    # 获取用户输入值，并 strip() 去掉头尾空格
    email = input("What is your email address?: ").strip()

    # 核心判断: 这 3 个条件必须都同时成立
    # @ 必须在其中，但不在开头和结尾
    if '@' in email and email.index('@') != 0 and email.index('@') != len(email) - 1:
        break
    else:
        print("Invalid input,please include an '@' sign with text before and after it.")

# 获取 @ 的左边
user_name = email[:email.index('@')]

# 获取 @ 的右边
domain_name = email[email.index("@") + 1:]

# 总结结果
output = f"Your username is '{user_name}' and your domain name is '{domain_name}'"

#展示总结
print(output)