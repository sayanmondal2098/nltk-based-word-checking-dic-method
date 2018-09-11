#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
    pid_t d;
    d = fork();
    
    if (d<0) {
        printf("Error.....");
    }
    
    else if (d==0)
    {
        printf("within child\n");
    }
    else{
        printf("within parent\n");
    }
    
    
}
