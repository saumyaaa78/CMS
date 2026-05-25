from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.upload import router as upload_router

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:5173",
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

app.include_router(upload_router)

@app.get("/")
def root():
    return {
        "message": "Cleanza Backend Running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
