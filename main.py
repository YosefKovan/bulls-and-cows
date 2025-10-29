from game.secret import generate_secret
from game.validate import is_valid_guess

#============================================
#                   play
#============================================
def play():
    secret = generate_secret(4)
    print(is_valid_guess("1231", 4, unique_digits=True))


#============================================
#                   main
#============================================
if __name__ == "__main__":
    play()