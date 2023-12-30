# Overview

Docker Microservice: Keras / Tensorflow prediction api using the flask framework and a uwsgi server.

## Getting Started

### Docker

Build your docker image
```
docker build -t <your_image_name>
```

Run: image -> container & expose port 8080
```
docker run -p 8080:8080 <your_image_name> 
```


