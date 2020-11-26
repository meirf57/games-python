import random

def main():
  dice_rolls = 2
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_sum = dice_sum + roll
  print(f"Totel: {dice_sum}")

if __name__== "__main__":
  main()