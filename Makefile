CC = gcc
CFLAGS = -Wall -Wextra -g
LDLIBS = -lncurses

BUILD_DIR = build
TARGET = $(BUILD_DIR)/blackjack
SOURCES = client/main.c client/screen.c client/engine_process.c
HEADERS = client/screen.h client/engine_process.h

$(TARGET): $(SOURCES) $(HEADERS)
	mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) $(SOURCES) -o $(TARGET) $(LDLIBS)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -rf $(BUILD_DIR)

.PHONY: run clean
