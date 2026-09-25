# 改进版猜拳游戏
# 相较于原版，本版优化了循环，但缺少了询问是否再次游玩，相信你可以自己加上的，这并不难
import random

# 核心规则，用字典表示"什么打败什么"
rules = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper",
}
choices = list(rules.keys())

# 计分器
score = {"win": 0, "lose": 0, "tie": 0}

while True:
    user = input("\n出拳 (rock/paper/scissor) 或 q 退出：").lower()
    if user =="q":
        break
    if user not in choices:
        print("乱出拳是违规的！")
        continue

    computer = random.choice(choices)
    print(f"电脑的选择是:{computer}")

    # 核心判断
    if user == computer:
        result = "tie"
    elif rules[user] == computer:
        result = "win"
    else:
        result = "lose"

    # 显示本局结果并加分
    print(f"你{ '赢了' if result == 'win' else '输了' if result == 'lose' else '们平了'}")
    score[result] += 1 # 在对应的上加一

# 最终成绩
print(f"\n总计: 胜 {score['win']} 局， 负 {score['lose']} 局， 平 {score['tie']} 局")