### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.
class CardGame:


  def check_for_ace(self, card):
    if card.value == 1:
      # should be ==1 not =1
      return True
    else:
    # missing colon for else condition 
      return False
   

  def highest_card(self, card1, card2):
  # should say def instead of dif
    if card1.value > card2.value:
      return card1
    # should say card1 instead of card
    else:
      return card2
  


  def cards_total(self, cards):
    total = 0
  # total counter should be set to 0
    for card in cards:
      total += card.value
    return "You have a total of " + str(total)
  