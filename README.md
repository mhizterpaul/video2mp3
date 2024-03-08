video to mp3 conversion service

This application demonstrates using the microservice architecture to manage a complex system by breaking the application(usually monolithic) into various components

It uses Docker, rabbitmq, kubernetes, mysql, mongodb, minikube(optional),  
and k9s(optional) for developing, managing and running the application

There are 5 services that make up this application

1 The Authentication Service
2 The Gateway Service
3 The Conversion Service
4 The Notification Service
5 The Message-brocker Service

If you are going to run this application on a windows machine using Docker Desktop for Windows  
you might run into issues getting minikube to tunnel requests to your kubernetes service/deployment. Here is a link to a related [problem](https://github.com/kantancoding/microservices-python/issues/18)  

To get started customizing this application:

Install the softwares listed above.
Cd into each child directory of the src directory and make an image, tag the build and push it to a registry.
cd into their manifest directory
update their deployment specification by editing the *-deploy.yaml file, find the image attribute and replace it with the correct registry
apply the various templates available to kubernetes to get the app running.

Refer to the video in the description for more information on how to use this application.

Feel free to modify this software to meet your requirements.