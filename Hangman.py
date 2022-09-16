import random
import string
from words import words


def remove_space_having_words():
    word = random.choice(words)
    while (" " in words or "-" in words):
        word = random.choice(words)
    return word.upper()



def select_words():
    selected = remove_space_having_words()
    print(selected)
    already_typed = set()
    alphabets = set(string.ascii_uppercase)
    original_words = set(selected)
    lives = 3
    

    
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
    else:
        print("You lose the game.")


select_words()
