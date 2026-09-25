# 1. 获取文本
text = input("Enter the text you want to encrypt: ")

# 2. 获取密码，并判断是否为空（练手必加的小细节）
password = input("Enter the password to encrypt the text: ")
if password == "":
    print("密码不能为空，程序退出！")
    exit()  # 结束程序，这个你应该学过

# 3. 加密（改动点：让密码的第一个字母参与偏移，而不是密码长度）
encrypted_text = ""
for char in text:
    # 把密码第一个字母转成数字作为偏移量（这样密码不同，结果就不同）
    shift = ord(password[0])
    encrypted_text += chr(ord(char) + shift)

print("Encrypted text:", encrypted_text)

# 4. 询问是否解密（改动点：把输入转成小写再判断）
decrypt = input("Do you want to decrypt the text? (yes/no): ")
if decrypt.lower() == "yes":  # .lower() 可以把大写变成小写，这样 YES 也能识别
    decrypted_text = ""
    for char in encrypted_text:
        shift = ord(password[0])  # 解密时用同样的偏移量减回去
        decrypted_text += chr(ord(char) - shift)

    print("Decrypted text:", decrypted_text)