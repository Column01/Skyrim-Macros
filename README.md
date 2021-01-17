# Skyrim Macros

A Collection of macros I'm writing for my Skyrim play through to make things easier. If you make a cool macro using Python 3, please submit a pull request to add it here!

## Python Version: Python 3.4+

- Developed using Python 3.8, but should work for all Python 3 versions after 3.6 (can change depending on the script.)
- No I won't add support for Python 2. It's EOL was Jan. 1st, 2020

## Auto Transmute (Author: Column01)

### Notes
- Stand in a safe spot
- Use `Ctrl+C` to exit the program. You must be tabbed into the console window for it to work
- It will calculate if you can only single cast. It will also tell you if you can only single cast so be sure to read all prompts in the console and follow the instructions.
- Using even numbers for the number of ores is best since you need 2 gold ore to make 1 ingot. If you enter an odd number, it will cast an extra time to compensate.
- If you have silver ore in your inventory, add one to the total number of ores for every 2 silver ore you have (or one for one if you want to play it safe)
- Install the dependencies below

### Dependencies
- [keyboard](https://pypi.org/project/keyboard/)
- [pynput](https://pypi.org/project/pynput/)

## Auto Conjuration (Author: Column01)

### Notes
- Stand in a safe spot
- Use `Ctrl+C` to exit the program. You must be tabbed into the console window for it to work
- Using a dead animal is the easiest way since they are easy to kill (anything that is considered "living" will work)
- Disable [USLEEP](https://www.nexusmods.com/skyrim/mods/71214) as it patches this method of training conjuration
- 1000 casts generally will level conjuration to 100 from 15 and takes about an hour to complete.
- Install the dependencies below

### Dependencies
- [keyboard](https://pypi.org/project/keyboard/)
- [pynput](https://pypi.org/project/pynput/)