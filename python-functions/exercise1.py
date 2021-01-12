def say_hello(name='World', greeting = None):
    #the sequence of input parameters matter. In case, greeting would have come in first [instead of name], a single parameter passed would be mapped to the first parameter.
    #None value is a special keyword that represents the NoneType object.
    print(f'Hello {name}!')

say_hello()
say_hello('Bob')
say_hello(greeting='Heyya')
say_hello('Roy','Heyya')

def add_two_numbers(x,y):
    return x+y

add_two_numbers(4,6)
result = add_two_numbers(5,6)
print(result)

def create_deck():
  suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  deck = []

  for  suit in suits:
    for rank in ranks:
      deck.append(f'{rank} of {suit}')

  return deck

my_deck = create_deck()
print(len(my_deck))