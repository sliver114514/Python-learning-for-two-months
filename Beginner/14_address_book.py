# 通讯录
import json # 把字典变成文字(存硬盘)，再把文字变回变回字典(读取内存)的进度
import os # 操作系统工具箱

# 设定一个常量:我们存通讯录的文件名
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """
    从硬盘上的JSON文件读取通讯录数据
    如果文件不存在，就返回一个空字典(代表没有联系人)
    """
    # os.path.exists (文件名) 会返回 True (存在)或(不存在)
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            # json.load 把文件里的文字内容转换成 Python 字典
            return json.load(f)
        # 如果文件不存在，直接返回一个空字典 {}
    return {}

def save_contacts(contacts):
    """
    把内存里的通讯录字典，存到硬盘的JSON文件里
    """
    # w 是写，若文件不存在，python 会创建一个;若存在，则覆盖旧内容
    with open(CONTACTS_FILE, "w") as f:
        # json.dump 把字典转换成 JSON 格式，并写入文件
        # indent=4 让文件里的内容缩进 4 个空格，方便看
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    """
    让用户输入姓名、电话、邮箱、然后添加到通讯录字典中
    """
    # 获取用户输入
    name = input("Enter name:")
    phone = input("Enter phone number:")
    email = input("Enter email address:")

    # 把 “姓名” 作为键(key),存入一个包含电话和邮箱的小字典作为值(Value)
    contacts[name] = {"phone": phone, "email": email}

    # 修改了数据，立刻存盘，数据就不会丢
    save_contacts(contacts)
    print(f"Contact '{name}' added")

def view_contacts(contacts):
    """
    打印出所有联系人信息
    """
    # 如果字典是空的 (即 if not contacts 为 True),就提示并返回
    if not contacts:
        print("No contacts found")
        return # 直接结束这个函数

    # contacts.items() 会把字典拆成一对一对的 (键，对)
    # name 是姓名， info 是包含电话和邮箱的小字典
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def delete_contact(contacts):
    """
    让用户输入姓名，从通讯录中删除该联系人
    """
    name = input("Enter the name of the contact to delete:")

    # 检查这个姓名是否在字典得到键(key)里面
    if name in contacts:
        # del 命令可以从字典中移除指定的键值对
        del contacts[name]
        # 修改了数据，立刻存盘
        save_contacts(contacts)
        print(f"Contact '{name}' deleted")
    else:
        print(f"Contact '{name}' not found")

def main():
    """
    主程序入口: 加载数据，显示菜单，并循环让用户操作
    """
    # 程序一启动，先把硬盘里的通讯录读到内存里
    contacts = load_contacts()

    # 无限循环，除非用户选择退出 (break)
    while True:
        # 打印操作菜单
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        # 获取用户输入的选项 (注意 input 返回的是字符串)
        choice = input("Enter your choice:")

        # 根据用户输入，调用不同的功能函数
        if choice == "1":
            add_contact(contacts) # 添加
        elif choice == "2":
            view_contacts(contacts) # 查看
        elif choice == "3":
            delete_contact(contacts) # 删除
        elif choice == "4":
            break # 退出循环，程序结束
        else:
            # 输入 1-4 以外的内容，提示错误，循环继续
            print("Invalid choice.Please try again.")

# 这是 Python 的"入口守卫”
# 意思是: 如果我是直接被运行的程序 (而不是被别人导入)，就执行 main()
# 实在无法理解就在每个项目的结尾都加上就行了
if __name__ == "__main__":
    main()