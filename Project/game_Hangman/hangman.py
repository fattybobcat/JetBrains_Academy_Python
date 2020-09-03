import random


def round_game(word_list):
    random_word = random.choice(word_list)
    random_word_set = set(random_word)
    hidden = list("-" * (len(random_word)))
    check_dict = set()
    count_tries = 8
    while count_tries != 0:
        print(''.join(hidden))
        letter = input("Input a letter:")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not letter.isalpha() or not letter.islower():
            print("It is not an ASCII lowercase letter")
        elif letter in check_dict:
            print("You already typed this letter")
        else:
            check_dict.add(letter)
            if letter in random_word_set:
                for j in range(len(random_word)):
                    if letter == random_word[j]:
                        hidden[j] = letter
                if "-" not in hidden:
                    return True
            else:
                count_tries -= 1
                print("No such letter in the word")
                if count_tries == 0:
                    return False
        print()


def main():
    print("H A N G M A N")
    while True:
        decision = input('Type "play" to play the game, "exit" to quit: ')
        if decision == "play":
            print()
            random.seed()
            word_list = ('python', 'java', 'kotlin', 'javascript')
            result = round_game(word_list)
            if result:
                print("You guessed the word!")
                print("You survived!")
            else:
                print("You are hanged!")
            print()
        elif decision == "exit":
            break


if __name__ == '__main__':
    main()
