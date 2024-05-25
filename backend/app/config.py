import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)))
load_dotenv(dotenv_path)


class Config:
    KEY = ""


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URL = os.getenv("PRODUCTION_DATABASE_URL")


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = os.getenv("DEVELOPMENT_DATABASE_URL")
