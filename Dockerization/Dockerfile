# We are creating the docker file so that our application has it's own operating system, repos, and libraries.

# defining the docker image 

FROM  python:3.8

# Here we are creating code working directory where all the files and libraries will be stored and the app will be running from this folder.

WORKDIR /code

# copy the requirements and all the necessary files in the code directory.

COPY ./requirements.txt /code/requirements.txt

# Now we will run the commands inside the contains

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy the code file in the app folder. 

COPY ./app /code/app

# app will be exposed to the port 8000,  


EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]

# CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
