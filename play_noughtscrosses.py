# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe/Noughts and Crosses

@author: vipashabansal
"""
from noughtscrosses import OXGame as game

#Print Welcome Message and Instructions
print('Welcome to Noughts and Crosses/Tic Tac Toe. This is a two player game.\n'
      'One player will be \'X\' and the other will be \'O\'. \n'
      'To make a move, select the number for your chosen space as seen below.\n')

print('1 2 3 \n')
print('4 5 6 \n')
print('7 8 9 \n')

my_game = game()

player = 'X'

#Alternately ask players to make their next move until a player wins or there is
#a draw. Allow players to request a list of available moves if they are unsure.
while my_game.check_win() is False and my_game.get_num_moves() < 9:
    player = my_game.whose_turn()
    print('It is player {}\'s turn. \n'.format(player))
    
    choice = input("Type \'Make Move\' or \'See Moves\' to continue. \n")
    
    available_moves = my_game.get_available_moves()
    
    if choice.lower().strip() == 'see moves':
        print("\nMoves currently available are {} \n".format(available_moves))
    elif choice.lower().strip() == 'make move':
        space = input("Enter your chosen space: ")
        print("\n")
        
        if int(space) not in range(1, 10):
            print("That's not a valid move. Enter a number between 1 and 9.\n")
        elif space not in available_moves:
            print("That space is already taken. Please try again. \n")
        else:
            my_game.make_move(player, space)
    else:
        print("that is not a valid response")
            
#Determine who has won and let the players know
moves = my_game.get_num_moves()
if moves == 9 and my_game.check_win() == False:
    print('It\'s a draw! Nobody wins.')
elif player == 'X':
    print('Player X wins! This game took {} moves'.format(moves))
else:
    print('Player O wins! This game took {} moves'.format(moves))
    
    
    
    