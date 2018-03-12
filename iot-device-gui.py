import sys,os
import curses

def draw_gui(stdscr,lights):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(0)
    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (True):
        if k == ord('q'): 
            lights ="off"
        else:
            lights ="on"
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Declaration of strings
        title = "Lights: " + lights
        statusbarstr = "SoftFIRE IOT Monitor | MMLab-AUEB"
        

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_y = int((height // 2) - 2)


        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)
        if lights == "on":stdscr.attron(curses.A_BLINK)

        # Rendering title
        if lights == "on": stdscr.addstr(start_y-1, start_x_title-5, "-------------------")
        stdscr.addstr(start_y, start_x_title, title)
        if lights == "on": stdscr.addstr(start_y+1, start_x_title-5, "-------------------")

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)
        if lights == "on":stdscr.attroff(curses.A_BLINK)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_gui,"off")

if __name__ == "__main__":
    main()
