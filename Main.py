import random, string

ascii_char = string.ascii_lowercase
word_selected = random.choice(['python', 'java', 'kotlin', 'javascript'])
guess = ['-' for _, _ in enumerate(word_selected)]
typed = set()
game_loop = True
lives = 8


def game_reset(word_selected, guess, typed, lives):
    word_selected = random.choice(['python', 'java', 'kotlin', 'javascript'])
    guess = ['-' for _, _ in enumerate(word_selected)]
    typed.clear()
    lives = 8
    return word_selected, guess, typed, lives


def validate(char):
    """
    :param char: user input character
    :return: True if validation is successful
    """
    if len(char) != 1:
        print(f"You should print a single letter")
        return False
    elif char in typed:
        print("You already typed this letter")
        return False
    elif char not in ascii_char:
        print("It is not an ASCII lowercase letter")
        return False

    return True


def live_decrement(word, guessed, input_char, count):
    """
    :param word: Random word selected
    :param guessed: hint variable replacing '-' with word character
    :param input_char: user input character
    :param count: lives left
    :return:
    """
    if input_char not in word:
        print("No such letter in the word")
        count -= 1
    if input_char in guessed:
        print("No improvement")
        count -= 1
    for index, temp in enumerate(word_selected):
        if input_char == temp:
            guessed[index] = input_char

    typed.add(input_char)
    return count


print("H A N G M A N")
while game_loop is True:
    menu = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if menu == 'play':
        lives = 8
        while lives != 0:
            print(f"\n{''.join(guess)}")
            if guess == list(word_selected):
                print("You guessed the word!\nYou survived!")
                word_selected, guess, typed, lives = game_reset(word_selected, guess, typed, lives)
                break
            elif lives == 0:
                print("You are hanged!")
            user_input = input("Input a letter: ")

            if validate(user_input):
                lives = live_decrement(word_selected, guess, user_input, lives)
                if lives == 0:
                    print("You are hanged!")
                    word_selected, guess, typed, _ = game_reset(word_selected, guess, typed, lives)
            else:
                continue

    elif menu == 'exit':
        quit()


