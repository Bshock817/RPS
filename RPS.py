# A Simple Rock, Paper, Scissors game played on your terminal!, First to get 3 points wins!! 
from random import randint
my_score = 0
AI_score = 0
AI_hand =["Rock", "Paper","Scissors"]

while True:
    I_got = input('Give "R" for Rock, "P" for Paper or "S" for Scissors: ')
    AI_got = AI_hand[randint(0,2)]

    #Rock
    if I_got == 'R' and AI_got == 'Paper':
        print('\nYou Chose Rock and the AI chose Paper. AI Wins!\n')
        AI_score += 1
        print('You have {} points and AI has {} Points'.format(my_score, AI_score))
    elif I_got == 'R' and AI_got =='Scissors':
        print('\nYou Chose Rock and the AI chose Scissors. You Win!\n')
        my_score += 1
        print('You have {} points and AI has {} Points'.format(my_score, AI_score))
        
    #Paper
    elif I_got == 'P' and AI_got == 'Scissors':
        print('\nYou Chose Paper and the AI chose Scissors. AI Wins!\n')
        AI_score += 1
        print('You have {} points and AI has {} Points'.format(my_score, AI_score))
    elif I_got == 'P' and AI_got =='Rock':
        print('\nYou Chose Paper and the AI chose Rock. You Win!\n')
        my_score += 1
        print('You have {} points and AI has {} Points'.format(my_score, AI_score))

    #Scissors    
    elif I_got == 'S' and AI_got == 'Rock':
        print('\nYou Chose Scissors and the AI chose Rock. AI Wins!\n')
        AI_score += 1
        print('You have {} points and AI has {} Points'.format(my_score, AI_score))
    elif I_got == 'S' and AI_got =='Paper':
        print('\nYou Chose Scissors and the AI chose Paper. You Win!\n')
        my_score += 1
        print('You have {} points and AI has {} Points'.format(my_score, AI_score))

    #Tie
    else:
        print("\nPicked the same hand, try again\n")


    #Check the score
    if my_score == 3:
        print('You Won!!')
        break
    elif AI_score == 3:
        print('You Lose, AI Won!!')
        break
print('Game Over!')