# Dockerized Flask App Boilerplate
http://localhost:8080/

## Docker usage
```
docker build -t flask_boiler .
docker run -d -p 8080:8080 flask_boiler (host:container)
docker ps -a
docker logs {CONTAINER ID}
docker stop {CONTAINER ID}
```
