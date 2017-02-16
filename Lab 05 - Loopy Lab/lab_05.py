import arcade

arcade.open_window("Lab 05 - Loopy Lab", 1200, 600)

arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

arcade.start_render()

arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

# Section 1
for row in range(30):
    for column in range(30):
        x = (column * 10) + 5
        y = (row * 10) + 5
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 2
for row in range(30):
    for column in range(30):
        x = (row * 10) + 305
        y = (column * 10) + 5
        if row % 2 == 1:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
        else:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 3
for row in range(30):
    for column in range(30):
        x = (row * 10) + 605
        y = (column * 10) + 5
        if column % 2 == 1:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
        else:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 4
for row in range(30):
    for column in range(30):
        x = (row * 10) + 905
        y = (column * 10) + 5
        if column % 2 == 1:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
        elif row % 2 == 1:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
        else:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 5
for row in range(30):
    for column in range(row):
        x = (row * 10) + 5
        y = (column * 10) + 305
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 6
for row in range(30):
    for column in range(30 - row):
        x = (row * 10) + 305
        y = (column * 10) + 305
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 7
for row in range(30):
    for column in range(30 - (row - 1)):
        x = (row * 10) + 605
        y = 300 - (column * 10) + 305
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 8
for row in range(30):
    for column in range(row + 2):
        x = (row * 10) + 905
        y = 300 - (column * 10) + 305
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


arcade.finish_render()

arcade.run()
