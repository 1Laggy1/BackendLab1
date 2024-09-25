A program madded by Shchigol Andrew IM-23 for backend subject.

# How to start

To start a program locally use docker run or docker compose

docker run 
1 docker build . -t backendlab1:latest

2 docker run -it --rm -p 80:80 -e PORT=80 backendlab1:latest

You can access it now with http://127.0.0.1/healthcheck

Docker compose

1 docker-compose build

2 docker-compose up

Get access with http://127.0.0.1:10000/healthcheck

Also this project is deployed on render.com.

You can access now without downloading source code with https://backendlab1-tgv7.onrender.com/healthcheck
