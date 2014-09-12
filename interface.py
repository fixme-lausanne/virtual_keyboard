import sh
import curses
import argparse
#adb_path = "/home/malik/adt/adt-bundle-linux-x86_64-20140702/sdk/platform-tools/adb"


class AndroidVirtualKeyboard(object):
    def __init__(self, adb_path, key_file="binding"):
        print(adb_path)
        self.adb = sh.Command(adb_path)
        self.binding = {}
        self.__parse_binding(key_file)

    def __parse_binding(self, binding_file_path):
        for line in open(binding_file_path):
            stripped_line = line.split('#', 2)[0]
            curse_key, adb_key = map(int,map(str.strip, stripped_line.split(':')))
            self.binding[curse_key] = adb_key

    def send_key(self, key):
        pass

    def main_loop():
        while 1:
            c = stdscr.getch()
            stdscr.addstr(0, 0, str(c), curses.A_REVERSE)

    def start():
        stdscr = curses.initscr()
        curses.noecho()

    def end():
        curses.nocbreak(); stdscr.keypad(0); curses.echo()
        curses.endwin()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="A simple keyboard")
    parser.add_argument('--adb_path', '-p', nargs='?', help='specify adb path', default='adb')
    args = parser.parse_args()
    virtual_keyboard = AndroidVirtualKeyboard(args.adb_path)

    #main_loop()

