import random

# Trivia questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest animal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Lion"],
        "answer": "Blue Whale"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"],
        "answer": "William Shakespeare"
    }
]

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")
    user_answer = input("Enter the number of your answer: ")
    return question["options"][int(user_answer) - 1]

def trivia_game():
    random.shuffle(questions)
    score = 0
    
    print("Welcome to the Trivia Quiz Game!")
    
    for question in questions:
        user_choice = ask_question(question)
        if user_choice == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {question['answer']}.\n")
    
    print(f"Quiz finished! Your score is {score}/{len(questions)}.")

if __name__ == "__main__":
    trivia_game()
