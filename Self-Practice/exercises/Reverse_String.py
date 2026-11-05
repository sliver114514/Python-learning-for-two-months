# 反转字符串
def reverse_string(text):
    return text[::-1]

def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# 程序入口：当且仅当直接运行此脚本时执行下，面代码
if __name__ == '__main__':
    print("请选择模式：")
    print("1. 字符级反转")
    print("2. 单词级反转")

    while True:
        mode = input("请输入 1 或 2：")
        if mode not in ("1", "2"):
            print("无效输入，请尝试 1 或 2")
            continue
        else:
            break
    user_text = input("请输入你要处理的文本：")
    if mode == "1":
        result = reverse_string(user_text)
        print(f"反转结果{result}")
    elif mode == "2":
        result = reverse_words(user_text)
        print(f"反转结果{result}")