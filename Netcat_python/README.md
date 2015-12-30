#Build a netcat using python 

Any network hacker will defintely familiar with netcat the renowned TCP/IP Swiss Army Knife, and now we are building one ourselves Python style. 

Some of the main feature of this app includes:

1)Server - to listen
2)Execution of files - when received a connection
3)Command - initialize a command shell
4)upload - to upload a file to server 

- h to check what commands are available. 

Code is being compiled with 5 functions and a main() 


1)run_command() 

we are able to pop a shell using this command and to avoid nasty stuff happens, we will strip all whitespace.
subprocess allows you to run external command 
and print out the output from your command.

2)client_handler

This will handle incoming client connection and we first check if there is any upload and add it into 'data'. If there is upload we will try to write a destination we declare earlier.

3)server_loop()
This is to loop and create thread for each connections when listening

4)client_sender
Like before, declaring IP, port and connections then check if there is any uploads and send it over. received message from server then allows user to send messages.

5)usage
manual page

6)main
try to retrieve all argument submit by user and match with predefined funciton and execute it accordingly.

Reference : Black hat Python 
