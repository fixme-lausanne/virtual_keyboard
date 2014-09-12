import sh
import curses
adb_path = "/home/malik/adt/adt-bundle-linux-x86_64-20140702/sdk/platform-tools/adb"
stdscr = curses.initscr()

adb = sh.Command(adb_path)
curses.noecho()


def send_command(key):
    pass

def main_loop():
    while 1:
        c = stdscr.getch()
        stdscr.addstr(0, 0, str(c),
                                curses.A_REVERSE)

def end():
    curses.nocbreak(); stdscr.keypad(0); curses.echo()
    curses.endwin()

if __name__ == '__main__':
    main_loop()

