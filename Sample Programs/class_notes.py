############ 2/8/17 #############
import random

my_list = []
for i in range(100):
    my_list.append(random.randrange(1, 1001))
print(my_list)

total = 0
for item in my_list:
    total += item
print(total)

smallest_number = 1000
# or smallest_number = my_list[0]
for item in my_list:
    if item < smallest_number:
        smallest_number = item
print(smallest_number)

print("__________________________________________________________________________________________")

x = "This is a test string."

print(x[:6])
print(x[6:])
print(x[6:10])

a = "Hi"
b = "there"
c = "! "
print(a + b)
print(a + b + c)
print(a * 3)
print(a * 2 + b * 2)
# This will not work because it doesnt know what youre wanting to add.
# print(a + 32)
# This next one WILL work
print(a + str(32))
# This prints the amount of characters in a string: (len)
print(len("Hello, how are you?"))
print("__________________________________________________________________________________________")
# months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# n = int(input("Enter a month number: "))
# print(months[(n - 1) * 3: (n - 1) * 3 + 3])

plain_text = "This is a test. ABCDEF"
for character in plain_text:
    x = ord(character)
    x += 1
    print(chr(x), end="")

print()

encrypted_text = "Uijt!jt!b!uftu/!BCDEFG"
for character in encrypted_text:
    x = ord(character)
    x -= 1
    print(chr(x), end="")
print("__________________________________________________________________________________________")

######### 2/10/17 ############

