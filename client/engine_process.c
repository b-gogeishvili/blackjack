#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(void)
{
    pid_t pid = fork();

    switch(pid) {
    case -1:
        perror("fork");
        return EXIT_FAILURE;

    case 0:
        execlp(
            "python3",
            "python3 main.py",
            (char *)NULL
        );

        perror("execlp")
        return EXIT_FAILURE;

    default:
        if (waitpid(pid, NULL, 0) == -1) {
            perror("waitpid");
            return EXIT_FAILURE;
        }
        printf("Exiting...\n");
    }

    return EXIT_SUCCESS;
}
