#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>

#define B 0xffffffffU

typedef struct
{
    unsigned int x;
    bool y;
} t1;

static unsigned int g = 0;

static void f1(void)
{
    puts("=== Math app for nerds v2.1 ===");
    puts(" 1) Check range  ");
    puts("2) Absolute value ");
    puts(" 3) Normalize input ");
    puts("4) Square number  ");
    puts("5) Clamp to 8-bit ");
    puts(" 6) Parity check ");
    puts("7) Statistics     ");
    puts(" 8) Exit          ");
}

static void f2(void)
{
    char b[50];
    int fd = open("flag.txt", O_RDONLY);
    if (fd == -1)
        exit(1);

    int n = read(fd, b, sizeof(b) - 1);
    b[n] = '\0';
    puts(b);
    close(fd);
}

static int f4(unsigned int v)
{
    unsigned int t = v;

    t = t + 1;

    if (t == 0)
    {
        if ((v & B) == B)
        {
            if (~v == 0)
            {
                return 1;
            }
        }
    }

    if (g != 0)
    {
        unsigned int f = v;
        f = f + 2;
        f = f - 2;
        if (f == 0)
            return 1;
    }

    return 0;
}

int main(void)
{
    char b[50];
    unsigned int c;
    unsigned int v;

    g = (unsigned int)time(NULL) % 256;

    f1();
    printf("> ");

    if (!fgets(b, sizeof(b), stdin))
        return 0;

    char *e;
    c = strtoul(b, &e, 10);
    if (c == 8)
        return 0;

    printf("Enter value: ");
    if (!fgets(b, sizeof(b), stdin))
        return 0;

    int tv = atoi(b);
    v = (unsigned int)tv;

    t1 container;
    container.x = v;
    container.y = false;

    switch (c)
    {
    case 1:
        puts("Range OK");
        break;

    case 2:
    {
        unsigned int av = container.x;
        if ((int)container.x < 0)
        {
            av = -container.x;
        }
        printf("Abs: %u\n", av);
    }
    break;

    case 3:
    {
        unsigned int n = container.x;

        container.y = true;

        unsigned int check = n;

        if (check == B)
        {
            if (f4(check))
            {
                f2();
                return 0;
            }
        }

        unsigned int r = n;
        if (r < B)
        {
            r = r + 1;
        }
        else
        {
            r = 0;
        }

        printf("Normalized: %u\n", r);
        break;
    }

    case 4:
    {
        unsigned long s = (unsigned long)container.x * container.x;
        printf("Square: %lu\n", s);
    }
    break;

    case 5:
        printf("Clamped: %u\n", container.x & 0xff);
        break;

    case 6:
        puts((container.x % 2) ? "Odd" : "Even");
        break;

    case 7:
        puts("Statistics complete");
        break;

    default:
        puts("Invalid option");
        break;
    }

    return 0;
}