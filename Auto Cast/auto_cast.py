import keyboard
from pynput.mouse import Button, Controller
import time


mouse = Controller()
print("Welcome! This script will help you automatically cast a spell that requires charging up to use."
      "\nThis will also calculate for optimal casting so be sure to enter the correct values.")


def initialize_magicka():
    mag = int(input('How much magicka do you have?: '))
    while mag <= 0:
        print('Please input a value above zero for magicka.')
        mag = int(input('How much magicka do you have?: '))
    return mag


def initialize_spell_cost():
    cost = int(input('What does it cost for you to cast the spell?: '))
    while cost <= 0:
        print('Please input a value above zero for the cost of the spell.')
        cost = int(input('How much magicka does it cost for you to cast the spell?: '))
    return cost


def initialize_wait_amount():
    wait = int(input('How many times would you like to wait when you run out of magicka? '))
    while wait <= 0:
        print("Please input a value above zero for the cost of the amount of times you'd like to wait.")
        wait = int(input('How many times would you like to wait when you run out of magicka? '))
    return wait


try:
    # Initialize the variables needed to calculate casts and whatnot.
    magicka = initialize_magicka()
    spell_cost = initialize_spell_cost()
    num_waits = initialize_wait_amount()
except KeyboardInterrupt:
    print("Quitting due to keyboard interrupt.")
    quit(0)


# Not enough magicka to cast the spell
if magicka < spell_cost:
    exit('You do not have enough magicka to cast the spell.'
         '\nPlease make sure you level up your character some or clear and debuffs that affect magicka before proceeding.')

# Number of times to cast the spell per wait command.
casts_per_wait = int(magicka / spell_cost)
time_per_wait = (1.25 * casts_per_wait) + 2.1

mins, secs = divmod((time_per_wait * num_waits), 60)
print("Estimated time required: {} minute(s) and {} second(s)\n".format(int(mins), int(secs)))

print("Great! Now it's time to setup for training. "
      "Move to a safe area and setup for whatever skill of magic you wish to train that requires casting.")


try:
    print('Press the "s" key to begin the casting the spel;.')
    keyboard.wait('s')
    print('Press Ctrl+C at any point when tabbed into the console window to quit the casting process.')
    print('Waiting 10 seconds then starting to send keystrokes. Please tab back into the game.')
    time.sleep(10)
    # Run the macro for "num_waits" iterations
    for _ in range(num_waits):
        # Cast the spell as many times as possible and then wait for an hour to regain magicka
        for _ in range(casts_per_wait):
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
