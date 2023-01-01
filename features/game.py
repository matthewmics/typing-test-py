import time
import random

from features.words import get_easy_words, get_hard_words, get_intermediate_words

path_data = "./data/scores.dat"

def start_game(words):
    
    easy_words = get_easy_words(words)
    intermediate_words = get_intermediate_words(words)
    hard_words = get_hard_words(words)

    error = False

    if len(easy_words) < 3:
        print("Easy list must have atleast 3 or more words")
        error = True

    if len(intermediate_words) < 3:
        print("Intermediate list must have atleast 4 or more words")
        error = True

    if len(hard_words) < 3:
        print("Hard list must have atleast 3 or more words")
        error = True

    if error:
        print()
        return None
    
    random.shuffle(easy_words)
    random.shuffle(intermediate_words)
    random.shuffle(hard_words) 

    print("The timer will start in 5...")
    time.sleep(1)
    print("The timer will start in 4...")
    time.sleep(1)
    print("The timer will start in 3...")
    time.sleep(1)
    print("The timer will start in 2...")
    time.sleep(1)
    print("The timer will start in 1...")
    print("Timer started\n")
    
    start = time.time()

    print("Easy")
    begin_typing(easy_words, ["1st word: ", "2nd word: ", "3rd word: "])
    print("Intermediate")
    begin_typing(intermediate_words, ["1st word: ", "2nd word: ", "3rd word: ", "4th word: "])
    print("Hard")
    begin_typing(hard_words, ["1st word: ", "2nd word: ", "3rd word: "])

    duration = int(round(time.time() - start, 0))

    print(f'It took you {duration} seconds to enter the 10 words correctly!')
    print("Enter your name so I can put you into our record books.")

    while True:
        u_input = input("Your name: ")
        
        if "$" in u_input or "|" in u_input:
            print("Invalid Input!\n")
            continue
            
        save_score(u_input, duration)
        print()
        break

def begin_typing(words, sequences):
    index = 0
    for sequence in sequences:

        while True:
            word = words[index]
            print(sequence + word)
            u_input = input("your input: ")

            if u_input == word:
                print("Correct!\n")
                break
            
            print("Try again!\n")

        index += 1

def fetch_scores():
    f = open(path_data, "r")
    data = f.read()
    f.close()

    if str.isspace(data) or len(data) == 0:
        return []

    data = data.split("|")

    result = []

    for record in data:
        record_data = record.split("$")
        result.append({
            "name": record_data[0],
            "score": record_data[1]
        })

    return result

def save_score(name, score):
    data_length = len(fetch_scores())

    f = open(path_data, "a")
    to_append = ""

    if data_length == 0:
        to_append += name + "$" + str(score)
    else:
        to_append += "|" + name + "$" + str(score)

    f.write(to_append)
    f.close()

def display_scores(scores):

    print()

    if len(scores) == 0:

        print("No records yet\n")
        return

    scores_sorted = sorted(scores, key=lambda x:x["score"])

    name_padding = 0
    rank_padding = 7

    for score in scores:
        length = len(score["name"])
        if length > name_padding:
            name_padding = length

    name_padding += 3
    print("Rank".ljust(rank_padding, " ") + "Name".ljust(name_padding, " ") + "Time")

    rank = 1
    for score in scores_sorted:
        print(str(rank).ljust(rank_padding, " ") + score["name"].ljust(name_padding, " ") + str(score["score"]) + "s" )
        rank += 1

    print()