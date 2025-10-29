
def is_new_guess(guess: str, history: set[str]) -> bool:
    return guess in history


def unique_and_valid_input(guess, length, unique_digits):

    if len(set(guess)) == len(guess):
        return valid_user_input(guess, length)

    return False, "Please enter unique digits only!"


def valid_user_input(guess, length):

    if len(guess) == length and int(guess):
        return True, "The input is valid!"
    return False, "The length is not correct!"


def is_valid_guess(guess: str, length: int, *, unique_digits: bool = True) -> tuple[bool, str]:

   try:

       if unique_digits:
           return unique_and_valid_input(guess, length, unique_digits)
       else:
           return valid_user_input(guess, length)

   except:
       return False, "Unable to convert a non int to a int"

