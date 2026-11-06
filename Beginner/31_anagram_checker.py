# 变位词检查器
def check_anagram(str1, str2):
    """
    检查两个字符串是否互为变位词(Anagram)
    变位词定义：通过重新排列一个单词或短语的字母，形成另一个单词或短语
    （；例如"listen"->"silent"）
    """
    # 清洗：将获取到的字符串拆分再重组成字符串，并全部转为小写
    cleaned_str1 = "".join(str1.split()).lower()
    cleaned_str2 = "".join(str2.split()).lower()

    # 简单检验长度是否相等，若长度不相等，则一定不是变位词
    if len(cleaned_str1) != len(cleaned_str2):
        return False

    # - sorted() 返回一个新的列表，原字符串不变
    return sorted(cleaned_str1) == sorted(cleaned_str2)

def main():
    print("=== Anagram Checker ===")

    input_str1 = input("Enter the first word or phrase:")
    input_str2 = input("Enter the second word or phrase:")

    is_anagram = check_anagram(input_str1, input_str2)

    if is_anagram:
        print(f"\nYes! '{input_str1}' and '{input_str2}' are anagram of each other.")
    else:
        print(f"\nNO. '{input_str1}' and '{input_str2}' are not anagram.")

if __name__ == "__main__":
    main()