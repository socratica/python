# TITLE:  Iterators, Iterables, and Itertools in Python
# URL: https://youtu.be/WR7mO_jYN9g


# list = ['CX32', 'GSOF', 'Emily', 'Franz', 'Rex']
# for element in list:
#   print(element)

# for element in ('Jose', 'Boh', 'Rusti'):
#   print(element)

# for letter in 'Socratica':
#   print(letter)

# for byte in b'Binary':
#   print(byte)

# for digit in 299792458:
#   print(digit)

# c = 299792458
# digits = [int(d) for d in str(c)]

# for digit in digits:
#   print(digit)
# users = ['laust', 'LeoMoon', 'JennaSys', 'dgletts']

# for user in users:
#     print(user)

# looper = iter(users)
# while True:
#     try:
#         user = next(looper)
#         print(user)
#     except StopIteration:
#         break


# class Portfolio:
#     def __init__(self):
#         self.holdings = {}  # Key = ticker, Value = number of shares
    
#     def buy(self, ticker, shares):
#         self.holdings[ticker] = self.holdings.get(ticker, 0) + shares
    
#     def sell(self, ticker, shares):
#         self.holdings[ticker] = self.holdings.get(ticker, 0) - shares
    
#     def __iter__(self):
#         return iter(self.holdings.items())


# p = Portfolio()
# p.buy('ALPHA', 15)
# p.buy('BETA', 23)
# p.buy('GAMMA', 9)
# p.buy('GAMMA', 20)

# for (ticker, shares) in p:
#     print(ticker, shares)

# import itertools

# ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
# ranks = [str(rank) for rank in ranks]

# print(ranks)

# suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
# deck = [card for card in itertools.product(ranks, suits)]

# for (index, card) in enumerate(deck):
#     print(1 + index, card)

# hands = [hand for hand in itertools.combinations(deck, 5)]

# print(f"The number of 5-card poker hands is {len(hands)}.")
