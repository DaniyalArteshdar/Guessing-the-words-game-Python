# GUessing the word game
# Coded by Daniyal Arteshdar

import random
import termcolor
import time

print(termcolor.colored("--<< Hello and Welcome to Word Guessing Game >>--", "magenta"))
print(termcolor.colored("** This game is designed by Py.Dan(Daniyal Arteshdar) ** \n", "magenta"))
name = input("-->> What's your name ? ")
print("!! Good luck ", name, " !!")

words_list = [
    'python', 'science', 'calculator',
              'computer', 'airplane', 'keyboard',
              'breakfast', 'play', 'victory',
              'cellphone', 'programming', 'rocket',
              'english', 'french', 'bookshelf',
              'giftshop', 'sunflower', 'desktop',
               'python', 'rocket', 'schoolbus','heater',
                'sync', 'programmer', 'armchair',
                'sofa', 'coffee', 'communication',
                'friendship', 'teacher','doctor',
                'firefighter','engineer','huddy', 
                'box', 'mousepod', 'organization']

time.sleep(1)
chosen_word = random.choice(words_list)
print("Let Go ... .  .   .    .      .\n")
guesses = ""
turns = len(chosen_word) + 2
time.sleep(1)

while turns > 0 :
    failed = 0

    print ( "...................................." )
    print ( "!! you have ", turns, "more guess !!" )

    for char in chosen_word :
        if char in guesses :
            print(char, end='')
        else:
            print(" - ", end='')
            failed +=1

    if failed == 0 :
        print("\n-*- YOU WIN -*-")
        print(termcolor.colored("\nThe chosen word was : ",
                                "magenta"), chosen_word)
        break

    guess = input("\n Guess the letter : ")
    guesses += guess

    if guess not in chosen_word :
        turns -= 1
        print("- wrong -")

        if turns == 0 :
            print("- YOU FAILED -")
            print(termcolor.colored("\nThe chosen word was : ",
                                    "magenta"), chosen_word)
