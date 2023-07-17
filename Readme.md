# Docker


## Getting Started

### Docker

Build your docker image
```
docker build -t <name>
```

Run the image as a container and expose port 8080
```
docker run -p 8080:8080 <name> sh
```

Test the API
```
curl -X POST -H "Content-Type: application/json" -d '{"text":"example_text"}' http://localhost:8080/predict
```
