import json
import random
import os


def load_questions(filename):
    """Load questions from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)


def save_progress(filename, incorrect_queue):
    """Save incorrect questions to a file so progress is not lost."""
    with open(filename, "w") as f:
        json.dump(incorrect_queue, f, indent=4)


def play_game(questions_file, progress_file):
    """Play the multiple-choice game."""
    questions = load_questions(questions_file)
    incorrect_queue = []

    # Load progress if available
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            incorrect_queue = json.load(f)
    else:
        incorrect_queue = list(questions)  # Start with all questions

    print(
        "Welcome to the Quiz Game! Answer all questions correctly to win. Type 'q' to quit and save progress."
    )

    while incorrect_queue:
        question = random.choice(incorrect_queue)
        print(f"\n{question['question_number']}. {question['question']}")

        for key, value in question["options"].items():
            print(f"  {key.upper()}: {value}")

        while True:
            answer = (
                input("Enter your answer (A, B, C, etc.) or 'q' to quit: ")
                .strip()
                .lower()
            )

            if answer == "q":
                save_progress(progress_file, incorrect_queue)
                print("Game progress saved. Goodbye!")
                return

            if answer in question["options"]:  # Valid answer check
                break
            else:
                print("Invalid input. Please enter a valid option (A, B, C, etc.).")

        if answer == question["correct_answer"]:
            print("✅ Correct!")
            incorrect_queue.remove(question)
        else:
            print(
                f"❌ Wrong! The correct answer was {question['correct_answer'].upper()}: {question['options'][question['correct_answer']]}"
            )
            # Incorrect answers stay in the queue

    print("\n🎉 Congratulations! You have answered all questions correctly! 🎉")
    os.remove(progress_file)  # Remove progress file on completion


if __name__ == "__main__":
    play_game("questions_with_answers.json", "quiz_progress.json")
