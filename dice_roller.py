import random

def main():
  # numbers list
  numbers = ["1",'2','3','4','5','6','7','8','9']

  # get rolls
  dice_rolls = input("How many dice to roll: ")
  # check input
  if len(dice_rolls) < 1 or dice_rolls not in numbers:
    dice_rolls = 0
  else:
    dice_rolls = int(dice_rolls)
  
  # get size to roll
  dice_size = input("How many sides to the dice: ")
  # check input
  if len(dice_size) < 1 or dice_rolls not in numbers:
    dice_size = 0
  else:
    dice_size = int(dice_size)
  dice_sum = 0

  # roll and print
  for i in range(dice_rolls):
    roll = random.randint(1,dice_size)
    if roll == 1:
      message = ". Critical Fail."
    elif roll == dice_size:
      message = ". Critical Success."
    else:
      message = "."
    print(f'{i+1}.You rolled a {roll}' + message)
    dice_sum = dice_sum + roll
  print(f"Total: {dice_sum}")

# run main
if __name__== "__main__":
  main()