import arcade


def draw_house(position_x, position_y):

    arcade.draw_rectangle_filled(position_x, position_y, 100, 100, arcade.color.AERO_BLUE)
    arcade.draw_triangle_filled(position_x - 75, position_y + 50,
                                position_x + 75, position_y + 50,
                                position_x, position_y + 100,
                                arcade.color.BLACK)

arcade.open_window("House", 600, 600)

arcade.set_background_color(arcade.color.YELLOW)

arcade.start_render()



draw_house(300, 300)

arcade.finish_render()

arcade.run()
