#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#include "engine_process.h"

int engine_start(EngineProcess *engine, const char *script)
{
    int to_child[2];    /* [0] read end, [1] write end */
    int from_child[2];

    if (pipe(to_child) == -1 || pipe(from_child) == -1) {
        perror("pipe");
        return -1;
    }

    pid_t pid = fork();
    if (pid == -1) {
        perror("fork");
        return -1;
    }

    if (pid == 0) {
        dup2(to_child[0], STDIN_FILENO);
        dup2(from_child[1], STDOUT_FILENO);

        close(to_child[0]);
        close(to_child[1]);
        close(from_child[0]);
        close(from_child[1]);

        execlp("python3", "python3", "-u", script, (char *)NULL);

        perror("execlp");
        _exit(1);
    }

    close(to_child[0]);
    close(from_child[1]);

    engine->pid = pid;
    engine->to_engine = to_child[1];
    engine->from_engine = from_child[0];
    return 0;
}

int engine_send(EngineProcess *engine, const char *line)
{
    size_t length = strlen(line);

    if (write(engine->to_engine, line, length) == -1) return -1;
    if (write(engine->to_engine, "\n", 1) == -1) return -1;
    return 0;
}

int engine_read_line(EngineProcess *engine, char *buffer, size_t size)
{
    size_t used = 0;

    while (used + 1 < size) {
        char c;
        ssize_t n = read(engine->from_engine, &c, 1);

        if (n <= 0) return -1;
        if (c == '\n') break;
        buffer[used++] = c;
    }

    buffer[used] = '\0';
    return 0;
}

void engine_stop(EngineProcess *engine)
{
    close(engine->to_engine);
    close(engine->from_engine);
    waitpid(engine->pid, NULL, 0);
}

