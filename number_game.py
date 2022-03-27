import art
import replit
import time
import random
iter=0
def clear_line(n):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def counter_check(i):
  clear_line(5)
  w = random.randint(0,100)
  while i != 0:
    i -= 1
    print(f"You have {i} attempts remaining to guess the number.")
    a = int(input("Make a guess : "))
    if a < w:
      print("Too Low .\n Guess again.")
    elif w < a:
      print("Too High .\n Guess again. ")
    else:
      replit.clear() 
      print("\t\t\t\t\tDamn Son!!! \n\t\t\t\t\t You Won!")
      i=0
  replit.clear() 
  print("\t\t\t\t\tAre you Dumb? \n\t\t\t\t\t Game Over!")    
counter = True
while counter is True:
  replit.clear()  
  art.logo()
  print("Welcome to the Number Guessing Game ")
  print("Processing a Number between 1 and 100 ")
  art.logo2()
  time.sleep(1)
  clear_line(8)
  inp=input("Choose a Difficulty Type \n Type 'Easy' or 'Hard' : ")
  inp=inp.lower()
  if inp=="easy":
    counter_check(10)
  elif inp=="hard":
    counter_check(5)
  else:
    #replit.clear()
    print("\t\t\t\t\tAre you Dumb? \n\t\t\t\t\t Game Over!")
    exit()
  counter = False
  
