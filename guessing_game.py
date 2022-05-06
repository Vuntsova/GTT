SUCCESS_MSG = "You guessed right! The secret word is: "
FAIL_MSG = "You guessed wrong! The secret word is: "


def guess_secret_word(secret_word, guess_limit):
    attempts = 0
    while attempts < guess_limit:
        attempts += 1
        guessed_word = str(input("What's your Guess: "))

        if str(secret_word) == str(guessed_word):
            return print(SUCCESS_MSG + str("'" + secret_word + "'"))
        elif attempts == guess_limit:
            return print(FAIL_MSG + str("'" + secret_word + "'"))


guess_secret_word("word", 3)
