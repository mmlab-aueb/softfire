from bf import PacketHandler,BFServer,BFClient
from random import randint
import sys,os
import curses
import time



class BFhandler(PacketHandler):
    
    def __init__(self):
        return
        self.screen = curses.initscr()
        self.draw_gui("off")

    def draw_gui(self,lights):
        print "Will set lights to " + lights
        return
        k = 0
        cursor_x = 0
        cursor_y = 0
         # Clear and refresh the screen for a blank canvas
        self.screen.clear()
        self.screen.refresh()
        curses.curs_set(0)
        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.screen.clear()
        height, width = self.screen.getmaxyx()

        # Declaration of strings
        title = "Lights: " + lights
        statusbarstr = "SoftFIRE IOT Monitor | MMLab-AUEB"
        

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_y = int((height // 2) - 2)


        # Render status bar
        self.screen.attron(curses.color_pair(3))
        self.screen.addstr(height-1, 0, statusbarstr)
        self.screen.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        self.screen.attroff(curses.color_pair(3))

        # Turning on attributes for title
        self.screen.attron(curses.color_pair(2))
        self.screen.attron(curses.A_BOLD)
        if lights == "on":self.screen.attron(curses.A_BLINK)

        # Rendering title
        if lights == "on": self.screen.addstr(start_y-1, start_x_title-5, "-------------------")
        self.screen.addstr(start_y, start_x_title, title)
        if lights == "on": self.screen.addstr(start_y+1, start_x_title-5, "-------------------")

        # Turning off attributes for title
        self.screen.attroff(curses.color_pair(2))
        self.screen.attroff(curses.A_BOLD)
        if lights == "on":self.screen.attroff(curses.A_BLINK)

        # Refresh the screen
        self.screen.refresh()
    def lights(self,value):
        if value == 1:
            self.draw_gui("on")
        else:
            self.draw_gui("off")
        
    def handle_packet(self,packet):
        options = packet.split("/")
        method  = options[1]
        uri     = options[2]
        if method == "PUT":
            payload = options[3]
            resource,value = payload.split("=")
            print payload + resource + value
            if resource == "lights":
                self.lights(value)
        if method == "GET":
            temperature = randint(20,30)
            client = BFClient()
            client.send_packet(0,str(temperature))

handler  =  BFhandler()
try:
    bfserver = BFServer(handler)
    bfserver.listen()
finally:
    curses.nocbreak(); 
    curses.echo()
    curses.endwin()

