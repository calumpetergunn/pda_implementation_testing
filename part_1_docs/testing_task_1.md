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
    if card.value = 1: #needs to have double == for a calculation rather than assignment to a variable
      return True
    else # needs double colon
      return False
   

  dif highest_card(self, card1 card2): # no comma between card1 and card2, 'def' misspelled as 'dif'
  if card1.value > card2.value: #needs to be indented 
    return card # card is not defined, should be 'card1'
  else:
    return card2
  


def cards_total(self, cards):
  total # nothing assigned to 'total', need to assign as zero to start
  for card in cards:
    total += card.value
    return "You have a total of" + total #need to use string concetenation here
  
```
