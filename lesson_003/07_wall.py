# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
brick_width, brick_height = 60, 20
width = 600
height = 600

sd.set_screen_size(width+200, height+200)
start_line_x = 0

for horizontal_line in range(start_line_x, height, brick_height):
    start_line_point = sd.get_point(start_line_x, horizontal_line)
    end_line_point = sd.get_point(width, horizontal_line)
    sd.line(start_line_point, end_line_point)

    if (horizontal_line + brick_height) % (brick_height * 2):
        x_shift = brick_width / 2
    else:
        x_shift = 0

    for vertical_line in range(0, width, brick_width):
        start_line_point = sd.get_point(vertical_line + x_shift, horizontal_line)
        end_line_point = sd.get_point(vertical_line + x_shift, horizontal_line + brick_height)
        sd.line(start_line_point, end_line_point)

sd.pause()
