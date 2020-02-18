# Skyrim Macros

A Collection of macros I'm writing for my skyrim playthrough to make things easier.

## Python Version

- Developed on Python 3.8, but should work for all python 3 versions (can change depending on the script.)
- No I won't add support for python 2

## Auto Transmute

### Notes
- Stand in a safe spot
- Use `Ctrl+C` to exit the program. You must be tabbed into the console window for it to work
- It will calculate if you can only single cast. It will also tell you if you can only single cast so be sure to read all prompts in the console and follow the instructions.
- Using even numbers for the number of ores is best since you need 2 gold ore to make 1 ingot. If you enter an odd number, it will cast an extra time to compensate.
- Install the dependencies below

### Dependencies
- [keyboard](https://pypi.org/project/keyboard/)
- [pynput](https://pypi.org/project/pynput/)