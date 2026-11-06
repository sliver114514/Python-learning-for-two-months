# 简单的选则题
def run_quiz(question):
    score = 0
    for i, q in enumerate(question):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("You answer (A, B, C or D):").upper()

        if user_answer == q['answer']:
            print(f"Correct! You got it!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}")

    print(f"\nQuiz finished!Yor final score is {score}/{len(question)}")


if __name__ == '__main__':
    quiz_question = [
        {
            "question":"'千古地仙随风逝，昔日三王归青冢。阳莽憾陨谁无败？卷土重来再称王...'首次出现是在什么地方？",
            "options": ["A.白骨山", "B.三王山", "C.义天山", "D.青茅山"],
            "answer": "B"
        },
        {
            "question":"蛊修世界的第十一位尊者是？",
            "options":["A.古月方源", "B.古月方正", "C.古月青书", "D.古月一代"],
            "answer": "A"
        },
        {
            "question": "'当时年少掷春光，飞马踏蹄酒溅香。爱恨情仇随浪来，夏蝉歌醒夜未央...'是指谁？",
            "options": ["A.炼天魔尊", "B.幽魂魔尊", "C.狂蛮魔尊", "D.红莲魔尊"],
            "answer": "D"
        }
    ]

    print("--- Simple Quiz Game---")
    run_quiz(quiz_question)