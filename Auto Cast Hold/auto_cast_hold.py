import keyboard
from pynput.mouse import Button, Controller
import time

mouse = Controller()
print("Welcome! This script will help you automatically level schools of magic that require holding a spell"
      "\nThis will also calculate for optimal casting so be sure to enter the correct values.")


def initialize_magicka():
    mag = int(input('How much magicka do you have?: '))
    while mag <= 0:
        print('Please input a value above zero for magicka.')
        mag = int(input('How much magicka do you have?: '))
    return mag


def initialize_wait_amount():
    wait = int(input('How many times would you like to wait when you run out of magicka?: '))
    while wait <= 0:
        print("Please input a value above zero for the cost of the amount of times you'd like to wait.")
        wait = int(input('How many times would you like to wait when you run out of magicka?: '))
    return wait


def initialize_healing_cost():
    cost = int(input('What does it cost for you to cast the spell per second?: '))
    while cost <= 0:
        print('Please input a value above zero for the cost to cast the spell.')
        cost = int(input('How much magicka does it cost for you to cast the spell per second?: '))
    return cost


# Initialize the variables needed to calculate casts and whatnot.
try:
    num_iterations = initialize_wait_amount()
    magicka = initialize_magicka()
    spell_cost = initialize_healing_cost()
except KeyboardInterrupt:
    print("Quitting due to keyboard interrupt.")
    quit(0)

# Not enough magicka to cast the spell
if magicka < spell_cost:
    exit('You do not have enough magicka to cast the spell.'
         '\nPlease make sure you level up your character some or clear and debuffs that affect magicka before proceeding.')

# How long to cast the spell in seconds per wait command.
length_of_cast = magicka / spell_cost

# Calculate the amount of time it may take to complete
mins, secs = divmod((length_of_cast * num_iterations) + 2.2, 60)
print("Estimated time required: {} minute(s) and {} second(s)\n".format(int(mins), int(secs)))

print("Great! Now it's time to setup for casting. "
      "\nPlease equip the spell in your main hand."
      "\nSave the game before beginning in case something goes wrong")


try:
    print('Press the "s" key to begin casting.')
    keyboard.wait('s')
    print('Press Ctrl+C at any point when tabbed into the console window to quit the process.')
    print('Waiting 10 seconds then starting to send keystrokes. Please tab back into the game.')
    time.sleep(10)

    # Cast the spell repeatedly
    for _ in range(num_iterations):
        time.sleep(0.1)
        # Start casting, wait until magicka empties and then stop casting. Then wait to regain magicka
        mouse.press(Button.left)
        time.sleep(length_of_cast)
        mouse.release(Button.left)
        time.sleep(1)
        keyboard.send('t')
        time.sleep(0.1)
        keyboard.send('enter')
        time.sleep(1)
except KeyboardInterrupt:
    print('Quitting script because you interrupted it. Please run again with new values if you wish to proceed.')
    quit(0)
