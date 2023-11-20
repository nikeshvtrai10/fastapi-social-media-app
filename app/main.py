from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from . import models, config 
from .database import engine
from .routers import post, user, auth, vote

# Command to generate all the tables in the postgres database
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello World"}