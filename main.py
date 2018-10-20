#!/usr/bin/python
import tcod
import ui
from config import SCREEN_WIDTH, SCREEN_HEIGHT, MAX_FPS


def main():
    tcod.console_set_custom_font(
        'terminal16x16.png',
        tcod.FONT_LAYOUT_ASCII_INCOL,
    )
    tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, b'Fleeing the Fray',
                           False)
    tcod.sys_set_fps(MAX_FPS)
    ui.handle_main_menu()

if __name__ == '__main__':
    main()
