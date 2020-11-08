# fastapi-pingpong

This is my testing of deployment for an app using FastAPI's framework while exploring both GET and POST Request APIs endpoints.

To test out this app, ensure that you have `Docker`, `Docker Compose` and `curl` installed.

Once you have the above installed, you can clone the repo into a local repo by typing the following instructions in the command line:

```
git clone https://github.com/kfoofw/fastapi-pingpong

# change to project repo
cd fastapi-pingpong
```

## 1. Build and Run the App using Docker-Compose.

Once within the directory itself, you can use `Docker Compose` to build the image and run it locally.

```
docker-compose up -d --build
```

The resultant container exposes the port of the localhost `8002` so this will be used in the following step.

## 2. API consumption/testing

The app itself can be explored in 2 ways with its RESTful APIs endpoints:
- (a) GET Request on `localhost:8002/ping`
- (b) POST Request on `localhost:8002/what_is_ping`

### 2(a) GET Request

Based on the GET Request, all you have to do is to type `localhost:8002/ping` on your browser and you should see the following:

```
{"ping":"pong!"}
```

Alternatively, you can also type in the following in the Terminal/command line:

```
curl localhost:8002/ping
```

and it should result in the following:

```
{"ping":"pong!"}
```

### 2(b) POST Request

With the POST Request, the app will return different output messages based on the input message.

To test the "right" message, you can type out the following in the Terminal/command line:

```
curl --data '{"message":"ping"}' --request POST localhost:8002/what_is_ping
```

and you should observe the following output:

```
{"ret_message":"Pong!"}
```

To test the "wrong" message, you can type out the following in the Terminal/command line:

```
curl --data '{"message":"not ping"}' --request POST localhost:8002/what_is_ping
```

and you should observe the following output:

```
{"ret_message":"No Ping so no Pong!"}
```
