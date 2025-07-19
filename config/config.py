import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    username = os.getenv('USERNAME', '')
    password = os.getenv('PASSWORD', '')
    host = os.getenv('HOST', '')
    port = os.getenv('PORT', '')
    database  = os.getenv('DATABASE', '')

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False