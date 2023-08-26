import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

TEST_DB_HOST = os.environ.get("TEST_DB_HOST")
TEST_DB_PORT = os.environ.get("TEST_DB_PORT")
TEST_DB_NAME = os.environ.get("TEST_DB_NAME")
TEST_DB_USER = os.environ.get("TEST_DB_USER")
TEST_DB_PASSWORD = os.environ.get("TEST_DB_PASSWORD")

EVENT = os.environ.get("EVENT")
TOUR = os.environ.get("TOUR")
UNIVERSITY = os.environ.get("UNIVERSITY")
USER = os.environ.get("USER")
ROOT = os.environ.get("ROOT")

ALLOWED_HOSTS = ["77.232.135.31", "109.172.81.237"]

ORIGINS = [
    "http://109.172.81.237:8888",
    "http://109.172.81.237",
    "https://109.172.81.237:8888",
    "https://109.172.81.237",
    "http://77.232.135.31:8000",
    "http://77.232.135.31",
    "https://77.232.135.31:8000",
    "https://77.232.135.31",
]
