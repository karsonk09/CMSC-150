import random
import arcade
import math

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


class Bullet(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.bottom > SCREEN_HEIGHT:
            self.kill()
        if self.left > SCREEN_WIDTH:
            self.kill()


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

        self.angle = 0
        self.radius = 0
        self.angle_speed = 0
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        self.center_x = math.sin(self.angle) * self.radius + self.circle_center_x
        self.center_y = math.cos(self.angle) * self.radius + self.circle_center_y

        self.angle += self.angle_speed


class MyApplication(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height)

        self.all_sprites_list = None
        self.coin_list = None
        self.bullet_list = None

        self.player_sprite = None
        self.reticle = None
        self.score = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.reticle = arcade.Sprite("reticle.png", SPRITE_SCALING)

        self.score = 0

        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING)
        self.player_sprite.left = 0
        self.player_sprite.bottom = 0

        self.all_sprites_list.append(self.player_sprite)
        self.all_sprites_list.append(self.reticle)

        for i in range(50):
            coin = Coin("coin_01.png", SPRITE_SCALING * 0.40)

            coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            coin.circle_center_y = random.randrange(SCREEN_HEIGHT)
            coin.radius = random.randrange(10, 200)
            coin.angle = random.random() * 2 * math.pi
            coin.angle_speed = 0.008

            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)

    def on_mouse_press(self, x, y, button, modifiers):
        bullet = Bullet("laserBlue01.png", SPRITE_SCALING * 1.5)
        self.all_sprites_list.append(bullet)
        self.bullet_list.append(bullet)

        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        angle = math.atan2(y_diff, x_diff)
        print("Angle: " + str(angle))

        bullet.change_x = math.cos(angle) * 5
        bullet.change_y = math.sin(angle) * 5

        bullet.angle = math.degrees(angle)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
        self.coin_list.draw()
        arcade.draw_text("Player Score: " + str(self.score), 10, 20, arcade.color.WHITE, 24)

    def animate(self, delta_time):

        self.all_sprites_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            coin.kill()
            self.score += 1

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
            for coin in hit_list:
                coin.kill()
                bullet.kill()
                self.score += 1

    def on_mouse_motion(self, x, y, dx, dy):
        self.reticle.center_x = x
        self.reticle.center_y = y

def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()

    arcade.run()

main()
