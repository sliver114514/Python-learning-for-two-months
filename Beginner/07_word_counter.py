# 读取文本
import re
file_path = input("Enter file path: (TXT): ")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    # 路径不对或文件没放对位置
    print(f"Error: The file '{file_path}' was not found. Please check the path.")
    exit()
except PermissionError:
    # 文件被其他程序打开或没有读取权限
    print(f"Error: Permission denied to read '{file_path}'.")
    exit()
except UnicodeDecodeError:
    # 文件不是UTF-8编码
    print(f"Error: Unable to decode the file. Please ensure it's a UTF-8 encoded file.")
    exit()
except Exception as e:
    # 捕获其它异常
    print(f"An unexpected error occurred: {e}")
    exit()

# 若为英文，则使用下面的
words_list = content.split()
word_count = len(words_list)

# 若为中文，则使用下面的
# words_list = re.findall(r"[A-Za-z]+[\u4e00-\u9fff]", content)
# word_count = len(words_list)

print(f"The file contains {word_count} words.")

# 显示前十个
print(f"Preview: {words_list[:10]}")
