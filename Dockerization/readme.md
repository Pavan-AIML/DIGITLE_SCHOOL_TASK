<h1> In this folder we will see how can we build a docker image and run the container in the AWS service. </h1>

- After listing all the necessary files in docker file we will create the docker image first by running the command "docker build -t myimage ." (t -> tag it , last . for the docker file in the same directory)

- run the container by using the command "docker run --name pavancontainernw -p 8000:8000 myimage"

- Follow the link for the fastapi docker https://fastapi.tiangolo.com/deployment/docker/#dockerfile

- Create the repository in docker hub.

- tag the image by "docker tag docker_image_name dockerhub_reponame"

- Now check the created image in the docker desktop. 

- 