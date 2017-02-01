import arcade


def draw_square(position_x, position_y):
    arcade.draw_rectangle_filled(position_x, position_y, 30, 30, arcade.color.BLACK)


def on_draw(delta_time):
    arcade.start_render()

    draw_square(on_draw.position_of_square_x, on_draw.position_of_square_y)
    on_draw.position_of_square_x = on_draw.position_of_square_x + 5
    on_draw.position_of_square_y = on_draw.position_of_square_y + 5

    if on_draw.position_of_square_x > 585:
        on_draw.position_of_square_x = on_draw.position_of_square_x - 5
    elif on_draw.position_of_square_x < 0:
        on_draw.position_of_square_x = on_draw.position_of_square_x + 5

    if on_draw.position_of_square_y > 585:
        on_draw.position_of_square_y = on_draw.position_of_square_y - 5
    elif on_draw.position_of_square_y < 0:
        on_draw.position_of_square_y = on_draw.position_of_square_y + 5

on_draw.position_of_square_x = 100
on_draw.position_of_square_y = 130



def main():
    arcade.open_window("bouncing square", 600, 600)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_draw, 1/80)
    arcade.run()

if __name__ == "__main__":
    main()