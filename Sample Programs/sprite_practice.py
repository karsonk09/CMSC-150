import random
import arcade

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


class MyApplication(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height)

        self.all_sprites_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0
        self.level = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

        self.coin_sound = arcade.load_sound("sounds/coin3.ogg")

    def setup(self):
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0
        self.level = 1

        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100

        self.all_sprites_list.append(self.player_sprite)

        for i in range(50):
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING * 0.40)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)
            self.all_sprites_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
        self.coin_list.draw()
        arcade.draw_text("Player Score: " + str(self.score), 10, 20, arcade.color.WHITE, 24)
        arcade.draw_text("Player Level: " + str(self.level), 590, 20, arcade.color.WHITE, 24)

    def animate(self, delta_time):

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            arcade.play_sound(self.coin_sound)
            coin.kill()
            self.score += 1

        if len(self.coin_list) == 0:
            self.level += 1
            for i in range(50 + (self.level * 2) + 10):
                coin = arcade.Sprite("coin_01.png", SPRITE_SCALING * 0.40)
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)
                self.coin_list.append(coin)
                self.all_sprites_list.append(coin)

        if len(self.coin_list) == 0 and self.level == 2:
            arcade.Sprite("coin_01.png", SPRITE_SCALING * 40)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()

    arcade.run()

main()
