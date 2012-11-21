#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[])
{
	int pipefd[2];
	pid_t cpid;
	pid_t c2pid;
	char buf, buf2;

	cpid = fork();
	c2pid = fork();

	if(cpid == -1 || c2pid == -1){
		perror("fork");
		exit(EXIT_FAILURE);
	}

	else if(cpid == 0){ // child process
		close(pipefd[1]);
		
		while(read(pipefd[0], &buf, 1) > 0)
			write(pipefd[1], &buf, 1);

		close(pipefd[0]);
		execve("./generator.cpp", NULL, NULL);
		fprintf(stderr, "child[%d] exited with status %d\n", getpid(), 0 );

		waitpid(cpid, 0 , WNOHANG);
		exit(EXIT_SUCCESS);
	}

	else if(c2pid == 0){ // child process
		close(pipefd[1]);
		
		while(write(pipefd[1], &buf2, 1) > 0)
			read(pipefd[0], &buf2, 1);

		close(pipefd[1]);
		execve("./consumer.cpp", NULL, NULL);
		fprintf(stderr, "child[%d] exited with status %d\n", getpid(), 0 );
		wait(0);
		exit(EXIT_SUCCESS);
	}

	else if(cpid > 0 || c2pid > 0){ // parent process
		close(pipefd[0]);
		close(pipefd[1]);
		wait(NULL);
		// exit(EXIT_SUCCESS);	
	}


sleep(1);

kill (cpid, SIGTERM);

}
