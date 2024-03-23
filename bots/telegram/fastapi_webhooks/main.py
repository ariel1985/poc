
# main.py

# web framework for building APIs with Python
from fastapi import FastAPI
# local tunneling service for exposing local servers to the internet 
from pyngrok import ngrok, conf
# web server for ASGI applications
import uvicorn

# environment variable dotenv
from dotenv import load_dotenv
import os
load_dotenv()

NGROK_AUTH_KEY = os.getenv("NGROK_AUTH")
PORT = os.getenv("NGROK_PORT")
conf.get_default().auth_token = NGROK_AUTH_KEY

print('NGROK_AUTH', NGROK_AUTH_KEY)
print('PORT', PORT)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    # Server set up on local environment
    
    # Open a ngrok tunnel to the uvicorn server
    http_tunnel = ngrok.connect(PORT, bind_tls=True) # bind_tls for https
    public_url = http_tunnel.public_url
    print("Public URL:", public_url)

    # Now you can access the FastAPI server over the internet via the ngrok tunnel
    uvicorn.run(app, host="0.0.0.0", port=8000)