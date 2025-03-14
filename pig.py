import random

def roll_die():
    return random.randint(1, 6)

def play_game():
    random.seed(0)
    target_score = 100
    scores = [0, 0]
    player = 0

    print("Welcome to Pig!")

    while max(scores) < target_score:
        turn_total = 0
        print(f"Player {player + 1}'s turn! Current score: {scores[player]}")

        while True:
            roll = roll_die()
            print(f"Player {player + 1} rolled a {roll}.")

            if roll == 1:
                print("Rolled a 1! No points for this turn.")
                turn_total = 0
                break
            else:
                turn_total += roll
                print(f"Turn total: {turn_total}, Overall score: {scores[player]}")

                decision = input("Roll again (r) or hold (h)? ").strip().lower()
                if decision == 'h':
                    scores[player] += turn_total
                    print(f"Player {player + 1} holds. New total score: {scores[player]}\n")
                    break

        if scores[player] >= target_score:
            print(f"Player {player + 1} wins with {scores[player]} points!\n")
            break

        player = 1 - player

    print("Game over! Thanks for playing.")

if __name__ == "__main__":
    play_game()
