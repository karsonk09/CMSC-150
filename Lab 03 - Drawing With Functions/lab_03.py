import arcade



def draw_grass():
    arcade.draw_rectangle_filled(300, 150, 600, 300, arcade.color.FOREST_GREEN)


def draw_sun(position_x, position_y):
    arcade.draw_circle_filled(position_x, position_y, 40, arcade.color.YELLOW)
    arcade.draw_line(position_x, position_y + 45, position_x, position_y + 70, arcade.color.YELLOW)
    arcade.draw_line(position_x + 45, position_y, position_x + 70, position_y, arcade.color.YELLOW)
    arcade.draw_line(position_x - 45, position_y, position_x - 70, position_y, arcade.color.YELLOW)
    arcade.draw_line(position_x, position_y - 45, position_x, position_y - 70, arcade.color.YELLOW)
    arcade.draw_line(position_x + 28, position_y + 33, position_x + 45, position_y + 45, arcade.color.YELLOW)
    arcade.draw_line(position_x + 28, position_y - 33, position_x + 45, position_y - 45, arcade.color.YELLOW)
    arcade.draw_line(position_x - 28, position_y + 33, position_x - 45, position_y + 45, arcade.color.YELLOW)
    arcade.draw_line(position_x - 28, position_y - 33, position_x - 45, position_y - 45, arcade.color.YELLOW)



def draw_house(position_x, position_y):
    arcade.draw_rectangle_filled(position_x, position_y, 150, 150, arcade.color.TAN)
    arcade.draw_triangle_filled(position_x - 100, position_y + 75,
                                position_x + 100, position_y + 75,
                                position_x, position_y + 150,
                                arcade.color.BLACK)
    arcade.draw_rectangle_filled(position_x, position_y - 42, 50, 65, arcade.color.BLACK)
    arcade.draw_rectangle_filled(position_x - 35, position_y + 27, 30, 30, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x + 35, position_y + 27, 30, 30, arcade.color.SKY_BLUE)


def draw_person(position_x, position_y):
    arcade.draw_line(position_x, position_y, position_x, position_y + 25, arcade.color.BLACK)
    arcade.draw_circle_outline(position_x, position_y + 37, 12, arcade.color.BLACK)
    arcade.draw_line(position_x, position_y, position_x + 15, position_y - 15, arcade.color.BLACK)
    arcade.draw_line(position_x, position_y, position_x - 15, position_y - 15, arcade.color.BLACK)
    arcade.draw_line(position_x, position_y + 9, position_x + 12, position_y + 21, arcade.color.BLACK)
    arcade.draw_line(position_x, position_y + 9, position_x - 12, position_y + 21, arcade.color.BLACK)

def draw_airplane(position_x, position_y):
    arcade.draw_rectangle_filled(position_x, position_y, 150, 30, arcade.color.WHITE)
    arcade.draw_arc_filled(position_x - 75, position_y, 20, 15, arcade.color.WHITE, 90, 270)
    arcade.draw_triangle_filled(position_x + 75, position_y + 15,
                                position_x + 35, position_y + 15,
                                position_x + 75, position_y + 40,
                                arcade.color.WHITE)
    arcade.draw_line(position_x - 75, position_y - 6, position_x + 75, position_y - 6, arcade.color.RED)
    arcade.draw_line(position_x + 40, position_y + 15, position_x + 72, position_y + 34, arcade.color.RED)
    arcade.draw_line(position_x + 72, position_y + 15, position_x + 72, position_y + 34, arcade.color.RED)
    arcade.draw_line(position_x + 40, position_y + 15, position_x + 72, position_y + 15, arcade.color.RED)
    arcade.draw_arc_filled(position_x - 75, position_y, 17, 13, arcade.color.SKY_BLUE, 90, 180)
    arcade.draw_triangle_filled(position_x, position_y - 15,
                                position_x, position_y - 70,
                                position_x - 25, position_y - 15,
                                arcade.color.WHITE)
    arcade.draw_triangle_filled(position_x, position_y + 15,
                                position_x, position_y + 45,
                                position_x - 25, position_y + 15,
                                arcade.color.WHITE)
    arcade.draw_rectangle_filled(position_x - 68, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x - 55, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x - 42, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x - 29, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x - 16, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x - 3, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x + 10, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x + 23, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x + 36, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(position_x + 10, position_y + 6, 8, 8, arcade.color.SKY_BLUE)
    arcade.draw_triangle_outline(position_x - 3, position_y - 18,
                                 position_x - 22, position_y - 18,
                                 position_x - 3, position_y - 67,
                                 arcade.color.RED)
    arcade.draw_line(position_x - 3, position_y + 15, position_x - 3, position_y + 37, arcade.color.RED)
    arcade.draw_line(position_x - 22, position_y + 15, position_x - 3, position_y + 37, arcade.color.RED)


def draw_bush(position_x, position_y):
    arcade.draw_rectangle_filled(position_x, position_y, 75, 25, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(position_x, position_y + 18, 25, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(position_x + 20, position_y + 16, 25, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(position_x - 25, position_y + 14, 25, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(position_x + 32, position_y + 2, 15, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(position_x - 32, position_y + 2, 15, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(position_x - 10, position_y, 2, arcade.color.STRAWBERRY)
    arcade.draw_circle_filled(position_x, position_y + 10, 2, arcade.color.STRAWBERRY)
    arcade.draw_circle_filled(position_x + 10, position_y + 20, 2, arcade.color.STRAWBERRY)
    arcade.draw_circle_filled(position_x - 20, position_y + 18, 2, arcade.color.STRAWBERRY)
    arcade.draw_circle_filled(position_x + 25, position_y - 5, 2, arcade.color.STRAWBERRY)
    arcade.draw_circle_filled(position_x + 30, position_y + 30, 2, arcade.color.STRAWBERRY)

def on_draw(delta_time):
    arcade.start_render()

    draw_grass()
    draw_sun(500, 500)
    draw_house(150, 255)
    draw_person(450, 100)
    draw_airplane(on_draw.airplane_position, 550)
    draw_bush(225, 178)
    draw_bush(80, 178)
    on_draw.airplane_position = on_draw.airplane_position - 5
    if on_draw.airplane_position < -100:
        on_draw.airplane_position = 750
on_draw.airplane_position = 500


def main():
    arcade.open_window("Drawing With Functions", 600, 600)
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()

main()