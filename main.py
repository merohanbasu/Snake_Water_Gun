import random

def play(user_choice, rand):
    match user_choice:
        case "snake":
            if (rand == "Snake"):
                print("So its a Draw")
            elif (rand == "Water"):
                print("So you Won")
            elif (rand == "Gun"):
                print("So you Lose")
        case "water":
            if (rand == "Snake"):
                print("So you Lose")
            elif (rand == "Water"):
                print("So its a Draw")
            elif (rand == "Gun"):
                print("So you Won")
        case "gun":
            if (rand == "Snake"):
                print("So you Won")
            elif (rand == "Water"):
                print("So you Lose")
            elif (rand == "Gun"):
                print("So its a Draw")
def check_input(user_choice):
    if user_choice not in ["snake", "water", "gun"]:
        raise ValueError("Invalid Input")

def main():
    s = "Welcome to Snake Water Gun Game"
    print(s.center(50))

    user_choice = input("Enter your choice within {Snake}  {Water}  {Gun}  -> ")
    user_choice = user_choice.lower()

    try:
        check_input(user_choice)
    except ValueError as e:
        print(e)
        return

    ch = ["Snake", "Water", "Gun"]

    rand = random.choice(ch)

    print(f"You chose '{user_choice}' and opponent chose '{rand}'")

    play(user_choice, rand)

if __name__ == "__main__":
    main()






