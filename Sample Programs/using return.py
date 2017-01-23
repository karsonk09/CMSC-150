def sum_two_numbers(a, b):
    result = a + b
    return result

def circumference_of_circle(radius):
    PI = 3.14159
    circumference = 2 * PI * radius
    return circumference
my_result = circumference_of_circle(20)
print(my_result)

def a():
    b()
    print("A")

def b():
    print("B")

a()