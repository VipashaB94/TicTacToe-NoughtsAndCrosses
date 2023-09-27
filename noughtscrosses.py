# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe/Noughts and Crosses

@author: vipashabansal
"""
    
class OXGame:
    
    #make dictionary corresponding spaces on the board to their coordinates
    space_chart = {'1': [0, 0], '2': [0, 1], '3': [0, 2], 
                   '4': [1, 0], '5': [1, 1], '6': [1, 2], 
                   '7': [2, 0], '8': [2, 1], '9': [2, 2]}
    
    def __init__(self):
      self.board = [[' ' for i in range(3)] for i in range(3)]
      self.available_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
      self.turn = 'X'
      self.moves = 0
    
    def make_move(self, player, space):

       coords = OXGame.space_chart.get(space)
       self.board[coords[0]][coords[1]] = player
       self.available_moves.remove(space)
           
       print(self.board[0])
       print(self.board[1])
       print(self.board[2])
       print("\n")
           
       self.moves += 1
       if player == 'X':
           self.turn = 'O'
       else:
           self.turn = 'X'
   
    
    def get_available_moves(self):
        return self.available_moves
    
    
    def check_win(self):
        win = False
        for i in range(3):
            win = (self.board[i][0] == self.board[i][1] and self.board[i][0] \
                   == self.board[i][2] and self.board[i][0] != ' ') \
                   or (self.board[0][i] == self.board[1][i] and self.board[0][i]\
                       == self.board[2][i] and self.board[0][i] != ' ')
            if win:
                return win
            
        win = (self.board[0][0] == self.board[1][1] and self.board[0][0] \
               == self.board[2][2] and self.board[0][0] != ' ') \
               or (self.board[2][0] == self.board[1][1] and self.board[2][0] \
                   == self.board[0][2] and self.board[2][0] != ' ')
            
        return win
            

    def whose_turn(self):
        return self.turn
    
    def get_num_moves(self):
        return self.moves

