import random
import time

# ========== 1. 数据层（字典）==========
# 这就像你之前做的通讯录管理器一样
player = {
    "name": "褪色者",
    "hp": 100,
    "max_hp": 100,
    "stamina": 100,  # 精力，攻击和翻滚都要消耗它
    "atk": 15
}

boss = {
    "name": "玛莲妮娅",
    "hp": 300,
    "max_hp": 300,
    "atk": 50,
    "action": "idle"  # 这个变量用来存Boss下一招的名字
}


# ========== 2. 核心函数（战斗逻辑）==========
def player_attack():
    """普通攻击：消耗精力，造成伤害"""
    if player["stamina"] < 20:
        print(" 精力不足！无法攻击。")
        return False

    # 消耗精力
    player["stamina"] -= 20

    # 伤害浮动（0.8 ~ 1.2 倍）
    damage = int(player["atk"] * random.uniform(0.8, 1.2))
    boss["hp"] -= damage
    print(f"⚔你砍中了{boss['name']}，造成 {damage} 点伤害！")

    # 不能让HP变成负数，难看
    if boss["hp"] < 0:
        boss["hp"] = 0
    return True


def player_roll():
    """翻滚：消耗精力，躲避下一次攻击（通过一个状态标志实现）"""
    if player["stamina"] < 30:
        print(" 精力不足！无法翻滚。")
        return False

    player["stamina"] -= 30
    print(" 你一个翻滚闪到侧面！下回合Boss攻击大概率Miss。")
    # 这里我们简单标记：如果翻滚了，Boss下一招伤害减半（模拟无敌帧）
    return True


def player_heal():
    """喝药：回复血量，不消耗精力，但有使用次数限制"""
    if player["hp"] >= player["max_hp"]:
        print(" 血量已满，别浪费药了。")
        return False

    heal_amount = random.randint(20, 35)
    player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
    print(f" 你喝了口药，回复了 {heal_amount} 点生命。")
    return True


def boss_ai():
    """Boss 的简单AI：随机出招"""
    # 恢复一点精力（模拟Boss的节奏）
    player["stamina"] = min(100, player["stamina"] + 10)

    # Boss 随机决定打你、重击、或者发呆
    choice = random.choice(["轻击", "重击", "突刺", "发呆"])
    boss["action"] = choice
    return choice


def boss_act(is_rolling):
    """执行Boss的动作，并计算伤害"""
    action = boss["action"]
    print(f"\n {boss['name']} 使出了【{action}】！")

    # 如果你选择了翻滚，Boss这回合伤害减半（模拟翻滚无敌）
    damage_multiplier = 0.3 if is_rolling else 1.0

    if action == "轻击":
        damage = int(boss["atk"] * 0.8 * damage_multiplier)
    elif action == "重击":
        damage = int(boss["atk"] * 1.4 * damage_multiplier)
    elif action == "突刺":
        damage = int(boss["atk"] * 1.0 * damage_multiplier)
    else:  # 发呆
        damage = 0
        print(" 但它打了个盹，什么也没发生。")

    if damage > 0:
        player["hp"] -= damage
        if player["hp"] < 0:
            player["hp"] = 0
        print(f" 你受到了 {damage} 点伤害！")
    else:
        print(" 你完全躲开了攻击！")


# ========== 3. 主游戏循环（你熟悉的 while）==========
def run_battle():
    print("=" * 30)
    print("  欢迎来到 2D 像素法环 Boss战  ")
    print(f"对手：{boss['name']} (HP: {boss['hp']})")
    print("=" * 30)

    turn = 1
    while player["hp"] > 0 and boss["hp"] > 0:
        print(f"\n--- 第 {turn} 回合 ---")
        print(f" 你的HP: {player['hp']}   ⚡ 精力: {player['stamina']}")
        print(f" BossHP: {boss['hp']}")

        # ---- 玩家回合 ----
        print("\n1. 攻击  2. 翻滚  3. 喝药")
        choice = input("请选择: ")

        # 重置翻滚状态
        rolled = False

        if choice == "1":
            player_attack()
        elif choice == "2":
            rolled = player_roll()  # 如果精力够，rolled就是True
        elif choice == "3":
            player_heal()
        else:
            print(" 愣着干嘛？Boss打过来了！")

        # 检查Boss是否被击败（在玩家攻击后可能死亡）
        if boss["hp"] <= 0:
            break

        # ---- Boss回合（只有在Boss活着时才执行）----
        boss_ai()  # Boss决定出什么招
        boss_act(rolled)  # Boss执行，传入是否翻滚了

        # ---- 回合结束检查玩家是否阵亡 ----
        if player["hp"] <= 0:
            print("\n 你倒下了... YOU DIED")
            break

        # ---- 自动恢复一点精力 ----
        player["stamina"] = min(100, player["stamina"] + 5)
        turn += 1
        time.sleep(0.8)  # 制造节奏感

    # ---- 结算 ----
    if boss["hp"] <= 0:
        print(f"\n {boss['name']} 被击败！")
        print(" 传说中的 2D 像素法环，由你亲手铸成！")
    elif player["hp"] <= 0:
        print("\n 你回到了赐福... 再试一次吧，褪色者。")


# ========== 4. 入口 ==========
if __name__ == "__main__":
    run_battle()