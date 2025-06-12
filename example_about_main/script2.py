from script1 import *

# print(__name__)

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("Goodbye!")

if __name__ == '__main__':
    main()