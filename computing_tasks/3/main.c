#include <stdio.h>

int main()
{
    char buf[6];

    for (int i = 0; i < 5; i++)
    {
        buf[i] = '0';
        buf[i + 1] = '\0';
        printf("%s\n", buf);
    }
}
