#include <stdio.h>
#include <time.h>

const int BUFFER_SIZE = 10;

int main()
{
    char buf[BUFFER_SIZE];
    time_t t;
    struct tm *ts;

    t = time(NULL);
    ts = localtime(&t);

    strftime(buf, BUFFER_SIZE, "%A", ts);
    printf("%s\n", buf);

    strftime(buf, BUFFER_SIZE, "%B", ts);
    printf("%s\n", buf);

    printf("Serafim\n");

    return 0;
}
