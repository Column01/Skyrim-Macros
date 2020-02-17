import keyboard
import pyautogui
import time


print("Welcome! This script will help you automatically transmute skyrim ores from iron to gold."
      "\nThis will also calculate for optimal casting so be sure to enter the correct values.")

def initialize_magicka():
    mag = int(input('How much magicka do you have?: '))
    while mag <= 0:
        print('Please input a value above zero for magicka.')
        mag = int(input('How much magicka do you have?: '))
    return mag

def initialize_num_ores():    
    ores = int(input('How many iron ore do you have?: '))
    while ores <= 0:
        print('Please input a value above zero for the number of iron ores.')
        ores = int(input('How many iron ore do you have?: '))
    return ores

def initialize_transmute_cost():
    cost = int(input('What does it cost for you to cast the transmute ores spell?: '))
    while cost <= 0:
        print('Please input a value above zero for the cost of the transmute ores spell.')
        cost = int(input('How much magicka does it cost for you to cast the transmute ores spell?: '))
    return cost

# Initialize the variables needed to calculate casts and whatnot.
magicka = initialize_magicka()
num_ores = initialize_num_ores()
transmute_cost = initialize_transmute_cost()
print(f'Total Magicka: {magicka}\nNumber of Iron Ores: {num_ores}\nTransmute Cost: {transmute_cost}')

# Not enough magicka to cast the spell
if magicka < transmute_cost:
    exit('You do not have enough magicka to cast the spell.' 
         '\nPlease make sure you level up your character some or clear and debuffs that affect magicka before proceeding.')

# Number of times to cast the spell per wait command. This will calculate for casting the spell twice (for both hands)
casts_per_wait = magicka / (transmute_cost * 2)

# Checks if the casts per wait is higher than 1 which means we can dual cast the spell. 
# If it isn't that means we can only single cast and we will need to double the number of ores to make sure they all get transmuted to gold.
if casts_per_wait >= 1:
    casts_per_wait = int(casts_per_wait)
    single_cast = False
else:
    casts_per_wait = 1
    # double the number of ores to make sure we go from iron > silver > gold
    num_ores * 2
    single_cast = True

if single_cast:
    print("Great! Not it's time to setup for transmuting. I detected that you can only cast the spell with one hand, so "
        "please equip the transmute ores spell in your main hand (left mouse button) and stand in a safe location."
        "\nMake sure you have your ores in your inventory as well. "
        "This will take twice as long to complete since it has to wait twice per ore to get from iron to gold.")
else:
    print("Great! Not it's time to setup for transmuting. "
        "Please equip the transmute ores spell in both hands and stand in a safe location."
        "\nMake sure you have your ores in your inventory as well.")

print('Press the "s" key to begin the transmuting.')
keyboard.wait('s')
print('Press Ctrl+C at any point when tabbed into the console window to quit the transmutation process.')
print('Waiting 10 seconds then starting to send keystrokes. Please tab back into the game.')
time.sleep(10)
try:
    for transmute_count in range(num_ores):
        for j in range(casts_per_wait):
            if not single_cast:
                pyautogui.mouseDown(button='left')
                pyautogui.mouseDown(button='right')
                time.sleep(1)
                pyautogui.mouseUp(button='left')
                time.sleep(0.25)
                pyautogui.mouseUp(button='right')
            else:
                pyautogui.mouseDown(button='left')
                time.sleep(1)
                pyautogui.mouseUp(button='left')
        time.sleep(0.25)
        keyboard.send('t')
        time.sleep(0.25)
        keyboard.send('enter')
        time.sleep(1)
except KeyboardInterrupt:
    print('Quitting script because you interrupted it. Please run again with new values if you wish to proceed.')
    quit(0)
