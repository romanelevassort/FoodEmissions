import pytest
from project import load_food_data, calculate_carbon_footprint, suggestions

#Test load_food_data()
def test_load_food_data():
    emissions = load_food_data()
    # Must return a non-empty dictionary
    assert isinstance(emissions, dict)
    assert len(emissions) > 0
    # Some expected keys present
    assert any("juice" in food.lower() for food in emissions.keys())
#checks that the data loaded by load_food_data() is a non-empty dictionary and contains at least one expected food item


# Test calculate_carbon_footprint()
def test_calculate_carbon_footprint():
    emissions_data = {
        "apple": 0.5,
        "banana": 0.9,
        "beef": 60.0,
    }
    food_items = {
        "apple": 2000,    # 2 kg apples
        "banana": 1500, # 1.5 kg bananas
        "beef": 100,  # 100 g beef
    }
    footprint, result_table = calculate_carbon_footprint(food_items, emissions_data)
    expected_footprint = (2000/1000 * 0.5 + 1500/1000 * 0.9 + 100 /1000 * 60.0)

    assert abs(footprint - expected_footprint) < 1e-6, "Footprint calculation error"

    expected_result_table = {
        "apple": [2000, 2000/1000 * 0.5],
        "banana": [1500, 1500/1000 * 0.9],
        "beef": [100, 100/1000 * 60.0],
    }

    assert result_table == expected_result_table, "Result table does not match expected"

#verifies the correct calculation of the total carbon footprint for a small sample of food items with known emission values. It compares the function’s output to the expected weighted sum.

#Test suggestions()
def test_suggestions():
    emissions_data = {
        "apple": 0.5,
        "apricot": 0.7,
        "banana": 0.9,
        "beef": 60.0,
    }
    # Test prefixe "ap"
    sugg = suggestions(emissions_data, "ap")
    assert "apple" in sugg
    assert "apricot" in sugg
    assert "banana" not in sugg

    # Test prefixe with capital letters
    sugg = suggestions(emissions_data, "Ap")
    assert "apple" in sugg
    assert "apricot" in sugg

    # Test prefixe without correspondance
    sugg = suggestions(emissions_data, "xyz")
    assert sugg == []
#ensures that the suggestions() function:
#Returns all food items starting with the given prefix (case insensitive)
#Returns an empty list when no matches are found
