import keyboard
from pynput.mouse import Button, Controller
import time
import math

mouse = Controller()
print("Welcome! This script will help you automatically transmute skyrim ores from iron to gold."
      "\nThis will also calculate for optimal casting so be sure to enter the correct values.")


def initialize_magicka():
    mag = int(input('How much magicka do you have?: '))
    while mag <= 0:
        print('Please input a value above zero for magicka.')
        mag = int(input('How much magicka do you have?: '))
    return mag


def initialize_num_ores():
    ores = int(input('How many iron ore do you have (Even numbers are best)?: '))
    while ores <= 0:
        print('Please input a number above zero for the number of iron ores.')
        ores = int(input('How many iron ore do you have (Even numbers are best)?: '))
    return ores


def initialize_transmute_cost():
    cost = int(input('What does it cost for you to cast the transmute ores spell?: '))
    while cost <= 0:
        print('Please input a value above zero for the cost of the transmute ores spell.')
        cost = int(input('How much magicka does it cost for you to cast the transmute ores spell?: '))
    return cost


# Initialize the variables needed to calculate casts and whatnot.
try:
    num_ores = initialize_num_ores()
    magicka = initialize_magicka()
    transmute_cost = initialize_transmute_cost()
except KeyboardInterrupt:
    print("Quitting due to keyboard interrupt.")
    quit(0)

# Not enough magicka to cast the spell
if magicka < transmute_cost:
    exit('You do not have enough magicka to cast the spell.'
         '\nPlease make sure you level up your character some or clear and debuffs that affect magicka before proceeding.')

# Number of times to cast the spell per wait command. This will calculate for casting the spell twice (for both hands)
casts_per_wait = magicka / (transmute_cost * 2)

# Checks if the casts per wait is higher than 1 which means we can dual cast the spell.
# If it isn't that means we can only single cast and we will need to double the number of ores to make sure they all get transmuted to gold.
iteration_time = -1.0
if casts_per_wait >= 1:
    casts_per_wait = int(casts_per_wait)
    # 2.2 seconds to cast, 2.1 seconds to wait
    iteration_time = 2.2 + 2.1
    single_cast = False
else:
    casts_per_wait = 1
    num_ores = num_ores * 2
    # 1.25 seconds to cast, 2.1 seconds to wait
    iteration_time = 1.25 + 2.1
    single_cast = True

# Calculate the amount of time it may take to convert all ores
num_iterations = math.ceil(num_ores / casts_per_wait)
mins, secs = divmod(iteration_time * num_iterations, 60)
print("Estimated time required: {} minute(s) and {} second(s)\n".format(int(mins), int(secs)))

if single_cast:
    print("Great! Now it's time to setup for transmuting. I detected that you can only cast the spell with one hand, "
          "please equip the transmute ores spell in your main hand (left mouse button) and stand in a safe location."
          "\nMake sure you have your ores in your inventory as well. "
          "This will take twice as long to complete since it has to wait twice per ore to get from iron to gold.")
else:
    print("Great! Now it's time to setup for transmuting. "
          "Please equip the transmute ores spell in both hands and stand in a safe location."
          "\nMake sure you have your ores in your inventory as well.")


try:
    print('Press the "s" key to begin the transmuting.')
    keyboard.wait('s')
    print('Press Ctrl+C at any point when tabbed into the console window to quit the transmutation process.')
    print('Waiting 10 seconds then starting to send keystrokes. Please tab back into the game.')
    time.sleep(10)

    # We use the number of ores / casts per wait so we can divide it into a number of iterations to complete the total amount of ores the user wanted.
    # This number will change a depending on if the user can only single cast the spell or dual cast
    # A side effect of this is that odd numbers will cast an extra time to compensate for the odd division result
    for _ in range(num_iterations):
        for _ in range(casts_per_wait):
            if not single_cast:
                time.sleep(0.1)
                mouse.press(Button.left)
                time.sleep(1)
                mouse.release(Button.left)
                time.sleep(0.1)
                mouse.press(Button.right)
                time.sleep(1)
                mouse.release(Button.right)
            else:
                time.sleep(0.25)
                mouse.press(Button.left)
                time.sleep(1)
                mouse.release(Button.left)
        time.sleep(1)
        keyboard.send('t')
        time.sleep(0.1)
        keyboard.send('enter')
        time.sleep(1)
except KeyboardInterrupt:
    print('Quitting script because you interrupted it. Please run again with new values if you wish to proceed.')
    quit(0)
