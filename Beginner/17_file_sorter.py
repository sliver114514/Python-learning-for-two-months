# # 文件自动归类整理器 : 读取文件夹 -> 看后缀 -> 丢进对应名字的文件夹
# 导入操作系统接口模块：负责文件和文件夹的路径操作、判断、读取
import os
# 导入高级文件夹操作模块：主要负责“移动”文件 (shutil.move)
import shutil

def sort_file_in_directory(directory_path):
    """
    组织（整理）指定目录中的文件，根据文件类型放入子文件

    参数：
        directory_path(str): 你要整理的文件夹路径，比如“D:/下载”
    """

    # 这是一个映射表（字典）。键 (key) 是文件后缀，值 (Value) 是要放进的文件夹名。
    # 注意：这里故意都用了小写，因为你后面用 .lower() 把后缀转小写了，这样能匹配到。
    file_type_mapping = {
        ".txt": "TextFiles",
        ".docx": "Documents",
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".mp3": "Music",
        ".mp4": "Music",
        ".zip": "Archives",
        # 当然也可以添加更多，比如".py": "PythonScripts"
    }

    try:
        # 列表推导式：遍历目录下的所有东西，只挑出[文件] (忽略子文件)
        # os.path.join 用来拼接路径，解决不同系统 (Win用\.Mac用/)的差距
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    except FileNotFoundError:
        # 防呆设计：如果用户输入的路径根本不存在，直接报错返回，防止程序崩溃
        print(f"错误：找不到路径 '{directory_path}'")
        return

    # 如果没有文件.提前退出，省的做无用功
    if not files:
        print("该目录下没有需要整理的文件")
        return

    for file in files:
        # os.path.splitext("图片.jpg") 返回 ("图片"， ".jpg")
        # 这里用 file_name 接收文件名，用 file_extension 接收拓展名（包含点号）
        file_name, file_extension = os.path.splitext(file)

        # .lower() 把后缀转成小写，防止 ".JPG" 匹配不到 ".jpg"
        # .get() 方法：如果在字典里找到，就用对应的值；找不到，就返回 "Other"
        destination_folder_name = file_type_mapping.get(file_extension.lower(), "Other")

        # 拼接出目标文件夹的完整绝对路径
        destination_path = os.path.join(directory_path, destination_folder_name)

        # os.path.exists 检查路径是否存在
        # os.makedirs 可以一次性创建多级目录（这里只创建一级）
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
            print(f"创建文件夹 ‘{file}' 至 '{destination_folder_name}'")

            # 执行移动操作
            source_file_path = os.path.join(directory_path, file)
            # shutil.move 是核心动作：剪切 + 粘贴
            shutil.move(source_file_path, destination_path)
            print(f"移动文件 '{file}' 至 '{destination_folder_name}'")

        print("\n文件整理完成！")

if __name__ == "__main__":
    # 提示用户输入绝对路径，去掉收尾空格
    path_to_sort = input("请输入要整理的文件夹路径:").strip()
    # 调用上面定义的函数，开始程序
    sort_file_in_directory(path_to_sort)