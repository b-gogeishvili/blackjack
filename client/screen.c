#include <ncurses.h>

#include "screen.h"

void screen_run(void) {
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    printw("Blackjack\n");
    printw("h: hit | s: Stand | q: Quit\n");
    refresh();

    int key;
    while ((key = getch()) != 'q') {
        move(3, 0);
        clrtoeol();

        switch (key) {
            case 'h':
                printw("You chose Hit");
                break;
            case 's':
                printw("You chose Stand");
                break;
            default:
                printw("Unknown key");
                break;
        }

        refresh();
    }

    endwin();
}

