# Dice Game

## Rules

### Objective
- Players aim to score the most points or reach the target score (default is 50).

### Gameplay
1. Players take turns rolling three dice.
2. Special rules for dice rolls:
   - Tuple Out: If all three dice show the same value, the player "tuples out" and ends their turn with 0 points.
   - Fixed Dice: If two dice show the same value, they are "fixed" and cannot be rerolled.
3. Players can reroll unfixed dice as many times as they like or stop to lock in their score.

### Turn End
- If a player stops voluntarily, their score for the turn is the sum of all three dice.
- If a player "tuples out," their score for the turn is 0.

### Features
- time.sleep() allows the players to process their decision to reroll and increases readability in the game
- time.localtime() and time.strftime() allows the player to know how long they have been gaming for so they dont lose track of time

## Instructions for how to play

### Running the Game
1. Save the Python script to a file (e.g., `ConsolidationProject.py`).
2. Open a terminal or command prompt.
3. Run the script:
   python ConsolidationProject.py
