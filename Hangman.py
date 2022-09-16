import random
import string
from words import words


def remove_space_having_words(level):
    word = random.choice(words)
    while (" " in words or "-" in words):
    
        word = random.choice(words)
    while True:
        if level == "easy":
            if 0<=len(word) <=4:
                return word.upper()
            else:
                break
        elif level == "medium":
            if 4 < len(word) <= 6:
                return word.upper()
            else:
                break
        elif level == "hard":
            if len(word) > 6:
                return word.upper()
            else:
                break
        else:
            break
    return remove_space_having_words(level)
        
    
    


def select_words():
    
    level = input("Type the Difficulty level('easy','medium','hard'): ").lower()
    try:
        if level =="easy" or "medium" or "hard":
            selected = remove_space_having_words(level)
            print(selected)

    except RecursionError:
        print("Invalid Input, Please try again.")
        return select_words()
       
            
    
    already_typed = set()
    alphabets = set(string.ascii_uppercase)
    original_words = set(selected)
    while True:
        try:
            lives = int(input("How Many Lives Do you want: "))
            break
        except ValueError:
            print("Invalid Input, Please try again")


    
    while (len(original_words) > 0 and lives > 0):
        print("the letters you typed: " ,  ", ".join(already_typed))
        print("Number of Lives Remaining: ", lives)
        word_list = [letter if letter in already_typed else "-" for letter in selected]
        print("Current word: "," ".join(word_list))
        
        typed_letter = input("Type the Letter: ").upper()
        if (typed_letter in alphabets - already_typed):
            already_typed.add(typed_letter)

            if typed_letter in original_words:
                original_words.remove(typed_letter)
            else:
                lives-=1
                print("Lives: ", lives)
        elif typed_letter in already_typed:
            print("You already typed that,try again.")
        else:
            print("Invalid character: ",    typed_letter, "Try again.")
    if lives > 0:
        print("Hurray You win the game.")
        print(f"The WOrd is : {selected}.")
    else:
        print("You lose the game.")
        print(f"The Word is : {selected}.")


select_words()
