import random

NUMBER_OF_DICE = 2
POINTS_TO_WIN = 100

questions = [
    {"question": "The capital of Australia is Sydney.", "answer": "False"},
    {"question": "Humans have three kidneys.", "answer": "False"},
    {"question": "The Great Wall of China is visible from space with the naked eye.", "answer": "False"},
    {"question": "The chemical symbol for gold is Au.", "answer": "True"},
    {"question": "Mount Everest is the tallest mountain in the world.", "answer": "True"},
    {"question": "A crocodile cannot stick its tongue out.", "answer": "True"},
    {"question": "The Atlantic Ocean is the largest ocean on Earth.", "answer": "False"},
    {"question": "The human body has 206 bones.", "answer": "True"},
    {"question": "Lightning never strikes the same place twice.", "answer": "False"},
    {"question": "The Mona Lisa was painted by Vincent van Gogh.", "answer": "False"},
    {"question": "The Statue of Liberty was a gift from France to the United States.", "answer": "True"},
    {"question": "The Nile River is the longest river in the world.", "answer": "False"},
    {"question": "Sharks are mammals.", "answer": "False"},
    {"question": "The human brain stops growing after the age of 18.", "answer": "False"},
    {"question": "The Eiffel Tower is taller than the Washington Monument.", "answer": "True"},
    {"question": "The Earth has only one moon.", "answer": "False"},
    {"question": "Venus is the hottest planet in our solar system.", "answer": "True"},
    {"question": "There are 365 days in a leap year.", "answer": "False"},
    {"question": "Bees communicate with each other by dancing.", "answer": "True"},
    {"question": "Albert Einstein failed mathematics in school.", "answer": "False"},
    {"question": "Mars is known as the Red Planet.", "answer": "True"},
    {"question": "A group of crows is called a murder.", "answer": "True"},
    {"question": "The Amazon River flows through Brazil only.", "answer": "False"},
    {"question": "Water boils at 100 degrees Fahrenheit.", "answer": "False"},
    {"question": "Bananas grow on trees.", "answer": "False"},
    {"question": "The human heart has four chambers.", "answer": "True"},
    {"question": "The currency of Japan is the yen.", "answer": "True"},
    {"question": "Ostriches can fly.", "answer": "False"},
    {"question": "The Sahara Desert is the largest desert in the world.", "answer": "False"},
    {"question": "The moon has its own gravitational force.", "answer": "True"}
]

class Player():
    def __init__(self, name):
        self.name = name

    def roll_dice(self, number_of_dice) -> list:
        result = []
        roll = [random.randint(1,6) for i in range(number_of_dice)]

        total = sum(roll)
        result.append(total)
        result.append(roll)
        return result
    
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True

player1 = Player("Thomas")
player2 = Player("Sam")

print("-- LETS PLAY --")
print(f"First to {POINTS_TO_WIN} points wins")
print("")

score = [0, 0]
players = [player1, player2]
current_player_index = 0

while True:
    current_player = players[current_player_index]
    a = input(f"{current_player.name.upper()} press enter to roll -> ")
    # roll = player1.roll_dice(2)
    roll = current_player.roll_dice(2)
    print(f"{roll[1]}...You rolled a {roll[0]}")

    q = random.choice(questions)
    print(f"Q. {q["question"]} (true/false)")
    answer = input("Answer: ")

    if check_answer(answer.capitalize(), q["answer"]):
        print("correct")
        score[current_player_index] += roll[0]
    else:
        print(f"That's incorrect! You need {POINTS_TO_WIN - score[0]} points to win")
  
    if score[current_player_index] >= POINTS_TO_WIN:
        print(f"{current_player.name.upper()} wins!!")
        break
    
    print(f"<<< Score: {score[0]} - {score[1]} >>>")
    questions.remove(q)
    current_player_index = (current_player_index + 1) % 2
