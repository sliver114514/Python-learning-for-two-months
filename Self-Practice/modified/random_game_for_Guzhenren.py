import random

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions):
        # 每次出题前，打乱纯文本列表（ABCD 标签还没贴呢）
        random.shuffle(q['options'])

        print(f"\n第 {i + 1} 题: {q['question']}")
        # 显示时，动态给每个选项贴上 A, B, C, D 标签
        for idx, text in enumerate(q['options']):
            label = chr(65 + idx)  # 0->A, 1->B, 2->C, 3->D
            print(f"   {label}. {text}")

        while True:
            user_input = input("你的答案 (A/B/C/D): ").upper()
            if user_input in ['A', 'B', 'C', 'D']:
                break
            else:
                print("输入无效！请输入A,B,C或D")
        # 把字母转成索引（A=0, B=1, C=2, D=3）
        chosen_index = ord(user_input) - ord('A')

        # 判断：用户选中的那个位置的文本，是不是正确答案？
        if q['options'][chosen_index] == q['answer']:
            print("正确！")
            score += 1
        else:
            # 找出正确答案在打乱后的列表中的索引
            correct_index = q['options'].index(q['answer'])
            # 根据索引生成对应的字母标签（0->A, 1->B, 2->C, 3->D）
            correct_label = chr(65 + correct_index)
            # 显示“字母. 文本”的格式
            print(f"错误！正确答案是：{correct_label}. {q['answer']}")

    print(f"\n最终得分：{score}/{len(questions)}")


if __name__ == '__main__':
    quiz_questions = [
        {
            "question": "'千古地仙随风逝，昔日三王归青冢。阳莽憾陨谁无败？卷土重来再称王...'首次出现是在什么地方？",
            "options": ["白骨山", "三王山", "义天山", "青茅山"],  # ← 只有纯文本
            "answer": "三王山"  # ← 直接存文本，不存字母！
        },
        {
            "question": "蛊修世界的第十一位尊者是？",
            "options": ["古月方源", "古月方正", "古月青书", "古月一代"],
            "answer": "古月方源"
        },
        {
            "question": "'当时年少掷春光，飞马踏蹄酒溅香。爱恨情仇随浪来，夏蝉歌醒夜未央...'是指谁？",
            "options": ["炼天魔尊", "幽魂魔尊", "狂蛮魔尊", "红莲魔尊"],
            "answer": "红莲魔尊"
        }
    ]

    # 只打乱题目顺序（选项在 run_quiz 里每次随机打乱）
    random.shuffle(quiz_questions)

    print("--- 随机问答游戏 ---")
    run_quiz(quiz_questions)