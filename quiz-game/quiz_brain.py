import random
import html
class QuizBrain:

    def __init__(self, question_list):
        self.max_score = 0
        self.q_number = 0
        self.question_list = question_list
        self.score = 0
        self.answered_question = []
        self.answer = ''
        self.correct_answer = ''
        self.q_text=None

    def next_question(self):
        self.max_score += 1
        self.q_number = random.randint(0, (len(self.question_list)-1))
        current_question = self.question_list[self.q_number].question
        self.q_text = html.unescape(current_question)
        # self.answer = input(f"Q.{self.max_score}. {self.q_text} (True or False): ").lower()
        self.answered_question.append(self.q_text)

    def still_has_questions(self):
        return len(self.question_list) > 0

    def calculate_score(self):
        self.correct_answer = self.question_list[self.q_number].answer
        if self.answer == self.correct_answer:
            self.score += 1

        self.question_list.remove(self.question_list[self.q_number])
