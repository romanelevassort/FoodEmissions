# FoodEmissions
(Diet Carbon Footprint Calculator (Console Version))

## Description

This project is a command-line application that allows you to compare the carbon footprint of two different diets.
Users can add foods with their respective quantities to each diet, benefiting from simple autocomplete suggestions in the terminal based on a real dataset (`agribalyse.csv`).
The application then calculates the total carbon emissions (in kg CO₂ equivalent) for each diet and indicates which one has the lower environmental impact.

---

## Features

* Loads carbon emission data from the `agribalyse.csv` file.
* Food entry with autocomplete suggestions in the console (up to 10 matches).
* Add foods and quantities (in kg) to two separate diets.
* Calculates and displays the total emissions for each diet.
* Simple comparison and recommendation of which diet to prioritize.
* User-friendly console interface.

---


## Installation

1. Clone this repository or download the files.
2. Make sure the `agribalyse.csv` file is located in the same folder as the Python script.
3. Run the main script:

```bash
python diet_carbon_console.py
```

---

## Usage

* The program shows a menu to add foods to either diet, display results, or quit.
* To add food, start typing the first letters. The program will suggest up to 10 matches.
* Choose a food by entering its corresponding number.
* Enter the quantity in kilograms.
* Repeat for as many foods as you want in each diet.
* Display results to compare the carbon footprint.
* Quit the program using the provided menu option.

---

## Project Structure

* `project.py`: Main script containing all the logic.
* `agribalyse.csv`: CSV file with carbon emission data per food item (must be provided or downloaded).

---

## License

This project is open source and free to use.

---

