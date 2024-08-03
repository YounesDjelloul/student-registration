from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from app.sql_app.database import db
from app.sql_app.models import StudentApplication

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Server is UP"


@app.post("/applications/")
async def create_application(application: StudentApplication):
    result = db.applications.insert_one(application.model_dump())
    if not result.inserted_id:
        raise HTTPException(status_code=400, detail="Failed to create application")
    return {"message": "Application created successfully"}


@app.get("/applications/")
async def get_all_applications():
    applications = list(db.applications.find({}, {"_id": 0}))
    return {"applications": [StudentApplication(**studentApp) for studentApp in applications]}
