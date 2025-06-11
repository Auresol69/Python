# function = A block of reusable code
#            place () after the function name to invoke it

def hpbd(name,old):
    print(f"hpbday {name} {old}!")

# hpbd("Roy",20)

def display_invoice(username,amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due: {due_date}")

# display_invoice("Roy",42.50,"01/01")

def add(x,y):
    return x+y

print(add(1,2)==3)