import arcade

def draw_grass():
    """
    This function draws grass.
    """
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

def draw_pine_tree(position_x, position_y):
    """
    This function draws a pine tree.
    """

    # Trunk
    arcade.draw_rectangle_filled(100, 200, 30, 80, arcade.color.BROWN)

    # Leaves
    arcade.draw_triangle_filled(position_x - 70, position_y + 60,
                                position_x - 50, position_y +60,
                                position_x, position_y + 150,
                                arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(position_x - 70, position_y + 100,
                                position_x - 70, position_y + 100,
                                positoion_x, position_y + 150,
                                arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(position_x - 55, position_y + 150,
                                position_x - 55, position_y + 150,
                                position_x, position_y + 230,
                                arcade.color.FOREST_GREEN)

draw_pine_tree(50, 100)

arcade.open_window("Drawing With Functions", 600, 600)

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

draw_grass()
draw_pine_tree()

center_x = 200
center_y = 200
width = 30
height = 30

arcade.draw_triangle_filled(center_x - width / 2, center_y - width / 2,
                            center_x + width / 2, center_y - width / 2,
                            center_x, center_y,
                            arcade.color.GREEN)

arcade.finish_render()

arcade.run()
