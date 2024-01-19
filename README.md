video to mp3 conversion service

This project tries to create an application that uses the microservice architecture

it uses Docker, rabbitmq, kubernetes, mysql, mongodb, minikube, 
and k9s for developing, managing and running the application

there are 5 services that make up this application

if you are going to run this application on a windows(10) pc like me
then we might have the same development experience

you might get some benign errors while trying to using minikube 

like this: Unable to resolve the current Docker CLI context "default": context "default" does not exist
and this: failed to close the audit log: invalid argument

and minikube tunnel prompting for password which requires configuring ssh keys
like below
icacls c:\\Users\\user\\.minikube\\machines\\minikube\\id_rsa /inheritance:r
icacls c:\\Users\\user\\.minikube\\machines\\minikube\\id_rsa /grant:r "%username%:(R)"
ssh-add c:\Users\user\.minikube\machines\minikube\id_rsa

I'm currently facing problems actually getting the tunnel service to run
after enabling ingress addon in minikube 
like so:
minikube addons enable ingress
all pods and service required to access to the rabbitmq management console are running but I do not
see any active http process listening at port 8080 for the auth service or even at 15672 on localhost

https://github.com/kantancoding/microservices-python/issues/18