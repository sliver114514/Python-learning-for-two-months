# 经典版石头剪刀布
import random

options = ["rock", "paper", "scissors"]

# 允许重复游戏
while True:
    # 读取用户选择
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    # 验证
    if user_choice not in options:
        print("Invalid choice.Please choose rock, paper, or scissors.")
        continue

    # 电脑的随机数
    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}.")

    # 决定胜者
    if user_choice == computer_choice:
        print("It's a tie.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win.")
    else:
        print("You lose.")

    # 询问是否再次游戏
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break