#ifndef ENGINE_PROCESS_H
#define ENGINE_PROCESS_H

#include <stddef.h>
#include <sys/types.h>

typedef struct {
    pid_t pid;
    int to_engine;    /* C writes here -> Python stdin */
    int from_engine;  /* C reads here  <- Python stdout */
} EngineProcess;

int engine_start(EngineProcess *engine, const char *script);
int engine_send(EngineProcess *engine, const char *line);
int engine_read_line(EngineProcess *engine, char *buffer, size_t size);
void engine_stop(EngineProcess *engine);

#endif
