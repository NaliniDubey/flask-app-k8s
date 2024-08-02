This project uses Flask to respond to an HTTP GET request and returns:
Timestamp
Hostname
Endpoint: http://<host-dns>/info

##Prerequisites:
Docker
Kubernetes (Minikube recommended for local testing)
Python 3.9


##Detailed Instructions on How to Build the Application
###Steps:
1. Navigate to the Project Directory:
   sh
   cd /path/to/AdjustProject/AdjustProject

2. Build the Docker Image and Push to Docker Hub:

   a. Build the Docker image:
   sh
   docker build -t <your-dockerhub-username>/<image-name>:latest .
   
   b. Log in to Docker Hub (if not already logged in):
   sh
   docker login
   
   c. Push the Docker image to Docker Hub:
   sh
   docker push <your-dockerhub-username>/<image-name>:latest

3. Update Files:

   a. Update deployment.yaml:
      i. Change the image name to the one defined above:
          yaml
          containers:
           - name: adjust-container
             image: <your-dockerhub-username>/<image-name>:latest

      ii. Add Basic Authentication (Optional):
          Base64 encode your username and password. The default username/password is user/user:
          Update AUTH_USER and AUTH_PASSWORD in deployment.yaml secrets section:
          yaml
          data:
            AUTH_USER: base64_encoded_username
            AUTH_PASSWORD: base64_encoded_password

   b. Update ingress.yaml:

   Change the host to your preferred DNS:
   yaml
   rules:
     - host: <your-preferred-dns>

4. Apply the Kubernetes Configurations:
Ensure you are in the directory containing your Kubernetes configuration files.

sh
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml

5. Access the Application:
The application should be available at:

sh
http://<host-dns>/info


##Testing the Code with Minikube

For testing the deployment using Minikube, follow the same steps above. Additionally, map the NodePort IP to the DNS provided in /etc/hosts.

1. Start Minikube:

sh
minikube start

2. Get Minikube IP:

sh
minikube ip

3. Map Minikube IP to DNS:
Open /etc/hosts and add an entry mapping the Minikube IP to your preferred DNS:

sh
sudo nano /etc/hosts
Add the line:
php
<minikube-ip> <your-preferred-dns>

4. Access the Application:
You should be able to access the application at:

sh
http://<your-preferred-dns>/info
