# 投骰子模拟器
import random

def roll_dice(num_dice):
    """扔骰子，返回列表总和(用列表推导精简)"""
    # 随机取(bum_dice)次值放到 rolls 里
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    # 封装打包返回总值
    return rolls, sum(rolls)

def main():
    print("--- 骰子模拟器 ---")
    while True:
        user_input = input("想扔几个骰子？(输入 q 退出):")
        if user_input.lower() == "q":
            print("拜拜!")
            break

        try:
            num_dice = int(user_input)
            if num_dice <= 0:
                print("请输入正数！")
                continue

            # 接住上面的return，total = sum(rolls)
            rolls, total = roll_dice(num_dice)
            print(f"\n扔了{num_dice}个骰子:")
            print(f"点数明细: {rolls}")
            print(f"总和: {total}")

        except ValueError:
            print("无效输入，请输入数字或q")

if __name__ == "__main__":
    main()