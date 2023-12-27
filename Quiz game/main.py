from data import question_data
from question import Question
from quiz_brain import QuizBrain
import random

question_bank = [Question(question['text'], question['answer']) for question in question_data]

quiz_brain = QuizBrain(random.shuffle(question_bank))


while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")