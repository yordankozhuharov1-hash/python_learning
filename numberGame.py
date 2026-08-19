import random
 
#Introducing and declaring global variables.
print("Welcome to the number guessing game")
lives=0
computerNumber = random.randint(1,100)
hardOrEasy = input("Choose a level 'hard' or 'easy':")
userNum = int(input("Pick a number between 1 and 100"))
 
#Lives statment
 
if hardOrEasy == "hard":
  lives+= 5
elif hardOrEasy == "easy":
  lives += 10
 
while lives > 1 :
  if userNum != computerNumber:
    lives=lives - 1
    if userNum < computerNumber:
      print(f"Your lives are {lives}!")
      userNum = int(input("Try with higher number: "))
    elif userNum > computerNumber:
      print(f"Your lives are {lives}!")
      userNum = int(input("Try with smaller number: "))
  else:
    print("You Win!!")
    break
if lives == 0 and userNum != computerNumber:
    print("You are dead")