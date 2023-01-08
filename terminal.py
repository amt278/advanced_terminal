import curses
from curses import wrapper
import time

def main(scr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    black_red = curses.color_pair(1)

    scr.clear()
    scr.addstr(0, 10, "samo 3lekooooooo", curses.A_UNDERLINE)
    scr.addstr(2, 10, "samo 3lekooooooo", black_red)
    scr.addstr(4, 10, "samo 3lekooooooo", curses.A_UNDERLINE | black_red)

    scr.refresh()
    scr.getch()

wrapper(main)