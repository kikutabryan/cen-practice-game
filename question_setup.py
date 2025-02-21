import json


def select_correct_answers(filename):
    with open(filename, "r") as f:
        questions = json.load(f)

    print("Select the correct answer for each question (A, B, C, etc.)")
    for q in questions:
        print("\n" + str(q["question_number"]) + ". " + q["question"])
        for key, value in q["options"].items():
            print(f"  {key.upper()}: {value}")

        while True:
            choice = input("Enter correct answer (A, B, C, etc.): ").strip().lower()
            if choice in q["options"]:
                q["correct_answer"] = choice
                break
            else:
                print("Invalid choice. Please enter A, B, C, D, or E.")

    # Save updated file with correct answers
    updated_filename = filename.replace(".json", "_with_answers.json")
    with open(updated_filename, "w") as f:
        json.dump(questions, f, indent=4)

    print(f"\nCorrect answers saved to {updated_filename}")


if __name__ == "__main__":
    select_correct_answers("questions.json")
