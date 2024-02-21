import random

quiz_questions = {
    'General Knowledge': {
        'What is the capital of France?': ['A. London', 'B. Paris', 'C. Berlin', 'D. Rome', 'B'],
        'Which planet is known as the Red Planet?': ['A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn', 'B'],
    },
    'Science': {
        'What is the chemical symbol for water?': ['A. H2O', 'B. CO2', 'C. O2', 'D. N2', 'A'],
        'Who developed the theory of general relativity?': ['A. Isaac Newton', 'B. Albert Einstein', 'C. Galileo Galilei', 'D. Stephen Hawking', 'B'],
    },
}

def run_quiz():
    score = 0

    print("Welcome to the Quiz Application!")

    
    for category, questions in quiz_questions.items():
        print(f"\n{category} Questions:")
        print("-" * 30)

        
        shuffled_questions = list(questions.items())
        random.shuffle(shuffled_questions)

        
        for question, options in shuffled_questions:
            print(question)
            for option in options[:-1]:
                print(option)
            
            
            user_answer = input("Enter the letter corresponding to your answer: ").upper()
            correct_answer = options[-1]

            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}\n")

    
    print("\nQuiz completed!")
    print(f"Your final score is: {score}/{len(shuffled_questions)}")

if __name__ == "__main__":
    run_quiz()
