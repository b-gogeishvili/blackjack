#include <ncurses.h>

void greeting() {	
    char name[100];  // buffer to store input
	initscr(); // Start curses mode
	printw("Enter your name: ");
    getnstr(name, sizeof(name)-1);
	refresh(); // Refresh screen
	printw("Hi %s", name);
    refresh();
	getch();
	endwin();
}


int main() {
    greeting();
}
