import random

#============================================
#               check_unique
#============================================
def check_unique(unique_digits, number_string, digit):
    """check if number needs to be unique and if it is unique"""
    return digit in number_string if unique_digits else False

#============================================
#           first_digit_is_not_ok
#============================================
def first_digit_is_not_ok(digit, allow_leading_zero, number_string):
    """check if the first number is allowed to be zero - and if not, it is zero"""
    return digit == 0 and len(number_string) == 0 and not allow_leading_zero

#============================================
#               generate_secret
#============================================
def generate_secret(length: int = 4, *, unique_digits: bool = True, allow_leading_zero: bool = False, rng: random.Random | None = None) -> str:

     secret = ""

     while len(secret) < length:

        #this will return the digit that will be added to the string!
        digit = str(random.randint(0, 9))

        #this will check if the first number is allowed to be zero!
        if first_digit_is_not_ok(digit, allow_leading_zero, secret):
            continue
        #if returned true it will not be added to the string!
        if check_unique(unique_digits, secret, digit):
            continue

        secret += digit

     return secret

