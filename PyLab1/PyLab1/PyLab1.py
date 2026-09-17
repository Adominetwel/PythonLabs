import random
def start_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    while True:
        try:
            user_guess = int(input())
            attempts += 1
            if user_guess < secret_number:
                print("Загаданное число больше.")
            elif user_guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Вы угадали число {secret_number}!")
                print(f"Количество попыток: {attempts}")
                break
        except ValueError:
            pass
    
start_game()