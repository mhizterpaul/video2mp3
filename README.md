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

tried to get logs from the controller 
like so: kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
I0119 00:31:32.833517       8 controller.go:190] "Configuration changes detected, backend reload required"
I0119 00:31:32.834550       8 event.go:298] Event(v1.ObjectReference{Kind:"Ingress", Namespace:"default", Name:"gateway-ingress", UID:"18cf170b-0597-4095-a504-de57e2d6b7e5", APIVersion:"networking.k8s.io/v1", ResourceVersion:"14282", FieldPath:""}): type: 'Normal' reason: 'Sync' Scheduled for sync
I0119 00:31:33.006704       8 controller.go:210] "Backend successfully reloaded"
I0119 00:31:33.007403       8 event.go:298] Event(v1.ObjectReference{Kind:"Pod", Namespace:"ingress-nginx", Name:"ingress-nginx-controller-7c6974c4d8-bxl2k", UID:"6cac6b2e-1b2b-4747-938e-e408921261cf", APIVersion:"v1", ResourceVersion:"5426", FieldPath:""}): type: 'Normal' reason: 'RELOAD' NGINX reload triggered due to a change in configuration
W0119 00:31:38.122705       8 controller.go:1214] Service "default/gateway" does not have any active Endpoint.
I0119 00:31:38.122881       8 controller.go:190] "Configuration changes detected, backend reload required"
I0119 00:31:38.229332       8 controller.go:210] "Backend successfully reloaded"
I0119 00:31:38.229814       8 event.go:298] Event(v1.ObjectReference{Kind:"Pod", Namespace:"ingress-nginx", Name:"ingress-nginx-controller-7c6974c4d8-bxl2k", UID:"6cac6b2e-1b2b-4747-938e-e408921261cf", APIVersion:"v1", ResourceVersion:"5426", FieldPath:""}): type: 'Normal' reason: 'RELOAD' NGINX reload triggered due to a change in configuration
I0119 00:31:59.521956       8 status.go:304] "updating Ingress status" namespace="default" ingress="gateway-ingress" currentValue=null newValue=[{"ip":"192.168.49.2"}]
I0119 00:31:59.777238       8 event.go:298] Event(v1.ObjectReference{Kind:"Ingress", Namespace:"default", Name:"gateway-ingress", UID:"18cf170b-0597-4095-a504-de57e2d6b7e5", APIVersion:"networking.k8s.io/v1", ResourceVersion:"14339", FieldPath:""}): type: 'Normal' reason: 'Sync' Scheduled for sync
W0118 22:36:03.355438       1 client_config.go:618] Neither --kubeconfig nor --master was specified.  Using the inClusterConfig.  This might not{"err":"secrets \"ingress-nginx-admission\" not found","level":"info","msg":"no secret found","source":"k8s/k8s.go:229","time":"2024-01-18T22:36:04Z"}
{"level":"info","msg":"creating new secret","source":"cmd/create.go:28","time":"2024-01-18T22:36:04Z"}
W0118 22:36:23.471541       1 client_config.go:618] Neither --kubeconfig nor --master was specified.  Using the inClusterConfig.  This might not work.
{"level":"info","msg":"patching webhook configurations 'ingress-nginx-admission' mutating=false, validating=true, failurePolicy=Fail","source":"k8s/k8s.go:118","time":"2024-01-18T22:36:24Z"}
:"2024-01-18T22:36:26Z"}

I couln't find any helpful information

I'm stuck and cannot complete this application..
if you get to complete this on your local machine using windows please do let me know, perhaps I have to tinker with it a bit longer to figure what the problem is