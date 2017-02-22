import arcade

# Constant Variables for program
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
SQUARE_LENGTH = 35
SQUARE_HEIGHT = 35
SQUARE_MOVE_SPEED = 5
BALL_MOVE_SPEED = 5
BALL_RADIUS = 20


class MyApplication(arcade.Window):

    # Main application class.

    def __init__(self, width, height):
        super().__init__(width, height)

        # Variables for square
        self.square_x_position = 150
        self.square_y_position = 300
        self.square_change_x = 0
        self.square_change_y = 0

        # Variables for ball
        self.ball_x = 200
        self.ball_y = 400
        self.ball_change_x = 0
        self.ball_change_y = 0

        arcade.set_background_color(arcade.color.BLACK)

        # Making the mouse invisible
        self.set_mouse_visible(False)

        # Loading sound files so I don't have to load them over and over
        self.coin_sound = arcade.load_sound("sounds/coin3.ogg")

        self.hit_sound = arcade.load_sound("sounds/hit1.ogg")

    # Drawing everything
    def on_draw(self):
        # Rendering the Screen
        arcade.start_render()

        # Setting Background color
        arcade.set_background_color(arcade.color.BLACK)

        # Square/Rectangle drawing function
        arcade.draw_rectangle_filled(self.square_x_position, self.square_y_position, SQUARE_LENGTH, SQUARE_HEIGHT,
                                     arcade.color.ALLOY_ORANGE)

        # Circle drawing function
        arcade.draw_circle_filled(self.ball_x, self.ball_y, BALL_RADIUS, arcade.color.RED_DEVIL)

    def animate(self, delta_time):
        # Movements for both figures
        self.ball_x += self.ball_change_x
        self.ball_y += self.ball_change_y

        self.square_x_position += self.square_change_x
        self.square_y_position += self.square_change_y

        # Collisions and sound effects for collisions
        if self.ball_x < BALL_RADIUS:
            self.ball_x = BALL_RADIUS
            arcade.play_sound(self.hit_sound)

        if self.ball_y < BALL_RADIUS:
            self.ball_y = BALL_RADIUS
            arcade.play_sound(self.hit_sound)

        if self.ball_x > SCREEN_WIDTH - BALL_RADIUS:
            self.ball_x = SCREEN_WIDTH - BALL_RADIUS
            arcade.play_sound(self.hit_sound)

        if self.ball_y > SCREEN_HEIGHT - BALL_RADIUS:
            self.ball_y = SCREEN_HEIGHT - BALL_RADIUS
            arcade.play_sound(self.hit_sound)

        if self.square_x_position < SQUARE_LENGTH / 2:
            self.square_x_position = SQUARE_LENGTH / 2
            arcade.play_sound(self.hit_sound)

        if self.square_x_position > SCREEN_WIDTH - SQUARE_LENGTH / 2:
            self.square_x_position = SCREEN_WIDTH - SQUARE_LENGTH / 2
            arcade.play_sound(self.hit_sound)

        if self.square_y_position < SQUARE_HEIGHT / 2:
            self.square_y_position = SQUARE_HEIGHT / 2
            arcade.play_sound(self.hit_sound)

        if self.square_y_position > SCREEN_HEIGHT - SQUARE_HEIGHT / 2:
            self.square_y_position = SCREEN_HEIGHT - SQUARE_HEIGHT / 2
            arcade.play_sound(self.hit_sound)

    # All functions for pressing keys to move the square
    def on_key_press(self, key, key_modifiers):

        if key == arcade.key.RIGHT:
            print("Right pressed")
            self.square_change_x = SQUARE_MOVE_SPEED

        if key == arcade.key.UP:
            print("Up Pressed")
            self.square_change_y = SQUARE_MOVE_SPEED

        if key == arcade.key.DOWN:
            print("Down Pressed")
            self.square_change_y = -SQUARE_MOVE_SPEED

        if key == arcade.key.LEFT:
            print("Left pressed")
            self.square_change_x = -SQUARE_MOVE_SPEED

    # Called whenever user releases the keys
    def on_key_release(self, key, key_modifiers):

        if key == arcade.key.RIGHT:
            self.square_change_x = 0

        if key == arcade.key.UP:
            self.square_change_y = 0

        if key == arcade.key.DOWN:
            self.square_change_y = 0

        if key == arcade.key.LEFT:
            self.square_change_x = 0

    # Mouse movement
    def on_mouse_motion(self, x, y, delta_x, delta_y):

        self.ball_x = x
        self.ball_y = y

    # Whenever user presses left mouse button, sound plays
    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.coin_sound)


# Calling the "MyApplication" class so it will run
window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

# Running the Application
arcade.run()
