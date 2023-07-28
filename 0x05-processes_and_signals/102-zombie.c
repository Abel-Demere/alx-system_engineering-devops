#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
* infinite_while - Function to run an infinite loop with a sleep of 1 second.
* This function will be used to keep the program running and
* create the zombie processes.
* Return: Always 0.
*/
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main - function to create zombie processes.
 * The program will fork a child process 5 times, and each child process
 * will exit immediately, becoming a zombie.
 * Return: Always 0.
 */

int main(void)
{
int i;
pid_t child_pid;

for (i = 0;  i < 5;  i++)
{
child_pid = fork();
if (child_pid == 0)
{
printf("Zombie process created, PID: %d\n", getpid());
exit(0);
}
}

infinite_while();

return (0);
}
