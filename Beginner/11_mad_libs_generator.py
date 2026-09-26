# 创建主函数（逻辑一点没动，全是中文提示）
def mad_libs(story):
    words = {}
    for word_type in story["word_types"]:
        words[word_type] = input(f"请输入一个{word_type}：")

    filled_story = story["template"].format(**words)
    print("\n" + "="*30)
    print(filled_story)
    print("="*30)

# 故事库（全部改成中文版）
stories = [
    {
        "name": "消失的宝藏",
        "word_types": ["形容词", "名词", "动词", "副词", "地点"],
        "template": "有一天，一个{形容词}的{名词}决定{副词}地{动词}到{地点}，从此再也没有人见过它……"
    },
    {
        "name": "奇怪的生日派对",
        "word_types": ["形容词", "名词", "动词", "数字", "食物"],
        "template": "在我的生日派对上，有{数字}个{名词}在{形容词}地{动词}，我们还吃了很多{食物}！"
    },
    {
        "name": "疯狂的秋游",
        "word_types": ["形容词", "名词", "动词", "地点", "动物"],
        "template": "我们的秋游非常{形容词}。我们在{地点}看到一只{动物}在{动词}一只{名词}，然后这只{动物}还想来{动词}我们！"
    },
    {
        "name": "外星人入侵",
        "word_types": ["形容词", "名词", "动词", "副词", "复数名词"],
        "template": "突然，一艘{形容词}的飞船降落在我家后院！一个{名词}外星人跳出来，开始{副词}地{动词}我的{复数名词}！我从来没想过{名词}外星人会这样做。"
    }
]

# 欢迎界面（全中文）
print("欢迎来到疯狂填词游戏！")
for i, story in enumerate(stories):
    print(f"{i+1}. {story['name']}")

# 选择故事（防呆循环，提示全中文）
while True:
    try:
        choice = int(input("请选择一个故事 (1-4)："))
        if 1 <= choice <= len(stories):
            break
        else:
            print("无效选择，请输入1到4之间的数字。")
    except ValueError:
        print("输入无效，请输入数字。")

# 调用函数，开始填词
mad_libs(stories[choice - 1])