from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain
from ui import UI

question_bank = []

for data in question_data:
    question = data["question"]
    answer = data["correct_answer"]
    new_question = Questions(question, answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
game_ui = UI(quiz)
