def prompt_user_choice():
    user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    return user_choice


def check_resources(requested_drink, required_resources, machine_resources):
    """Checks if the Coffee Machine has sufficient resources to complete the order. If so,
    function returns true. If not, the function tells the user what ingredients are lacking
    and returns false."""
    resources_sufficient = True

    if machine_resources['water'] < required_resources[requested_drink]['ingredients']['water']:
        water_check = False
        resources_sufficient = False
    else:
        water_check = True

    if requested_drink != 'espresso':
        if machine_resources['milk'] < required_resources[requested_drink]['ingredients']['milk']:
            milk_check = False
            resources_sufficient = False
        else:
            milk_check = True

    if machine_resources['coffee'] < required_resources[requested_drink]['ingredients']['coffee']:
        coffee_check = False
        resources_sufficient = False
    else:
        coffee_check = True

    if resources_sufficient == False:
        print("Sorry, the machine is too low on resources to make that drink. Too low on: ")
        if water_check == False:
            print('Water')
        if not milk_check:
            print('Milk')
        if not coffee_check:
            print('Coffee')
        return False
    else:
        return True


def brew_beverage(requested_drink, required_resources, machine_resources):
    machine_resources['water'] = machine_resources['water'] - required_resources[requested_drink]['ingredients'][
        'water']

    if requested_drink != 'espresso':
        machine_resources['milk'] = machine_resources['milk'] - required_resources[requested_drink]['ingredients']['milk']

    machine_resources['coffee'] = machine_resources['coffee'] - required_resources[requested_drink]['ingredients'][
        'coffee']

    print(f'Here is your {requested_drink}! Enjoy!')




def check_money(requested_drink, required_resources, machine_resources):
    """Function checks for user entered money. If user inserts enough money, function calls
    function brew_beverage. If not, function prompts user to try another order."""
    print('How many coins do you have? (quarters, dimes, nickels)')
    quarters = int(input('Quarters: '))
    dimes = int(input('Dimes: '))
    nickels = int(input('Nickels: '))

    user_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05)
    user_money = "{:.2f}".format(user_money)

    drink_cost = required_resources[requested_drink]['cost']
    drink_cost_str = "{:.2f}".format(drink_cost)

    change = float(user_money) - drink_cost
    change = "{:.2f}".format(change)

    print(f"You gave ${user_money}. The drink you requested costs ${drink_cost_str}")
    if float(user_money) == drink_cost:
        print('You gave me enough. Working on your drink now!')
        # Add money to computer profit
        machine_resources['profit'] = machine_resources['profit'] + drink_cost
        return brew_beverage(requested_drink, required_resources, machine_resources)

    elif float(user_money) > drink_cost:
        print(f'You gave me extra! Your change is ${change}. Working on your drink now!')
        machine_resources['profit'] = machine_resources['profit'] + drink_cost
        return brew_beverage(requested_drink, required_resources, machine_resources)

    else:
        print("Sorry, that's not enough money. Please make another choice.")
        return
