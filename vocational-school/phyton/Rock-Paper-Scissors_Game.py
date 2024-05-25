import random
user_score = 0
system_score = 0
symbols = ["rock", "paper", "scissors"]

def main():
    while True:
        for i in range(len(symbols)):
            print(f"{i+1}: {symbols[i]}")
        user_turn: str = ""
        while user_turn not in symbols:
            user_turn = input("Please choose one of the following symbols or enter Q to quit:\n").lower()
            if user_turn == "q":
                quit("User entered 'q' to quit")
            if user_turn.isdigit():
                if 1 <= int(user_turn) <= 3:
                    user_turn = symbols[int(user_turn)-1]
                    break
        system_turn = generate_system_turn()
        print(f"The system took {system_turn}")
        evaluate_winning(user_turn, system_turn)
        print_standings()

def generate_system_turn():
    return symbols[random.randint(0 , 2)]

def print_standings():
    print(f"The current standings are the following:\n######################################\n\n{user_score=}\t|\t{system_score=}\n\n######################################\n")



def evaluate_winning(user_turn, system_turn):
    global system_score, user_score
    if user_turn == system_turn:
        print(f"The game ended in a tie, because both parties took {user_turn}")
    elif user_turn == "rock" and system_turn == "paper":
        print("The System won because Paper destroys Rock")
        system_score += 1
    elif user_turn == "rock" and system_turn == "scissors":
        print("You won because Rock destroys Scissors")
        user_score += 1
    elif user_turn == "paper" and system_turn == "rock":
        print("You won because Paper destroys Rock")
        user_score += 1
    elif user_turn == "paper" and system_turn == "scissors":
        print("The System won because Scissors destroys Paper")
        system_score += 1
    elif user_turn == "scissors" and system_turn == "rock":
        print("The System won because Rock destroys Scissors")
        system_score += 1
    elif user_turn == "scissors" and system_turn == "paper":
        print("You won because Scissors destroys Paper")
        user_score += 1


if __name__ == "__main__":
    main()