import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
SQUARE_LENGTH = 35
SQUARE_HEIGHT = 35
TRIANGLE_COORDINATES = []
SQUARE_MOVE_SPEED = 3


class Square:
    def __init__(self, position_x, position_y, change_x, change_y, side_length, side_height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.side_length = side_length
        self.side_height = side_height
        self.color = color


class MyApplication(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        # Draw the Square
        self.square_x_position = 150
        self.square_y_position = 300
        self.square_change_x = 3
        self.square_change_y = 3

        # Draw the Triangle
        self.triangle_x1_y1 = [100, 50]
        TRIANGLE_COORDINATES.append(self.triangle_x1_y1)

        self.triangle_x2_y2 = [50, 50]
        TRIANGLE_COORDINATES.append(self.triangle_x2_y2)

        self.triangle_x3_y3 = [75, 100]
        TRIANGLE_COORDINATES.append(self.triangle_x3_y3)

        self.triangle_movement = 1

        arcade.set_background_color(arcade.color.BLACK)

        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        # self.set_update_rate(1/80)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        arcade.set_background_color(arcade.color.BLACK)

        arcade.draw_triangle_filled(TRIANGLE_COORDINATES[0][0], TRIANGLE_COORDINATES[0][1], TRIANGLE_COORDINATES[1][0],
                                    TRIANGLE_COORDINATES[1][1], TRIANGLE_COORDINATES[2][0], TRIANGLE_COORDINATES[2][1],
                                    arcade.color.RED_DEVIL)

        arcade.draw_rectangle_filled(self.square_x_position, SCREEN_HEIGHT // 2, SQUARE_LENGTH, SQUARE_HEIGHT,
                                     arcade.color.ALLOY_ORANGE)

    def animate(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # Move the ball
        # self.ball_x_position += self.ball_x_pixels_per_second * delta_time

        # Did the ball hit the right side of the screen while moving right?
        """
        if self.ball_x_position > SCREEN_WIDTH - BALL_RADIUS \
                and self.ball_x_pixels_per_second > 0:
            self.ball_x_pixels_per_second *= -1

        # Did the ball hit the left side of the screen while moving left?
        if self.ball_x_position < BALL_RADIUS \
                and self.ball_x_pixels_per_second < 0:
            self.ball_x_pixels_per_second *= -1
        """

        self.square_x_position += self.square_change_x * delta_time
        self.square_y_position += self.square_change_y * delta_time

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://pythonhosted.org/arcade/arcade.key.html
        """

        # See if the user hit Shift-Space
        # (Key modifiers are in powers of two, so you can detect multiple
        # modifiers by using a bit-wise 'and'.)
        if key == arcade.key.SPACE and key_modifiers == arcade.key.MOD_SHIFT:
            print("You pressed shift-space")

        # See if the user just hit space.
        elif key == arcade.key.SPACE:
            print("You pressed the space bar.")

        if key == arcade.key.RIGHT:
            print("Right pressed")
            self.square_change_x = SQUARE_MOVE_SPEED

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.SPACE:
            print("You stopped pressing the space bar.")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass


window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
