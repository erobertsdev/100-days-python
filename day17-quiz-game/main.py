# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0 # default value
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# user_1 = User("007", "Elias")
# print(user_1.username)
# print(user_1.followers)

# user_2 = User("101", "Clementine")
# print(user_2.username)

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.following)
# print(user_2.followers)

# from question_model import Question
# from data import question_data

# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[question_number]
        input(f"{self.question_number}: {current_question.text} (True/False): ")