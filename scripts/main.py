import ncurses

ncurses.main() # initialize ncurses
ncurses.init_screen()
ncurses.parse_input()

flagfinder.start(ncurses.get_command())
