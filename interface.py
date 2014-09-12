import sh
import curses
import argparse
#adb_path = "/home/malik/adt/adt-bundle-linux-x86_64-20140702/sdk/platform-tools/adb"


class AndroidVirtualKeyboard(object):
    def __init__(self, adb_path, key_file="binding"):
        print(adb_path)
        self.adb = sh.Command(adb_path)
        self.stdscr = None
        self.binding = {}
        self.__parse_binding(key_file)

    def __parse_binding(self, binding_file_path):
        for line in open(binding_file_path):
            stripped_line = line.split('#', 2)[0].strip()
            if stripped_line:
                curse_key, adb_key = map(int,map(str.strip, stripped_line.split(':')))
                self.binding[curse_key] = adb_key

    def send_key(self, key):
        pass

    def main_loop(self):
        while 1:
            c = self.stdscr.getch()
            self.stdscr.addstr(0, 0, "{!s} --> {!s}".format(c, self.binding.get(int(c), ''), curses.A_REVERSE)

    def start(self):
        self.stdscr = curses.initscr()
        curses.noecho()

    def end(self):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="A simple keyboard")
    parser.add_argument('--adb_path', '-p', nargs='?', help='specify adb path', default='adb')
    args = parser.parse_args()
    virtual_keyboard = AndroidVirtualKeyboard(args.adb_path)
    virtual_keyboard.start()
    virtual_keyboard.main_loop()
