# 首字母缩略词生成器 (Acronym Generator)
def generate_acronym(phrase):
    words = phrase.split()
    acronym_letters = []
    # 遍历字符串，过滤多余，提取首字母
    for word in words:
        if word[0].isalpha():
            acronym_letters.append(word)

    # 将提取出来的首字母拼回去并转化为字符串
    acronym = "".join(acronym_letters)
    return acronym

def main():
    print("=== Acronym Generate ===")

    user_phrase = input("Enter a phrase to generate acronym: ")

    if user_phrase.strip() == "":
        print("Please enter a valid non-empty phrase.")
    else:
        result_acronym = generate_acronym(user_phrase)

        if result_acronym:
            print(f"\nThe acronym for '{user_phrase}' is '{result_acronym}'.")
        else:
            print("\nCould not generate a valid acronym from the input.")

if __name__ == "__main__":
    main()