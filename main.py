from fastapi import FastAPI, Depends, Path
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routers import auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:8000",  # Adjust this to the origin you are using
    "http://127.0.0.1:8000",
    "http://127.0.0.1:54591",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(auth.router)



# List the origins that are allowed to make requests to this server
# Use '*' to allow all origins. Be cautious with this in a production environment.


