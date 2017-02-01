import random

heads = 0
tails = 0

for i in range(50):

    random_number = random.randrange(0, 2)

    if random_number == 1:
        print("Heads")
        heads += 1

    else:
        print("Tails")
        tails += 1

print("Heads:", heads)
print("Tails:", tails)
