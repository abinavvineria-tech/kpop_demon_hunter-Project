import curses
import os


def huntrix_editor(stdscr, filename):
    # Setup basic UI colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(1))

    content = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = [list(line.rstrip('\n')) for line in f.readlines()]

    if not content:
        content = [[]]

    y, x = 0, 0  # Cursor position

    while True:
        stdscr.clear()
        # Display the text
        for idx, line in enumerate(content):
            stdscr.addstr(idx, 0, "".join(line))

        # Display Status Bar
        height, width = stdscr.getmaxyx()
        status = f" HUNTRIX | File: {filename} | CTRL+S: Save | CTRL+Q: Quit "
        stdscr.addstr(height-1, 0, status[:width], curses.A_REVERSE)

        stdscr.move(y, x)
        key = stdscr.getch()

        if key == 17:  # CTRL+Q to Quit
            break
        elif key == 19:  # CTRL+S to Save
            with open(filename, 'w') as f:
                for line in content:
                    f.write("".join(line) + "\n")
        elif key == curses.KEY_BACKSPACE or key == 127:
            if x > 0:
                content[y].pop(x-1)
                x -= 1
            elif y > 0:  # Move line up
                x = len(content[y-1])
                content[y-1].extend(content.pop(y))
                y -= 1
        elif key == 10:  # Enter key
            new_line = content[y][x:]
            content[y] = content[y][:x]
            content.insert(y + 1, new_line)
            y += 1
            x = 0
        elif key == curses.KEY_UP and y > 0:
            y -= 1
            x = min(x, len(content[y]))
        elif key == curses.KEY_DOWN and y < len(content) - 1:
            y += 1
            x = min(x, len(content[y]))
        elif key == curses.KEY_LEFT and x > 0:
            x -= 1
        elif key == curses.KEY_RIGHT and x < len(content[y]):
            x += 1
        elif 32 <= key <= 126:  # Regular characters
            content[y].insert(x, chr(key))
            x += 1


if __name__ == "__main__":
    import sys
    fname = sys.argv[1] if len(sys.argv) > 1 else "untitled.txt"
    curses.wrapper(huntrix_editor, fname)
