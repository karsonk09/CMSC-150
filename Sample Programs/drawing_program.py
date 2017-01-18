"""
This is my sample drawing program
"""

# This is my drawing program.

import arcade

arcade.open_window("Drawing Example", 600, 600)

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

# Drawing code goes here
# Left, right, top, bottom
arcade.draw_lrtb_rectangle_filled(5, 35, 590, 570, arcade.color.BITTER_LIME)

arcade.draw_lrtb_rectangle_filled(5, 35, 20, 0, arcade.color.ALLOY_ORANGE)

arcade.draw_point(50, 580, arcade.color.ORANGE, 5)

arcade.draw_line(75, 590, 95, 570, arcade.color.BLACK, 2)


arcade.finish_render()
arcade.run()
