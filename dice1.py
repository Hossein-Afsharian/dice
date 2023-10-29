import random

while True:

    op = input("tas or exit")
    if op == "exit":
        break

    if op == "tas":
        x=random.randint(1,6)
        print(x)

        if x==6:
             print("jayeze!! dobareh tas beriz")
             x = random.randint(1,6)
             print(x)
             break