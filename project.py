#pip install pandas
import pandas as pd


# Class

class Diet:
    def __init__(self, name):
        self.name = name
        self.food_items = {}  # {food_name: quantity}

    #add food and its quantity to the diet
    def add_food(self, food, quantity):
        self.food_items[food] = self.food_items.get(food, 0) + quantity

    #modify the diet : remove food or change the quantity
    def modify_food(self, food, quantity):
        if food not in self.food_items:
            print(f"Warning: '{food}' not found in diet")
            return
        if quantity <= 0:
            print("Quantity must be positive")
            return
        self.food_items[food] -= quantity
        # If the quantity becomes zero or negative, the food item is removed.
        if self.food_items[food] <= 0:
            del self.food_items[food]

    #displays all foods and their quantities currently in the diet
    def list_foods(self):
        if not self.food_items:
            print("No foods in this diet.")
            return

        print("\nFoods in the diet:")
        for i, (food, quantity) in enumerate(self.food_items.items(), start=1):
            print(f"{i}. {food} - {quantity:.0f} g")

    #Calculates the total carbon footprint of the diet using emission factors
    def total_emissions(self, emissions_data):
        return calculate_carbon_footprint(self.food_items, emissions_data)



# Data loading from a csv

def load_food_data():
    df = pd.read_csv("agribalyse.csv", sep=";")
    df = df.rename(columns={
        'Name': 'Food_Name',
        'Changement climatique (kg CO2 eq/kg de produit)': 'Emission'
    })
    df['Emission'] = pd.to_numeric(df['Emission'].str.replace(',', '.'), errors='coerce')
    return dict(zip(df['Food_Name'], df['Emission']))


#Calculate total carbon footprint of food items and create a dictionnary with all foods, their quantities and their footprint

def calculate_carbon_footprint(food_items, emissions_data):
    footprint = 0.0
    result_table = {}
    for food,quantity in food_items.items():
        emission = emissions_data.get(food) #float
        if emission is None:
            print(f"Warning: emission data not found for {food}")
            continue
        footprint += emission*quantity/1000
        if food not in result_table:
            result_table[food] = []
            result_table[food].append(quantity)
            result_table[food].append(emission*quantity/1000)
    return footprint,result_table




# Autocomplete the choice to fit the list of the csv (use the prefixe to find the food in the list)

def suggestions(emissions_data, prefix):
    prefix = prefix.lower()
    return [food for food in emissions_data if food.lower().startswith(prefix)]


def choose_food(emissions_data):
    while True:
        prefix = input("Type the first letters of the food item:").strip()
        matches = suggestions(emissions_data, prefix)

        if not matches:
            print("❌ No match found.")
            continue

        for i, food in enumerate(matches[:10], start=1):    #show the firts 10 matches and create an index to choose the food
            print(f"{i}. {food}")

        choice = input("Choose a number (or press ENTER to start again): ").strip()
        if not choice:
            continue

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(matches[:10]):
                return matches[index]

        print("❌ Invalid choice.")

#Allows the user to select an existing food item from a given diet to modify or remove quantities.
def choose_food_from_diet(diet):
    foods = list(diet.food_items.keys())

    if not foods:
        print("❌ No foods to modify.")
        return None

    for i, food in enumerate(foods, start=1):   #show the foods in the diet

        choice = input("Choose a food number: ").strip() #to choose the food the user want to modify in the diet
        print(f"{i}. {food}")
    if not choice.isdigit():
        print("❌ Invalid choice.")
        return None

    index = int(choice) - 1
    if index < 0 or index >= len(foods):
        print("❌ Invalid choice.")
        return None

    return foods[index]


# Main program

def main():
    emissions_data = load_food_data()

    diet1 = Diet("Diet 1")
    diet2 = Diet("Diet 2")

    print("=== Food Carbon Footprint Calculator ===")

    while True:
        print("\n1. Add a food item to Diet 1")
        print("2. Add a food item to Diet 2")
        print("3. Modify Diet 1")
        print("4. Modify Diet 2")
        print("5. Display results")
        print("6. Quit")

        choice = input("Your choice : ").strip()

        if choice in ("1", "2"):    #users choose to add food items in one of the 2 diets
            diet = diet1 if choice == "1" else diet2
            print(f"\nAdd to {diet.name}")

            food = choose_food(emissions_data)  #show the food that match with the list

            try:
                quantity = float(input("Quantity (g) : "))
                if quantity <= 0:
                    raise ValueError
            except ValueError:
                print("❌ Invalid quantity.")
                continue

            diet.add_food(food, quantity)
            print(f"✅ {food} ({quantity} g) added to {diet.name}")

        elif choice in ("3", "4"):  # users choose to modify one of the two diets
            diet = diet1 if choice == "3" else diet2
            print(f"\nModify {diet.name}")

            food = choose_food_from_diet(diet)      #user choose food in the diets list of food
            if food is None:
                continue

            max_quantity_g = diet.food_items[food]

            try:
                quantity_g = float(
                input(f"Quantity to remove (g) (max {max_quantity_g:.0f} g): ")
                )
                if quantity_g <= 0 or quantity_g > max_quantity_g:
                    raise ValueError
            except ValueError:
                print("❌ Invalid quantity.")
                continue

            diet.modify_food(food, quantity_g)

            print(f"✅ {food} ({quantity_g} g) removed from {diet.name}")


        elif choice == "5":
            e1,result_1 = diet1.total_emissions(emissions_data)
            e2,result_2 = diet2.total_emissions(emissions_data)
            table_diet1 = pd.DataFrame.from_dict(result_1, orient='index', columns=["Quantity (g)", "Footprint (kg Co2e)"])
            title_1 = "Carbon footprint of Diet 1"
            table_diet2 = pd.DataFrame.from_dict(result_2, orient='index', columns=["Quantity (g)", "Footprint (kg Co2e)"])
            title_2 = "Carbon footprint of Diet 2"

        #show the result of the carbon footprint calcul
            print("\n=== Results ===")
            print(f"\n{title_1}\n" + "-" * len(title_1))
            print(f"\n{diet1.name} : {e1:.2f} kg CO2e")
            print(table_diet1.to_string())
            print(f"\n{title_2}\n" + "-" * len(title_2))
            print(f"\n{diet2.name} : {e2:.2f} kg CO2e")
            print(table_diet2.to_string())


            if e1 < e2:
                print("\n🌱 Diet 1 has a lower carbon footprint.")
            elif e2 < e1:
                print("\n🌱 Diet 2 has a lower carbon footprint.")
            else:
                print("\n⚖️ Both diets have the same impact.")

        elif choice == "6":
            print("Bye 👋")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
