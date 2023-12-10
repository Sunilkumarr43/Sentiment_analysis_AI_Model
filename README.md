# Sentiment_analysis_AI_Model
Develop a simple AI model and set up a deployment pipeline using Docker and Kubernetes. The candidate will also need to create a basic web service (using either Python or Go Lang) that interacts with the AI model and stores results in a MySQL database.
For this example, let's create a simple Python script for sentiment analysis using a pre-trained model. You can use libraries like TensorFlow or PyTorch.

#step1:
#pretrained model(optional) or you can use your model for this based on your project.
First, it is necessary to develop a pre-trained model using TensorFlow and Keras, incorporating positive and neutral text for training within the code. Subsequently, the model will be saved as an .h5 file using the `model.save` function.It will automatically create the file in specified path.

#step2:
Create a sentment_analysis_model.py file
The code defines a sentiment analysis model (`sentiment_analysis_model.py`) using TensorFlow and Keras. It loads a pre-trained sentiment analysis model stored in an .h5 file. The model uses a tokenizer to process positive and neutral texts. The `analyze_sentiment` function takes a text input, tokenizes it, and predicts its sentiment (positive or negative) using the loaded model. The result is based on the model's prediction threshold of 0.5.

#step3:
Create a Basic Web Service
Create a simple web service using a framework like Flask in Python.
The code (`web_service.py`) sets up a Flask web service that exposes an API endpoint at `/analyze_sentiment`. This endpoint accepts POST requests with JSON data containing a "text" field. The received text is then passed to the `analyze_sentiment` function from the `sentiment_analysis_model` module. The sentiment analysis result (positive or negative) is returned as a JSON response. Additionally, the code includes commented-out sections demonstrating how to store the results in a MySQL database, with placeholders for database logic. The service runs on `0.0.0.0:5000` in debug mode when executed directly.

#step4:
Set up Deployment Pipeline using Docker
Create a Dockerfile for your web service.
The provided Dockerfile is used to build a Docker image for a Python application. It starts with the official Python 3.8 slim base image. The working directory is set to `/app`, and the `requirements.txt` file is copied to the working directory. Then, it installs the Python dependencies listed in `requirements.txt` using `pip`. Finally, the entire content of the current directory is copied into the container's working directory. The command `CMD ["python", "web_service.py"]` specifies the default command to run when the container starts, which is to execute the `web_service.py` script using Python. This Dockerfile is suitable for containerizing a Python web service.

#step5:
#Create a requirements.txt file listing the required Python packages based on your code and system requirements.
Flask==2.0.2
Werkzeug==2.0.0
tensorflow>=2.8.0

#step6:
Build and Test Docker Image Locally using 
->docker build -t sentiment-analysis-service .
->docker run -p 5000:5000 sentiment-analysis-service
The provided commands are used to build and test a Docker image locally for a sentiment analysis service. The `docker build -t sentiment-analysis-service .` command builds a Docker image tagged as "sentiment-analysis-service" using the current directory as the build context. The `docker run -p 5000:5000 sentiment-analysis-service` command runs a container based on the built image, mapping port 5000 on the host to port 5000 on the container. This allows the locally built sentiment analysis service to be accessed at `http://localhost:5000`.

#step7:
Deploy to Kubernetes.
Apply the configurations to your Kubernetes cluster.
->Create Kubernetes #deployment.yaml file.
The provided YAML file is a Kubernetes Deployment configuration for a sentiment analysis service. It defines the desired state of the deployment, specifying that three replicas of the sentiment analysis service should run. The deployment uses a pod template with a container running the `sentiment-analysis-service` image, exposing port 5000. This configuration enables scalable deployment and management of the sentiment analysis service in a Kubernetes cluster.
->Create #service.yaml file.
The provided YAML file is a Kubernetes Service configuration for the sentiment analysis service. It defines a service named `sentiment-analysis-service` that exposes the sentiment analysis deployment to external traffic. The service uses a LoadBalancer type to automatically provision an external IP address and distribute incoming traffic to the sentiment analysis pods. The service listens on port 80 and forwards traffic to port 5000 on the selected pods. Applying this configuration to a Kubernetes cluster enables external access to the sentiment analysis service.
 
 #step8:
->kubectl apply -f deployment.yaml
->kubectl apply -f service.yaml
The provided commands, `kubectl apply -f deployment.yaml` and `kubectl apply -f service.yaml`, are essential for deploying and exposing the sentiment analysis service on a Kubernetes cluster. The deployment command applies the configurations specified in `deployment.yaml`, creating three replicas of the sentiment analysis service with load balancing. The service command applies the configurations in `service.yaml`, creating a LoadBalancer service that exposes the sentiment analysis service to external traffic, enabling external access to the service through the assigned external IP address and port. Together, these commands facilitate the deployment and accessibility of the sentiment analysis service within a Kubernetes environment.

#step9:
Accessing the Web Service
Once deployed, you can access the web service using the external IP provided by the LoadBalancer service.

Now you have a basic AI model, a web service, and a deployment pipeline using Docker and Kubernetes. Adapt the code and configurations as needed for your specific use case and MySQL database integration.



