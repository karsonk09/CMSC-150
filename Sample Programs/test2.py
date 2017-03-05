import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_RADIUS = 15


class MyApplication(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        self.ball_x = 50
        self.ball_y = 50

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x, self.ball_y, BALL_RADIUS, arcade.color.ORANGE)

    def on_mouse_motion(self, x, y, dx, dy):
        print("Mouse movement", x, y, dx, dy)
        self.ball_x = x
        self.ball_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        print("Press: ", button)
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Main mouse button pressed")



window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
