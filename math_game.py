# Math Practice Game
import random
from time import time as t

print('Project - Math Tutor')

num_q = int(input('How many questions would you like: '))
num_1 = int(input('Which multiplication table would you like to practice: '))
max_num = int(input('what is the highest number you would like to practice with: '))
score = 0
answer_list = []

start = t()
for q in range(num_q):
    num_2 = (random.randint(1, max_num + 1))
    ans = num_1 * num_2
    u_ans = int(input(f'{num_1}x{num_2}= '))
    answer_list.append(f'{num_1}x{num_2}= {ans}, you answered {u_ans}.')
    if u_ans == ans:
        score += 1
    end = t()

print(f'You got {score} out of {num_q} correct! ({round(score / num_q * 100)}% score). \n'
      f'You took {round(end - start, 1)} seconds total.')
for a in answer_list:
    print(a)