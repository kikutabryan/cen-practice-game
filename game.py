import json
import random
import os
import pickle


def load_questions(filename):
    """Load questions from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)


def save_progress(progress_file, remaining_questions):
    """Save remaining question numbers to a file."""
    with open(progress_file, "wb") as f:
        pickle.dump(remaining_questions, f)


def load_progress(progress_file, total_questions):
    """Load remaining question numbers if progress exists, else return all question indexes."""
    if os.path.exists(progress_file):
        with open(progress_file, "rb") as f:
            return pickle.load(f)
    return list(range(total_questions))


def play_game(questions_file, progress_file):
    """Play the multiple-choice game."""
    questions = load_questions(questions_file)
    remaining_questions = load_progress(progress_file, len(questions))

    print(
        "Welcome to the Quiz Game! Answer all questions correctly to win. Type 'q' to quit and save progress."
    )

    while remaining_questions:
        question_index = random.choice(remaining_questions)
        question = questions[question_index]
        print(f"\n{question['question_number']}. {question['question']}")

        for key, value in question["options"].items():
            print(f"  {key.upper()}: {value}")

        while True:
            answer = (
                input(
                    f"Enter your answer (A, B, C, etc.) or 'q' to quit (Questions remaining: {len(remaining_questions)}): "
                )
                .strip()
                .lower()
            )

            if answer == "q":
                save_progress(progress_file, remaining_questions)
                print("Game progress saved. Goodbye!")
                return

            if answer in question["options"]:  # Valid answer check
                break
            else:
                print("Invalid input. Please enter a valid option (A, B, C, etc.).")

        if answer == question["correct_answer"]:
            print("✅ Correct!")
            remaining_questions.remove(question_index)
        else:
            print(
                f"❌ Wrong! The correct answer was {question['correct_answer'].upper()}: {question['options'][question['correct_answer']]}"
            )
            # Incorrect answers stay in the queue

    print("\n🎉 Congratulations! You have answered all questions correctly! 🎉")
    os.remove(progress_file)  # Remove progress file on completion


if __name__ == "__main__":
    play_game("questions.json", "quiz_progress.pkl")
