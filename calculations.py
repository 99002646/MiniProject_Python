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
    def sort_names_in_asc(self):
        """
        Function to sort names in ascending order.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[1])
        return sorted(new_list)
    
    def sort_titles_in_desc(self):
        """
        Function to sort players titles in descending order.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[4])
        return sorted(new_list, reverse=True)

    
    

DATA = Calculations('top_women_chess_players_aug_2020.csv')
print(DATA.import_data())
print(DATA.display())
print(DATA.sort_names_in_asc())
print(DATA.sort_titles_in_desc())

