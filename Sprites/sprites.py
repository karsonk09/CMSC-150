import random
import arcade

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600


class MyApplication(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height)

        self.all_sprites_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING)
        self.all_sprites_list.append(self.player_sprite)


def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()

    arcade.run()

main()
