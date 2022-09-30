# import image
FROM python:3

# create container
ENV PYTHONUNBUFFERED 1

#
WORKDIR /app

# take file we need and put it in container
# COPY example.py example.py
COPY . .

# run command on docker container
CMD ["python", "example.py"]


# docker build -f Dockerfile . -t example_server
# docker build build an image from commands and from the files
# -t = tag/name
# constructed an image which CAN be used to make a container


# docker run example_server
# creates a container


# volumes creates local USB drive/folder/connection between the files
# we're working on locally and the files that exist inside container

# docker run -v "$(pwd):/app" example_server
# want everything we're doing inside current folder to be directed inside
# this particular container in our app
