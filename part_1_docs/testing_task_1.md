### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else          # improperly formatted, needs a colon
      return False
   

  dif highest_card(self, card1 card2):   # def/dif error, missing comma in variable list
  if card1.value > card2.value:
    return card
  else:
    return card2
  


def cards_total(self, cards):  #it seems to be a variable, but 'total' is undefined
  total
  for card in cards:
    total += card.value # card for cards - 'cards' was passed to function, card is iteration of cards
    return "You have a total of" + total  #improperly formatted f string 
  
```