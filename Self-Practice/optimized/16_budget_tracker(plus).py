# # 进阶版账单
import json
import os
from datetime import datetime # 用于给每笔账打时间戳

# 常量：数据文件名 (写死在顶部，方便以后更改)
BUDGET_FILE = "budget.json"

def clear_screen():
    """
    清空终端屏幕，让菜单每次都显示在顶部
    """
    # Windows 是 cls,Mac/Linux 是 clear
    os.system('cls' if os.name == 'nt' else 'clear')

def safe_load_json():
    """
    安全加载 JSON 文件
    如果文件不存在 -> 返回初始空模板
    如果文件损坏/格式错误 -> 备份坏文件，重建空模板(绝不崩)
    """
    if not os.path.isfile(BUDGET_FILE):
        return {"income": [], "expense": []}

    try:
        with open(BUDGET_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # 防御性检查：确保加载进来的数据有我们需要的两个键0
            if not isinstance(data, dict) or "income" not in data or "expense" not in data:
                raise ValueError("数据格式不对，缺少 income 或 expenses 键")
            return data
    except (json.JSONDecodeError, ValueError) as e:
        # 文件坏了就把坏文件重新命名备份，防止用户数据彻底丢失
        backup_name = f"budget_corrupted_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        os.rename(BUDGET_FILE, backup_name)
        print(f"原数据文件损坏，已自动备份为：{backup_name}")
        print("已建立新的空帐本")
        return {"income": [], "expense": []}

def save_data(data):
    """
    将内存中的数据序列化为 JSON 存到硬盘
    indent=4 让生成的文件有缩进，方便人们直接打开阅读
    """
    with open(BUDGET_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_positive_float(prompt):
    """
    专门用来获取金额的输入函数。
    只要用户不输入有效的正数，就永远循环问，直到输入正确。
    这比原代码的 try/except 只问一次要健壮得多。
    """
    while True:
        user_input = input(prompt)
        try:
            amount = float(user_input)
            if amount <= 0:
                print("金额必须大于零，请重新输入")
                continue
            return amount
        except ValueError:
            print("请输入有效的数字(列如：12.5)")

def get_non_empty_string(prompt):
    """
    专门获取描述信息，禁止用户直接敲回车输入空字符串。
    strip() 去掉首尾空格，防止用户输入一堆空格糊弄。
    """
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            print("描述不能为空，请重新输入")
            continue
        return user_input

def add_transaction(data, transaction_type):
    """
    新增一笔收入或支出。
    参数 transaction_type 只能是 "income" 或 "expenses"。
    自动添加当前时间戳。
    """
    print(f"\n---添加 {transaction_type.capitalize()}---")
    amount = get_positive_float("输入金额：")
    description = get_non_empty_string("请输入描述：")

    # 构造一条完整的记录：金额、描述、时间
    record = {
        "amount": amount,
        "description": description,
        "date" : datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    }
    data[transaction_type].append(record)
    save_data(data)
    print(f"{transaction_type.capitalize()} 已添加")
    input("按回车继续...")

def view_transactions(data):
    """
    打印所有收支记录。
    每条记录前显示一个序号（索引），方便用户后续按序号删除。
    """
    clear_screen()  # 先清屏，让列表干净显示
    print(f"\n {'=' * 10} 收入记录 {'=' * 10}")
    if not data["income"]:
        print("(暂无收入)")
    else:
        for idx, item in enumerate(data["income"]):
            # idx 从 0 开始，显示的时候 +1 更符合人们习惯
            print(f" [{idx + 1}] ${item['amount']:.2f} | {item['description']} | {item['date']}")

    print(f"\n {'=' * 10} 支出记录 {'=' * 10}")
    if not data["expense"]:
       print("(暂无支出)")
    else:
        for idx, item in enumerate(data["expense"]):
            print(f" [{idx + 1}] ${item['amount']:.2f} | {item['description']} | {item['date']}")

    print("\n" + "-" * 40)
    input("按回车键返回菜单...")

def delete_transaction(data):
    """
    按索引删除记录。用户先选要删收入还是支出，再选序号。
    原代码没有这个功能，现在补上，否则输错账只能删文件。
    """
    clear_screen()
    print("1. 删除收入")
    print("2. 删除支出")
    choice = input("请选择要删除的类型")

    if choice == "1":
        key = "income"
        label = "收入"
    elif choice == "2":
        key = "expense"
        label ="支出"
        return
    else:
        print("无效选择")
        input("按回车键继续...")

    if not data[key]:
        print(f" 当前没有 {label} 记录可删除")
        input("按回车键继续")
        return

    # 打印当前列表让用户看
    print(f"\n--- 当前 {label} 列表 ---")
    for idx, item in enumerate(data[key]):
        print(f"[{idx + 1}] ${item['amount']:.2f} | {item['description']} | {item['date']}")

    try:
        del_idx = int(input("请输入要删除的序号: ")) - 1
        if del_idx < 0 or del_idx >= len(data[key]):
            print("序号超出范围")
        else:
            delete_item = data[key].pop(del_idx)
            save_data(data)
            print(f"已删除：{delete_item['description']} (${delete_item['amount']:.2f})")
    except ValueError:
        print("请输入有效的数字序号")

    input("按回车键继续...")

def calculate_balance(data):
    """
    计算总余额，并显示总收入与总支出。
    使用生成器表达式 sum(...)，既简洁又高效。
    """
    clear_screen()
    total_income = sum(item['amount'] for item in data["income"])
    total_expenses = sum(item['amount'] for item in data["expense"])
    balance = total_income - total_expenses

    print(f"\n{'=' * 10} 财务汇总 {'=' * 10}")
    print(f"  总收入：  $ {total_income:>10.2f}")
    print(f"  总支出：  $ {total_expenses:>10.2f}")
    print(f"  {'-' * 20}")
    print(f"  结余：    $ { balance:>10.2f}")
    print("=" * 32)
    input("按回车键返回菜单...")

def main():
    """
    程序主循环。
    加载数据 → 进入无限菜单 → 用户选择对应操作。
    只有选 6. 退出 才会 break 跳出循环，结束程序。
    """
    data = safe_load_json()  # 这一步已经保证了 data 一定是个合法字典

    while True:
        clear_screen()
        print("\n       个人预算追追踪器")
        print("  ————————————————————————")
        print("  1.添加收入")
        print("  2.添加支出")
        print("  3.查看所有流水")
        print("  4.查看汇总余额")
        print("  5.删除某条记录")
        print("  6.退出程序")
        print("  ————————————————————————")

        choice = input("  请选择操作：")

        if choice == "1":
            add_transaction(data, "income")
        elif choice == "2":
            add_transaction(data, "expense")
        elif choice == "3":
            view_transactions(data)
        elif choice == "4":
            calculate_balance(data)
        elif choice == "5":
            delete_transaction(data)
        elif choice == "6":
            print("账本已保存，再见！")
            break  # 退出 while 循环，程序自然结束
        else:
            print("无效选项，请输入 1-6")
            input("按回车键继续...")

# 只有直接运行此脚本时才执行 main()，被其他文件导入时不执行
if __name__ == "__main__":
    main()