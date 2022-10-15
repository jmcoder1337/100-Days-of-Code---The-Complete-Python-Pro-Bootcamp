from machine_data import MENU, resources
from machine_programs import prompt_user_choice, check_resources, brew_beverage, check_money

resources["profit"] = 0

machine_on = True



# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

print((MENU['espresso']['cost'])-1)



    # TODO: 1.1 Check the user’s input to decide what to do next.#
while machine_on == True:

    user_choice = prompt_user_ choice()

    if user_choice == 'espresso':
        if check_resources(user_choice, MENU, resources):
            check_money(user_choice, MENU, resources)

    elif user_choice == 'latte':
        if check_resources(user_choice, MENU, resources):
            check_money(user_choice, MENU, resources)

    elif user_choice == 'cappucino':
        if check_resources(user_choice, MENU, resources):
            check_money(user_choice, MENU, resources)

    elif user_choice == 'report':
        print(f"Coffee Machine's current resources: \n {resources}")

    elif user_choice == 'off':
        machine_on = False

    else:
        print("Sorry, I didn't understand your answer")

# TODO: 1.2 The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt
#  should show again to serve the next customer.
#
# Need to insert a recursive call within the function, after drink is dispensed, to prompt the user for a choice again,
# and in turn, starting the program over.

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.

# The entire program needs to be run only while it is powered on. Throughout it needs to check if the user enters the
# prompt to turn it "off".  If the user turns it off the code stops running.

# while machine_powered_on == True:

#
# TODO: 2.1 For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
#  Your code should end execution when this happens.
#
# See above

# TODO: 3. Print report of all the coffee machine resources.

# print(f"Coffee Machine's current resources: \n {resources}")
#
# TODO: 3.1  When the user enters “report” to the prompt, a report should be generated that shows: the current
#  resource values. e.g.
#  Water: 100ml
#  Milk: 50ml
#  Coffee: 76g
#  Money: $2.5
#
# See above (TODO 3)

# TODO: 4. Check resources sufficient?
#
# TODO: 4.1 When the user chooses a drink, the program should check if there are enough resources to make that drink.
#  E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the
#  drink but print: “Sorry there is not enough water.”
#  c. The same should happen if another resource is depleted, e.g. milk or coffee.


# NEED THIS CODE AT THE BEGINNING OF PROGRAM!!!


#   print('Sorry, there is not enough water in the machine.')
#   print('Sorry, there is not enough milk in the machine.')
#   print('Sorry, there is not enough coffee in the machine.')
#
# TODO: 5. Process coins.
#
# TODO: 5.1 If there are sufficient resources to make the drink selected, then the program should prompt the user to
#  insert coins.
#  b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#  c. Calculate the monetary value of the coins inserted.
#  E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#


# TODO: 6. Check transaction successful?
#
# TODO: 6.1 Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50,
#  but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money.
#  Money refunded.”.
#
# TODO: 6.2 But if the user has inserted enough money, then the cost of the drink gets added to the machine as the
#   profit and this will be reflected the next time “report” is triggered. E.g.
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
#
# TODO: 6.3 If the user has inserted too much money, the machine should offer change. E.g.
#  “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
#
#


# TODO: 2.
