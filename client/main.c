#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "engine_process.h"
#include "screen.h"

int main(void)
{
    signal(SIGPIPE, SIG_IGN);

    EngineProcess engine;
    if (engine_start(&engine, "engine/server.py") == -1) {
        return EXIT_FAILURE;
    }

    engine_send(&engine, "deal");

    char line[128];
    while (engine_read_line(&engine, line, sizeof(line)) == 0) {
        if (strcmp(line, "END") == 0) {
            break;
        }
        printf("got: %s\n", line);
    }

    engine_stop(&engine);

    // screen_run();
    return EXIT_SUCCESS;
}
