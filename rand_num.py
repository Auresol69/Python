import random

from tornado.options import options

# print(help(random))
# number = random.randint(1,6)
# number = random.random()

options = ("rock","paper","scissors")
option = random.choice(options)

cards = ["A","2","3"]

random.shuffle(cards)
print(cards)