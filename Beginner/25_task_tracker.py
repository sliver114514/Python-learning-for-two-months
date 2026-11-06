# # 任务追踪器
# 定义全局列表作为数据库
tasks = []

def add_task(task):
    # 将新元素添加到列表末尾
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    # 利用 Python 的”真值测试“:空列表 [] 在布尔上下文中等于 False
    # 所以 ‘if not tasks' 等价于 ’if len(tasks) == 0',写法更 Pythonic.
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")

        # enumerate(可迭代对象, start=起始数字)
        # 它会把列表里的每一项打包成一个“元组 (索引, 值)”
        # 这里 start=1，所以索引从 1 开始数（人们习惯从 1 开始）
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(index):
    try:
        # 删除指定编号
        remove_task = tasks.pop(index - 1)
        print(f"Task '{remove_task}' deleted.")
    except IndexError:
        # 如果用户输入的数字大于列表长度，pop 会抛出 IndexError
        # 比如列表只有 2 项，用户输入 3，pop(2) 会报错，这里捕获并友好提示
        print("Invalid task number.")

def main():
    while True:
        # 打印菜单
        print("\n=== Task Tracker ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        # 获取用户选项（注意：这里没有 int() 转换，直接用字符串比较）
        choice = input("Select an option (1-4):")

        # 路由分支（根据用户选择调用不同的函数）
        if choice == "1":
            task = input("Enter Task:")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            # 先展示现有任务，让用户知道有哪些可以删
            view_tasks()
            # if tasks == True
            if tasks:
                try:
                    # 注意：这里用了 int() 转换，用户输入字母会触发 ValueError
                    index = int(input("Enter task number to delete: "))
                    delete_task(index)
                except ValueError:
                    print("Please enter a valid number.")
            # 如果 tasks 为空，view_tasks 已经打印了 "No tasks found."，
            # 所以这里不需要额外处理，会自然回到主菜单。

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")

# 入口守卫（确保只有直接运行此文件时才执行 main）
if __name__ == "__main__":
    main()