import threading
from time import sleep

# for x in reversed(range(1,11,3)):
#     print(x)
#     sleep(1)
# print("Happy Birthday!")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    if x.isdigit():
        if int(x) == 7:
            continue
        else:
            print(x)