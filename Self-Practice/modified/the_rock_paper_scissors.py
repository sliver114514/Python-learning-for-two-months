# 地方性的玩法
import random

# 核心规则（5种武器互相克制）
# 结构：键（你出的拳） -> 值（你能打败的拳头列表）
rules = {
    "剪刀": ["布", "蜥蜴"],  # 剪刀剪布、斩蜥蜴
    "布": ["石头", "史波克"],  # 布包石头、反驳史波克
    "石头": ["剪刀", "蜥蜴"],  # 石头砸剪刀、砸蜥蜴
    "蜥蜴": ["史波克", "布"],  # 蜥蜴毒死史波克、吃布
    "史波克": ["剪刀", "石头"]  # 史波克踩碎剪刀、蒸发石头
}
choices = list(rules.keys())  # 获取所有武器名字，做成列表

# 计分器（存胜负平各多少局）
score = {"win": 0, "lose": 0, "tie": 0}

# 主游戏循环
while True:
    # 显示可选的武器，并获取输入
    user = input(f"\n请出拳 ({'/'.join(choices)}) 或输入 q 退出: ").strip()

    # 退出条件
    if user == "q":
        break

    # 输入校验
    if user not in choices:
        print("没有这个选项，重新出拳！")
        continue

    # 电脑随机选一个
    computer = random.choice(choices)
    print(f" 电脑出了：{computer}")

    # 判断输赢（最核心的3行）
    if user == computer:
        result = "tie"
    elif computer in rules[user]:  # 如果电脑出的拳，在“用户能打败的列表”里
        result = "win"
    else:
        result = "lose"

    # 显示本局结果
    if result == "win":
        print("你赢了！")
    elif result == "lose":
        print("你输了！")
    else:
        print("平局！")

    # 计分
    score[result] += 1

# 游戏结束，显示总战绩
print("\n" + "=" * 20)
print(f"🏆 最终战绩：胜 {score['win']} 局，负 {score['lose']} 局，平 {score['tie']} 局")