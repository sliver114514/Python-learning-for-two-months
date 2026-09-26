# # 魔改版Hangman_game,比原版更完善，新加入了部分功能
import random

def play_hangman():
    """运行一局 Hangman 游戏，包含猜词逻辑、输入校验和结果展示"""
    # "天道使然"， "冷酷的恒常", "彻底的漠然", "焚身的执念", "思乡病", "撕裂的二重性", "异类"， "被放逐者"
    words = ["Inevitability", "Relentlessness", "Apathy", "Obsession", "Homesickness", "Dichotomy", "Anomaly", "Pariah"]
    chosen_word = random.choice(words).lower() # 随机选词
    guessed_letters = [] # 记录用户已经猜过的字母
    length_word = len(chosen_word) # 为了显示单词长度，方便判断
    attempts = 6 # 允许的最大错误次数
    # 生成与单词等长的下划线:遍历与选择的单词的同等次数，并用下划线代替
    word_display = ["_" for _ in chosen_word]

    print("=" * 20 +"\nWelcome to Hangman!\n" + "=" * 20)

    # 循环继续条件的条件:还有猜测的次数，且，下划线列表拼起来不等于原单词
    while attempts > 0 and "".join(word_display) != chosen_word:
        wrong_letters = [l for l in guessed_letters if l not in chosen_word]
        print(f"\nWord: {' '.join(word_display)}") # 加装空格隔开字母
        print(f"Guessed length: {length_word}") # 显示长度
        # 加装逗号和空格,-sorted()返回一个新列表，原字符串不变，显示所猜的字母
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Attempts remaining: {attempts}")
        print(f"Wrong guesses: {', '.join(wrong_letters)}")

        guess = input("Guess a letter: ").lower()

        # 卫语句,快速过滤非法输入
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input.Please enter a single letter.")
            continue

        # 卫语句，防止反复猜测
        if guess in guessed_letters:
            print(f"You have already guessed '{guess}'.Please try another letter.")
            continue

        guessed_letters.append(guess) # 记录本次猜测

        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.'")
            # enumerate 同时获取索引和字符，用于更新对应位置下滑线
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[i] = guess # 替代下划线为正确字母

        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1 # 猜错一次减一次机会

    # 循环结束后，根据是否完全猜出来判断胜负
    if "".join(word_display) == chosen_word:
        print(f"Congratulations, you guessed the word: {chosen_word}.")
    else:
        print(f"\nGame over, you ran out of attempts.The word was: {chosen_word}.")

def main():
    """循环运行游戏，直到用户选择退出"""
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again not in ("y", "yes"):
            print("Thank you for playing Hangman!")
            break # 退出

# 如果这个文件直接被运行而不是被导入，则执行main()
if __name__ == "__main__":
    main()