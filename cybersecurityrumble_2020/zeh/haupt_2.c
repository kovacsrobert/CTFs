#include <stdio.h>
#include <stdlib.h>
#include "fahne.h"

void main(void) {
    int i = rand();
    int k = 13;
    int e;
    int *p = &i;

    printf("%d\n", i);
    fflush(stdout);
    scanf("%d %d", &k, &e);

    for (int i = 7; i--;)
        k = (*p) >> (k % 3);

    k = k ^ e;

    if(k == 53225)
        puts(Fahne);
    else
        puts("War wohl void!");
}
