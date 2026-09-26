# 填词游戏，蛊真人版
def mad_libs(story):
    words = {} # 存放填写的词
    for word_type in story["word_types"]: # 遍历所填写的词
        words[word_type] = input(f"请输入一个{word_type}: ") # 遍历选择

    filled_story = story["template"].format(**words) # 严格按照键值对来匹配
    # 打印结果
    print("\n" + "=" * 30)
    print(filled_story)
    print("=" * 30)

# 数据仓库
stories = [
    {
        "name" : "纵身亡魔心仍不悔",
        "word_types" : ["形容词", "名词", "副词", "动词", "地点"],
        "template" : "方源，快快交出春秋蝉！一个{形容词}的{名词}大喊！他{副词}的{动词}到{地点}面前，"
    },
    {
        "name" : "逆光阴五百年觉悟",
        "word_types" : ["形容词", "名词", "动词", "数字", "食物"],
        "template" : "为了一个女人，你就{形容词}地对{名词}，我为什么{动词}你？就为了{数字}块原石？我宁愿自己挨饿，也没忘了你爱吃{食物}"
    },
    {
        "name" : "人兽葬生蛊",
        "word_types" : ["形容词", "名词", "动词", "地点", "食物"],
        "template" : "一个{形容词}熊，看着眼前的{名词}，方源面无表情，只是冷冰冰地{动词}这一切，谁也没想到，在{地点}里，一头熊正吃着{食物}"

    },
    {
        "name" : "定仙游",
        "word_types" : ["形容词", "名词", "副词", "动词", "人名"],
        "template" : "众人一脸{形容词}，仙蛊！他当真在炼制仙蛊！{形容词}！真是美轮美奂啊！众人{副词}{动词}{方源}，只听他吟到......"
    }
]

# 菜单显示部分
print("欢迎来到填词游戏！")
for i, story in enumerate(stories):
    print(f"{i + 1}. {story['name']}")

while True:
    try:
        choice = int(input("请选择一个故事(1-4):"))
        if 1<= choice <= len(stories):
            break
        else:
            print("无效选择，请输入1到4之间的数字")
    except ValueError:
        print("输入无效，请输入数字")

# 启动函数
mad_libs(stories[choice - 1])