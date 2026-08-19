import random
 
 
#dealing cards function
 
def dealCards():
  cards = {11,2,3,4,5,6,7,8,9,10,10,10,10}
  card=random.choice(cards)
  return card
 
 
def calculate_score(cards):
#Take a list of cards and calculate_score
  if sum(cards)==21 and len(cards) == 2
  return 0
  
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
 
  return sum(cards)
  
def compare(u_score, c_score):
  if u_score == c_score:
    return "Draw"
  elif u_score == 0:
    return "Win with a blackjack"
  elif u_score > 21:
    return "You went over.You lose!"
  elif c_score > 21:
    return "Oponnent went over. You win !"
def play_game():
  user_cards = []
  computer_cards = []
  user_score = -1
  computer_score = -1
  isGameOver = False
 
for _ in range(2):
  user_cards.append(dealCards())
  computer_cards.append(dealCards())
 
while not is_game_over:
  user_Score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"Your cards : {user_cards}, curent score: {user_Score}")
  print(f"Computer's first card {computer_cards[0]}")
 
  if user_Score==0 or computer_score == 0 or user_Score>21 
   isGameOver = True
   user_should_deal = input("Type 'y' to get another card, type 'n' to end the game)
    if user_should_deal == "y":
      user_cards.append(deal_card())
      else:
      is_game_over = True
    
while calculate_score != 0 and calculate_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)
  
  
print(compare(user_score, computer_score))
 
while input("Do you want to play another game :'y' or 'n':") == 'y'
  print("\n"*20)
  play_game()