from features.words import fetch_words, display_words, add_words
from features.game import start_game, fetch_scores, display_scores

data = {
    "words": fetch_words(),
    "scores": fetch_scores()
}

while True :

    print("[1] Game Start")
    print("[2] High Score")
    print("[3] Add Words")
    print("[4] List of Words")
    print("[5] Quit Game")

    user_input = input("Input: ") 
    if str(user_input) == "5":
        break

    elif (user_input) == "4":
        display_words(data["words"])

    elif (user_input) == "3":
        add_words(data["words"])
    
    elif (user_input) == "2":
        display_scores(data["scores"])

    elif (user_input) == "1":
        start_game(data["words"])
        data["scores"] = fetch_scores()

    else:
        print("Invalid Input!\n")



print("Bye...")