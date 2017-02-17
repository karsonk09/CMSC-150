import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_RADIUS = 15
MOVEMENT_SPEED = 3

class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        self.ball_x = 50
        self.ball_y = 50

        self.ball_change_x = 0
        self.ball_change_y = 0

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x, self.ball_y, BALL_RADIUS, arcade.color.ORANGE)

    def animate(self, delta_time):
        self.ball_x += self.ball_change_x
        if self.ball_x >= SCREEN_WIDTH - BALL_RADIUS:
            self.ball_x = SCREEN_WIDTH - BALL_RADIUS
        self.ball_y += self.ball_change_y

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            print("Right key pressed")
            self.ball_change_x = MOVEMENT_SPEED


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.ball_change_x = 0

window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)



arcade.run()
