import random
def game():
    player_input=input("Enter your choice: rock(r), paper(p) and scissors(s): ".lower())
    computer_input=random.choice(['r','p','s'])
    if computer_input=='r':
        print("Computer has picked: Rock")
    elif computer_input=='s':
        print(("Computer has picked: Scissors"))
    else:
        print("Computer has picked: Paper")
#r>s, s>p, p>r
    if player_input==computer_input:
        return "The game is tied"
    if is_win(player_input,computer_input):
        return "You have won"
    return "You lost bitch"


def is_win(human,machine):
    if(human =='r' and machine=='s') or (human =='s' and machine =='p') or (human =='p' or machine =='r'):
        return True

print(game())
