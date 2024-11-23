<<<<<<< HEAD
#Host the server code for backend
#To be able to call the server from any other website.
=======
#host the server code that we need to make the chat app work

#these settings are  to be able to call the servers from any other website
>>>>>>> 356f2f468418e76feb2128864b0c9e6bd1780e86
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

<<<<<<< HEAD
import requests

=======
>>>>>>> 356f2f468418e76feb2128864b0c9e6bd1780e86
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
PRIVATE_KEY = "..."

=======
>>>>>>> 356f2f468418e76feb2128864b0c9e6bd1780e86
class User(BaseModel):
    username: str

@app.post('/authenticate')
async def authenticate(user: User):
<<<<<<< HEAD
    response = requests.put('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username,
        },
        headers={ "Project-ID": PRIVATE_KEY }
    )
    return response.json()
=======
    return {}
>>>>>>> 356f2f468418e76feb2128864b0c9e6bd1780e86
