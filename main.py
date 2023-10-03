from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import authentication.auth_router as auth_router
import uvicorn


import os

host = os.getenv("GAS_BACKEND_HOST")
port = os.getenv("GAS_BACKEND_PORT")

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=host, port=int(port))
    
