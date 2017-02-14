import arcade

class Character():

    def __init__(self):
        self.name = "Link"
        self.sex = "Male"
        self.max_hit_points = 50
        self.current_hit_points = 50
        self.max_speed = 10
        self.armor_amount = 8

class Address():
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""

home_address = Address()
home_address.name = "Karson Richardson"
home_address.line1 = "100 Amelia Dr"
home_address.city = "East Peoria"
home_address.state = "Illinois"
home_address.zip = "61611"

def print_address(address):
    print(address.name)
    if len(address.line1) > 0:
        print(address.line1)
    if len(address.line2) > 0:
        print(address.line2)



class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bork(self):
        if self.weight <= 20:
            print("Bork says " + self.name + ".")
        else:
            print("BORK says " + self.name + ".")

doge = Dog()
doge.name = "Jeffery"
doge.age = 8
doge.weight = 19

doge.bork()

doggo = Dog()
doggo.name = "Cheren"
doggo.age = 9
doggo.weight = 45

doggo.bork()

class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 10
        self.color = (255, 255, 255)
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
    def draw(self, screen):
        arcade.draw_circle_filled(self.x)