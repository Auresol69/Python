# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello",first="Spongebob",title="Mr.",last="Squarepants")

# position argu phải đứng ĐẦU TIÊN

print("1","2","3", sep="-")
                #   ^
                #   |
                # keyword argument
