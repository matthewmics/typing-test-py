path_data = "./data/words.dat"

def fetch_words():
    f = open(path_data, "r")
    data = f.read()
    f.close()

    if str.isspace(data) or len(data) == 0:
        return []

    return data.split("|")

def add_words(words):
    added_words = []

    while True:
        print()
        print("Enter New Word")
        user_input = input("Input: ")

        if str.isspace(user_input) or len(user_input) == 0 or not str.isalpha(user_input):
            print("Invalid Input!")
            continue

        if len(user_input) < 6:

            if user_input in get_easy_words(words):
                print("\"" + user_input + "\"" " already exists")
                continue
            print(user_input + " added to the easy list")

        elif len(user_input) > 5 and len(user_input) < 9:

            if user_input in get_intermediate_words(words):
                print("\"" + user_input + "\"" " already exists")
                continue
            print(user_input + " added to the intermediate list")

        else:

            if user_input in get_hard_words(words):
                print("\"" + user_input + "\"" " already exists")
                continue
            print(user_input + " added to the hard list")
        
        words.append(user_input)
        added_words.append(user_input)
        user_input = input("Add again? [y,n] ")

        if user_input != "y":
            print()
            break
    
    data_length = len(fetch_words())

    f = open(path_data, "a")
    to_append = ""

    index = 0
    for word in added_words:

        if index == 0 and data_length == 0:
            to_append += word
        else:
            to_append += "|" + word

        index += 1


    f.write(to_append)
    f.close()

    return added_words

def get_easy_words(words):
    result = []
    for word in words:
        if len(word) < 6 and len(word) != 0:
            result.append(word)     
    return result

def get_intermediate_words(words):
    result = []
    for word in words:
        if len(word) >= 6 and len(word) < 9:
            result.append(word)     
    return result

def get_hard_words(words):
    result = []
    for word in words:
        if len(word) > 8:
            result.append(word)     
    return result

def display_words(words):
    while True:
        print()
        print("[1] View easy words")
        print("[2] View intermediate words")
        print("[3] View hard words")
        print("[4] Return")
        user_input = input("Input: ")

        if user_input == "1":

            print()
            easy_words = get_easy_words(words)
            print("There are " + str(len(easy_words)) + " words in the \"easy\" list")
            for word in easy_words:
                print(word)

        elif user_input == "2":

            print()
            intermediate_words = get_intermediate_words(words)
            print("There are " + str(len(intermediate_words)) + " words in the \"Intermediate\" list")
            for word in intermediate_words:
                print(word)

        elif user_input == "3":

            print()
            hard_words = get_hard_words(words)
            print("There are " + str(len(hard_words)) + " words in the \"Hard\" list")
            for word in hard_words:
                print(word)

        elif user_input == "4":

            print()
            break

        else:
            
            print("Invalid Input!")
            continue

        user_input = input("\nView again? [y,n] ")

        if user_input != "y":
            print()
            break


