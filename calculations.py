"""
This class is responsible for various calculations on the top_women_chess_players dataset.
"""
from dataset import Players
class Calculations(Players):
    """
    This is a constructor which initialized the base class constructor i.e Players
    """
    def __init__(self, my_list):
        Players.__init__(self, my_list)
