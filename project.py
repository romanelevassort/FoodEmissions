'''
class Diet:
    def __init__(self, name, food_items):
        self.name = name
        self.food_items = food_items

    def total_emissions(self, data):
        ...



def main():
 ...
def load_food_data(filepath):
 ...
def calculate_carbon_footprint(food_list, data):
 ...
def compare_diets(diet1, diet2, data):
 ...
if __name__ == "__main__":
 main()
'''

import pandas as pd
food_emissions = r"C:\Users\Utilizador\Desktop\FoodEmissions\agribalyse_food_emissions.csv"
df = pd.read_csv(food_emissions)

print(df.head())
