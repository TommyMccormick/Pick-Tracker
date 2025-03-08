# This class represnts the grid for weekly NFL picks
# import sys
# import os

import player

class Grid():
    def __init__(self, week, name, selection):
        self.week = week
        self.name = name
        self.selection = selection

    # self.week = 1
    # self.name = "big tito"
    # self.selection = "birds"
    def print_grid(self):
        # initial positions for the board
        board_setup = [
            ["title", "name", "name", "name", "name", "name", "name"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"], 
            ["game", "selection", "selection", "selection", "selection", "selection", "selection"]
        ]
                # # Place pieces on the board in the correct spaces
                # piece = starting_positions[row][col]
        for row in range(17):
            row_print = [] # collect values for each row
            for col in range(7):
                square = board_setup[row][col]

                if square == "title":
                    row_print.append(f'NFL Week {self.week}')
                elif square == "game":
                    row_print.append("x(0-0) @ y(0-0)")
                elif square == "name":
                    #self.name = player.__name__
                    row_print.append(f'{self.name}')
                elif square == "selection":
                    row_print.append(f'{self.selection}')
                else:
                    pass
            print("\t".join(row_print))

test = Grid(1, "BIG TITO", "birds")
test.print_grid()