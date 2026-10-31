from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

def ask_ai(topic):
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="You are a friendly Python tutor who explains concepts simply to beginners.",
        input=topic
        
    )
    return response.output_text
def get_study_tip(topic):
    tips = {"loops": "Practice tracing each iteration.",
            "functions": "Practice parameters and return values.",
            "lists": "Practice append(), pop(), and indexing."
    }
    return tips.get(topic.lower(), "Practice a little every day.")
correct_count = 0
total_questions = 0
print("=== AI STUDY ASSISTANT ===")
print("Enter a Python topic to receive a study tip.")
print("Type 'quit' to exit the program.")
print("Type 'quiz' to practice with a question.")
print("Type 'score' to view your quiz results.")
print("Type 'reset' to start your quiz score over.")

def generate_quiz(topic):
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="You are a Python tutor. Create one beginner-friendly multiple-choice question with four answer choices(A, B, C, D). After the four choices, include EXPLANATION: followed by a short explanation of the correct answer. Put ANSWER: A on the final line, using the actual correct letter. Do not use Markdown formatting or triple backticks in the question or answer choices.",
        input=topic 
    )
    return response.output_text

while True:
    topic = input("What Python topic do you need help with? ")
    if topic.lower() == "quit":
        break
    if topic.lower() == "reset":
        correct_count = 0
        total_questions = 0
        print("Your quiz score has been reset!")
        continue 
    if topic.lower() == "score":
        print(f"Correct Answers: {correct_count}/{total_questions}")
        if total_questions == 0:
            print("You haven't answered any quiz questions yet.")
        else:
            score = (correct_count / total_questions) * 100
            print(f"Current Score: {score:.1f}%")
        continue 
    if topic.lower() == "quiz":
        quiz_topic = input("What Python topic would you like to practice? ")
        quiz_question = generate_quiz(quiz_topic)
        parts = quiz_question.rsplit("ANSWER:", 1)
        if len(parts) != 2:
            print("Unable to generate a valid quiz. Please try again.")
            continue 
        quiz_parts = parts[0].rsplit("EXPLANATION:", 1) 
        if len(quiz_parts) != 2:
            print("The AI did not provide an explanation. Please try another quiz.")
            continue 
        correct_answer = parts[1].strip().upper()
        if correct_answer not in ["A", "B", "C", "D"]:
            print("The AI provided an invalid answer. Please try another quiz.")
            continue 
        print(quiz_parts[0])

        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid answer. Please enter A, B, C, or D.")
            user_answer = input("Try again (A, B, C, or D): ").strip().upper()
        total_questions += 1
        if user_answer == correct_answer:
            print("Correct! Great job!")
            correct_count += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
        print(f"\nExplanation: {quiz_parts[1].strip()}")
        score = (correct_count / total_questions) * 100
        print(f"Current Score: {score:.1f}%")
        print(f"Correct Answers: {correct_count}/{total_questions}")
        continue 

    print(ask_ai(topic))
    print("\n--- STUDY TIP ---")
    print(get_study_tip(topic))