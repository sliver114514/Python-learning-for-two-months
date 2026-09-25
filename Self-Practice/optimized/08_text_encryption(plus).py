# 古典凯撒密码加密
# 获取文本
text = input("Enter the text you want to encrypt:")

# 获取密码，并判断是否为空(练手必加的小细节)
password = input("Enter the password to encrypt the text:")
if password == "":
    print("The password must not be empty, and the program will exit!")
    exit() # 结束程序

# 加密，让密码的第一个字母参与偏移量，而不是密码长度
encrypted_text = ""
# 凯撒密码与维吉尼亚密码二选一，此为前者
# for char in text:
#     # 把密码第一个字母转成数字作为偏移量
#     shift = ord(password[0])
#     encrypted_text += chr(ord(char) + shift)
# 后者
for i in range(len(text)):
    shift = ord(password[i % len(password)])
    encrypted_text += chr(ord(text[i]) + shift)

print(f"The encrypted text is: {encrypted_text}")

# 询问是否解密
decrypt = input("Do you want to decrypt the text?(yes/no):)")
if decrypt.lower() == "yes":
    decrypted_text = ""
    for char in encrypted_text:
        shift = ord(password[0]) # 解密时用同样的偏移量减回去
        decrypted_text += chr(ord(char) - shift)

    print(f"The encrypted text is: {decrypted_text}")