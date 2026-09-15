# 检查是否为回文字符串
word = input("What is the word you want to check?:").lower()

if word in word[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")