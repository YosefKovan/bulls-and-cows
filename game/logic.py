
#def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool):

def bull(index, secret, guess):
    """if the indexes equal it returns true"""
    return secret[index] == guess[index]

def cow(index, guess, secret):
    """checks if the letter is in the secret"""
    return guess[index] in secret

def score_guess(secret: str, guess: str) -> tuple[int, int]:
    """counts the bulls and counts and returns the results"""
    bulls, cows = 0, 0

    for index in range(0, len(guess)):

        if bull(index, secret, guess):
            bulls += 1
        elif cow(index, secret, guess):
            cows += 1

    return bulls, cows