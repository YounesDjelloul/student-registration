from pymongo import MongoClient

from app.settings import Settings

settings = Settings()

client = MongoClient(settings.DATABASE_URL)

db = client.registration_db