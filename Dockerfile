# init a base image (Alpine is small Linux distro)
FROM python:3.10-slim
# define the present working directory
WORKDIR /FastAPI
# copy the contents into the working dir
COPY . .
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python", "run.py"]
