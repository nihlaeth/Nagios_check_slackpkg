#include <unistd.h>
#include <sys/types.h>
#include <string.h>

int main(int argc, char *argv[]) {
    setreuid(geteuid(), geteuid());
    setregid(getegid(), getegid());
    if (strcmp(argv[1], "check-updates") == 0) {
        char c[] = "slackpkg check-updates";
        strcpy(argv[0], strtok(c," "));
        argv[1] = strtok(0, " ");
        return execv("/usr/sbin/slackpkg", argv);
    } else if (strcmp(argv[1], "update") == 0) {
        char c[] = "slackpkg update";
        strcpy(argv[0], strtok(c, " "));
        argv[1] = strtok(0, " ");
        return execv("/usr/sbin/slackpkg", argv);
    } else if (strcmp(argv[1], "upgrade-all") == 0) {
        char c[] = "slackpkg -dialog=off -default_answer=n -batch=on upgrade-all";
        strcpy(argv[0], strtok(c, " "));
        argv[1] = strtok(0, " ");
        argv[2] = strtok(0, " ");
        argv[3] = strtok(0, " ");
        argv[4] = strtok(0, " ");
        return execv("/usr/sbin/slackpkg", argv);
    }
    return 3;
}
