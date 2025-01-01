import random

def ask_questions():
    questions = [
        {
            "question": "What color is the sky?",
            "options": ["1. Blue", "2. Gray"],
            "correct_answer": "1"
        },
        {
            "question": "What is the capital of France?",
            "options": ["1. Berlin", "2. Paris"],
            "correct_answer": "2"
        },
        {  __name__ == "__main__
         
            "question": "What is 2 + 2?",
            "options": ["1. 3", "2. 4"],
            "correct_answer": "2"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["1. Earth", "2. Mars"],
            "correct_answer": "2"
        }
    ]
    
    selected_question = random.choice(questions)
    
    print(selected_question["question"])
    for option in selected_question["options"]:
        print(option)

    choice = input("Choose the correct option (1 or 2): ")

    if choice == selected_question["correct_answer"]:
        print("Correct!")
    else:
        print("Incorrect! The correct answer is:", selected_question["correct_answer"])

if __name__ == "__main__":
    ask_questions()
