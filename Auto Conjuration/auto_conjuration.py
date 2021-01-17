import keyboard
from pynput.mouse import Button, Controller
import time


mouse = Controller()
print("Welcome! This script will help you automatically shoot a corpse with soul trap to train conjuration."
      "\nThis will also calculate for optimal casting so be sure to enter the correct values.")


def initialize_magicka():
    mag = int(input('How much magicka do you have?: '))
    while mag <= 0:
        print('Please input a value above zero for magicka.')
        mag = int(input('How much magicka do you have?: '))
    return mag


def initialize_soultrap_cost():
    cost = int(input('What does it cost for you to cast the soultrap spell?: '))
    while cost <= 0:
        print('Please input a value above zero for the cost of the soultrap spell.')
        cost = int(input('How much magicka does it cost for you to cast the soultrap spell?: '))
    return cost


def initialize_wait_amount():
    wait = int(input('How many times would you like to wait when you run out of magicka? '))
    while wait <= 0:
        print("Please input a value above zero for the cost of the amount of times you'd like to wait.")
        wait = int(input('How many times would you like to wait when you run out of magicka? '))
    return wait


# Initialize the variables needed to calculate casts and whatnot.
magicka = initialize_magicka()
soultrap_cost = initialize_soultrap_cost()
num_waits = initialize_wait_amount()


# Not enough magicka to cast the spell
if magicka < soultrap_cost:
    exit('You do not have enough magicka to cast the spell.'
         '\nPlease make sure you level up your character some or clear and debuffs that affect magicka before proceeding.')

# Number of times to cast the spell per wait command.
casts_per_wait = int(magicka / soultrap_cost)

print("Great! Now it's time to setup for training. "
      "Please kill a mob (anything \"living\" works. A deer, a wolf, anything) and equip the soul trap spell in your main hand."
      "\nStand in a safe location and make sure you have USLEEP disabled (if you use it) as it patches this method of training conjuration.")

print('Press the "s" key to begin the casting soul trap.')
keyboard.wait('s')
print('Press Ctrl+C at any point when tabbed into the console window to quit the casting process.')
print('Waiting 10 seconds then starting to send keystrokes. Please tab back into the game.')
time.sleep(10)
try:
    # Run the macro for "num_waits" iterations
    for transmute_count in range(num_waits):
        # Cast the spell as many times as possible and then wait for an hour to regain magicka
        for j in range(casts_per_wait):
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
