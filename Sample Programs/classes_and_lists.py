import arcade

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, ball_x, ball_y, change_x, change_y, radius, color):

        self.ball_x = ball_x
        self.ball_y = ball_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.ball_x, self.ball_y, self.radius, self.color)

    def animate(self):
        self.ball_x += self.change_x
        self.ball_y += self.change_y

        if self.ball_x < self.radius:
            self.change_x *= -1

        if self.ball_y < self.radius:
            self.change_y *= -1

        if self.ball_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.ball_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyBallGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.ball_list = []

        ball = Ball(200, 350, 3, 3, 15, arcade.color.YELLOW)
        self.ball_list.append(ball)

        ball = Ball(100, 100, 3, 3, 15, arcade.color.BLACK)
        self.ball_list.append(ball)

        ball = Ball(250, 400, -3, -3, 15, arcade.color.BLUE)
        self.ball_list.append(ball)

    def on_draw(self):
        arcade.start_render()

        for ball in self.ball_list:
            ball.draw()

    def animate(self, delta_time):
        for ball in self.ball_list:
            ball.animate()

window = MyBallGame(640, 480, "My Ball Game")

arcade.run()
