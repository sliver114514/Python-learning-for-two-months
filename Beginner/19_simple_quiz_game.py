def run_quiz(questions):
    score = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Your answer (A, B, C, or D): ").upper()

        if user_answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nQuiz finished! Your final score is {score}/{len(questions)}.")


if __name__ == "__main__":
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
            "answer": "B"
        }
    ]

    print("--- Simple Quiz Game ---")
    run_quiz(quiz_questions)