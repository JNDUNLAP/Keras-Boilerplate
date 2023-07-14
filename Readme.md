# ML in Logistics
Lots of low handing fruit for ml optimization in logistics.
From inbound emails, pricing models, market segementation, route optimization, bin packing ... etc
You can quickly adjust this nlp model serving bolier plate to fit many use cases.

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
curl -X POST -H "Content-Type: application/json" -d '{"text":"Hi can you please quote me on this lane out of Norfolk? We need rates soon."}' http://localhost:8080/predict
```
