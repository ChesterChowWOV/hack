from colorama import Fore
from random import randint

while True:
  # Your terminal must support color in order for this to work correctly
  print(Fore.GREEN + str(randint(0,1)), end = '')
