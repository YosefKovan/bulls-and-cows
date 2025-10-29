from game.secret import generate_secret


def game_manager():
    secret = generate_secret(4)
    print(secret)
