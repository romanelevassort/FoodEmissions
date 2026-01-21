# FoodEmissions
(Diet Carbon Footprint Calculator (Console Version))
Romane LEVASSORT

## Description

This project is a command-line application that allows you to compare the carbon footprint of two different diets.
Users can add foods with their respective quantities to each diet, benefiting from simple autocomplete suggestions in the terminal based on a real dataset (`agribalyse.csv`).
Users can also modify each diet to remove food or chnge the quantity.
The application then calculates the total carbon emissions (in kg CO₂ equivalent) for each diet and indicates which one has the lower environmental impact.

---

## Project composition

* Information ("README.md")
* Base data ("agribalyse.csv")
* Programs ("project.py" and "test_project.py")
* Pip-installable libraries ("requirements.txt")

---

## Features

* Loads carbon emission data from the agribalyse.csv file.
* Food selection with autocomplete suggestions in the console (up to 10 matches).
* Add foods and quantities (stored in kilograms) to two separate diets.
* Modify diets by removing foods or decreasing quantities.
* Calculates and displays the total carbon emissions for each diet.
* Compares both diets and highlights the most climate-friendly option.

---


## Installation

1. Clone this repository or download the files.
2. Make sure the `agribalyse.csv` file is located in the same folder as the Python script.
3. Run the main script:

```bash
python project.py
```

---

## Usage

* The program displays a menu allowing users to:
* Add foods to Diet 1 or Diet 2
* Modify existing diets
* Display and compare results
* Quit the program
* To add a food, type the first letters of its name.
* Select a food from the suggested list by entering its number.
* Enter the quantity in grams.
* Repeat the process to build each diet.
* Display the results to compare the total carbon footprint of both diets and of each foods of the diet.

---

## Project Structure

* `project.py`: Main script containing all the logic.
* `test_project.py`: Test script for the project.py script.
* `agribalyse.csv`: CSV file with carbon emission data per food item (must be provided or downloaded).

---

## Program Structure

The developed program (project.py) is a console-based application that allows users to compare the carbon footprint of two diets by adding, modifying, and managing food items and their quantities.

The program uses the following main components:

* Class Diet:
Represents a diet with a name and a dictionary of food items and quantities (in grams).

** add_food(food, quantity): Adds the specified quantity of a food to the diet.

** modify_food(food, quantity): Removes a specified quantity of a food from the diet; if quantity reaches zero or below, the food is removed completely.

** list_foods(): Displays all foods and their quantities currently in the diet.

** total_emissions(emissions_data): Calculates the total carbon footprint of the diet using emission factors.

* Function load_food_data():
Loads food emission data from the agribalyse.csv file, processes it, and returns a dictionary mapping food names to their carbon emission values (kg CO₂e per kg food).

* Function calculate_carbon_footprint(food_items, emissions_data):
Calculates the total carbon footprint of the given food items based on quantities and emission factors. Quantities are stored in grams, so appropriate conversion to kilograms is applied during calculation. Also returns a detailed breakdown per food item.

* Function suggestions(emissions_data, prefix):
Provides autocomplete suggestions for food items based on the user-input prefix (case-insensitive), returning up to 10 matches.

* Function choose_food(emissions_data):
Interactive console function allowing users to type the start of a food’s name and select it from autocomplete suggestions.

* Function choose_food_from_diet(diet):
Allows the user to select an existing food item from a given diet to modify or remove quantities.


