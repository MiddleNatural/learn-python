
import random
Random = random.randint(1, 10)
Answer = int(input("Guess the number from 1 to 10:"  ))
Tries  = 0
if Answer > 10 or Answer < 1:
  print("You're going too far with the numbers, please try again.")
elif Answer != Random:
    Tries = Tries + 1
    WrongAnswer = ("You got it wrong again, please try again. Your attempt count:", Tries)
    print(WrongAnswer)
    for WrongAnswer in range(9):
       NextTry = int(input("Please guess again: "))
       if NextTry != Random:
           Tries = Tries + 1
           print("You got it wrong, please try again. Your attempt count:", Tries)
       elif NextTry == Random:
        print("You got it right. The answer is", Random, "Your attempt count:", Tries)
        break
if Answer == Random:
    print("You got it right!")