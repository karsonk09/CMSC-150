import arcade

arcade.open_window("My Drawing", 600, 600)

arcade.set_background_color((58, 56, 59))

arcade.start_render()

arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.color.DARK_GREEN)

arcade.draw_circle_filled(525, 525, 50, arcade.color.GHOST_WHITE)

arcade.draw_circle_filled(20, 575, 2, arcade.color.YELLOW)

arcade.draw_rectangle_filled(125, 125, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(125, 150, 25, 20, arcade.color.GRAY, 0, 180)

arcade.draw_line(0, 100, 225, 100, arcade.color.BLACK, border_width=1)
arcade.draw_line(375, 100, 600, 100, arcade.color.BLACK, border_width=1)
arcade.draw_line(20, 0, 20, 100, arcade.color.BLACK, 1)
arcade.draw_line(40, 0, 40, 100, arcade.color.BLACK, 1)
arcade.draw_line(60, 0, 60, 100, arcade.color.BLACK, 1)
arcade.draw_line(80, 0, 80, 100, arcade.color.BLACK, 1)
arcade.draw_line(100, 0, 100, 100, arcade.color.BLACK, 1)
arcade.draw_line(120, 0, 120, 100, arcade.color.BLACK, 1)
arcade.draw_line(140, 0, 140, 100, arcade.color.BLACK, 1)
arcade.draw_line(160, 0, 160, 100, arcade.color.BLACK, 1)
arcade.draw_line(180, 0, 180, 100, arcade.color.BLACK, 1)
arcade.draw_line(200, 0, 200, 100, arcade.color.BLACK, 1)
arcade.draw_line(225, 0, 225, 100, arcade.color.BLACK, 1)
arcade.draw_line(375, 0, 375, 100, arcade.color.BLACK, 1)
arcade.draw_line(400, 0, 400, 100, arcade.color.BLACK, 1)
arcade.draw_line(420, 0, 420, 100, arcade.color.BLACK, 1)
arcade.draw_line(440, 0, 440, 100, arcade.color.BLACK, 1)
arcade.draw_line(460, 0, 460, 100, arcade.color.BLACK, 1)
arcade.draw_line(480, 0, 480, 100, arcade.color.BLACK, 1)
arcade.draw_line(500, 0, 500, 100, arcade.color.BLACK, 1)
arcade.draw_line(520, 0, 520, 100, arcade.color.BLACK, 1)
arcade.draw_line(540, 0, 540, 100, arcade.color.BLACK, 1)
arcade.draw_line(560, 0, 560, 100, arcade.color.BLACK, 1)
arcade.draw_line(580, 0, 580, 100, arcade.color.BLACK, 1)



arcade.draw_arc_outline(300, 100, 75, 75, arcade.color.BLACK, 0, 180)


arcade.finish_render()

arcade.run()
