import random
import diceRoll
import tupleOut
import fixedDice
import time
    
def show_time(event):
    current_time = time.localtime()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    print(f"{event} at {timestamp}")

# This programs the process of whether or not the player should be allowed to reroll their turn depending on if they
# tupled out or rolled a fixed dice
def player_turn(player, scores):
    print(f"\nPlayer {player + 1}'s turn ==============================================================================================")
    time.sleep(1)
    roll = diceRoll.dice_roll()
    if_fixed = fixedDice.fixed_dice(roll)

    while True:
        print(f"Dice rolled: {roll}")
        time.sleep(1)
        if tupleOut.tuple_out(roll):
            print("You tupled out! Your score for this round is 0 :(")
            return 0
        if if_fixed:
            print(f"{[roll[i] for i in if_fixed]}")
        while True:
            try:
                reroll_chance = input("\nDo you want to reroll? (yes/no): ").strip().lower()
                if reroll_chance not in {'yes', 'no'}:
                    raise ValueError("Invalid input. Please type 'yes' or 'no'.")
                break
            except ValueError as e:
                print(e)
        
        if reroll_chance == 'no':
            total_score = sum(roll)
            print(f"Scored {total_score} points")
            return total_score
        
        for i in range(3):
            if i not in if_fixed:
                roll[i] = random.randint(1, 6)
        if_fixed = fixedDice.fixed_dice(roll)

# This function keeps track of the players scores while saving past scores and updating them with each roll
def game(target_score):
    show_time("The game has begun.")
    scores = [0, 0]
    current_player = 0

    while all(score < target_score for score in scores):
        print(f"\nScores: \nPlayer 1 = {scores[0]}, Player 2 = {scores[1]}")
        turn_score = player_turn(current_player, scores)
        scores[current_player] += turn_score
        current_player = 1 - current_player

    if scores[0] >= target_score:
        winner = 1
    else:
        winner = 2
    
    print("\nTime for the final scores...")
    time.sleep(3)
    print(f"\nPlayer 1 scored...") 
    time.sleep(3)
    print(f"{scores[0]}")
    time.sleep(2)
    print("\nAnd Player 2 scored...")
    time.sleep(3)
    print(f"{scores[1]}")
    time.sleep(2)
    print(f"Player {winner} wins!")

    show_time("Game ended.")

# Initializing game. First to reach a specific goal (in this case 50) wins the game
game(target_score = 50)