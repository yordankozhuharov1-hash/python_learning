# Predefined quantities of products and machine resources
coffee_recipes = {
    "black_coffee": {"water_ml": 70, "coffee_g": 20, "milk_ml": 0, "cost": 0.80},
    "latte": {"water_ml": 30, "coffee_g": 18, "milk_ml": 200, "cost": 1.50},
    "flat_white": {"water_ml": 30, "coffee_g": 18, "milk_ml": 120, "cost": 2.00},
}
 
resources_machine = {
    "water_in_machine": 1000,
    "coffee_in_machine": 400,
    "milk_in_machine": 1000,
}
 
COIN_VALUES = {"half": 0.50, "quarter": 0.25, "penny": 0.10}
coin_container = 0
 
MENU = {1: "black_coffee", 2: "latte", 3: "flat_white"}
 
 
def report(resources):
    """Return a readable string of current machine resource levels."""
    return (
        f"\nYou have\n"
        f" Water: {resources['water_in_machine']} ml\n"
        f" Coffee: {resources['coffee_in_machine']} g\n"
        f" Milk: {resources['milk_in_machine']} ml"
    )
 
 
def has_enough_resources(recipe):
    """Return True only if the machine has enough of every ingredient."""
    if resources_machine["water_in_machine"] < recipe["water_ml"]:
        print("Sorry, not enough water.")
        return False
    if resources_machine["coffee_in_machine"] < recipe["coffee_g"]:
        print("Sorry, not enough coffee.")
        return False
    if resources_machine["milk_in_machine"] < recipe["milk_ml"]:
        print("Sorry, not enough milk.")
        return False
    return True
 
 
def collect_coins():
    """Ask the user to insert coins and return the total amount inserted."""
    print("Please insert coins.")
    total = 0
    total += int(input("How many halves (0.50)?: ")) * COIN_VALUES["half"]
    total += int(input("How many quarters (0.25)?: ")) * COIN_VALUES["quarter"]
    total += int(input("How many pennies (0.10)?: ")) * COIN_VALUES["penny"]
    return round(total, 2)
 
 
def make_order(drink_name):
    """Deduct the recipe's ingredients from the machine's resources."""
    recipe = coffee_recipes[drink_name]
    resources_machine["water_in_machine"] -= recipe["water_ml"]
    resources_machine["coffee_in_machine"] -= recipe["coffee_g"]
    resources_machine["milk_in_machine"] -= recipe["milk_ml"]
 
 
def process_order(choice):
    """Handle one full order: check stock, take payment, dispense drink."""
    global coin_container
 
    drink_name = MENU[choice]
    recipe = coffee_recipes[drink_name]
 
    if not has_enough_resources(recipe):
        return
 
    money = collect_coins()
    if money >= recipe["cost"]:
        change = round(money - recipe["cost"], 2)
        coin_container += recipe["cost"]
        make_order(drink_name)
        print(f"\nHere is your {drink_name.replace('_', ' ')}! Enjoy.")
        if change > 0:
            print(f"Here is {change} in change.")
    else:
        print("Sorry, that's not enough money. Money refunded.")
 
 
def main():
    while True:
        choice = input(
            "\nWhat would you like?\n"
            " Black Coffee [1]\n Latte [2]\n Flat White [3]\n"
            " Report [r]\n Exit [0]\n> "
        )
 
        if choice == "0":
            print("Goodbye!")
            break
        elif choice.lower() == "r":
            print(report(resources_machine))
        elif choice in ("1", "2", "3"):
            process_order(int(choice))
        else:
            print("Invalid input, please try again.")
 
 
if __name__ == "__main__":
    main()