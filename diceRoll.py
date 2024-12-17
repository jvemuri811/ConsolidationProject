# Rolls the dice three times to initialze points
import random

def dice_roll():
    return [random.randint(1, 6) for _ in range(3)]

# def test_dice_roll():
#     random.seed(42)
#     result = dice_roll()
#     print(f"Dice rolled: {result}")

#     # Dice roll should return exactly 3 values and all dice rolls should be between 1 and 6.
#     assert len(result) == 3
#     assert all(1 <= value <= 6 for value in result)

# test_dice_roll()