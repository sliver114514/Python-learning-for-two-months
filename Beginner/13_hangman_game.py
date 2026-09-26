import random

def play_hangman():
    """运行一局 Hangman 游戏，包含猜词逻辑、输入校验和结果展示"""

    words = ["python", "javascript", "coding", "developer", "computer", "science", "algorithm", "programming", "github"]
    chosen_word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6
    word_display = ["_" for _ in chosen_word]

    print("Welcome to Hangman!")

    while attempts > 0 and "".join(word_display) != chosen_word:
        print(f"\nWord: {' '.join(word_display)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Attempts remaining: {attempts}")

        guess = input("Guess a letter: ").lower()

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

    # Game over
    if "".join(word_display) == chosen_word: # 判断是否猜完
        print(f"\nCongratulations! You guessed the word: {chosen_word}")
    else:
        print(f"\nGame Over! You ran out of attempts. The word was: {chosen_word}")

def main():
    """循环运行游戏，直到用户选择退出"""
    while True:
        play_hangman()
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    main()
