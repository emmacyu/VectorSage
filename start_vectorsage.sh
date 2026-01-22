#!/bin/bash
# -----------------------------
# VectorSage starting script
# -----------------------------

python3.10 -m venv /Users/Test/coding-projects/venv_vectorsage
source /Users/Test/coding-projects/venv_vectorsage/bin/activate

# 1. upgrade pip and install dependency
echo "Upgrading pip and installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 2. check MongoDB connection
echo "Checking MongoDB connection..."
python3 - <<END
from pymongo import MongoClient, errors
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()
    db = client[DB_NAME]
    if COLLECTION_NAME not in db.list_collection_names():
        db.create_collection(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' created!")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists!")
except errors.ServerSelectionTimeoutError as err:
    print("Cannot connect to MongoDB.")
    print(err)
    exit(1)
END

# 3. start VectorSage
echo "Starting VectorSage..."
python3 src/main.py
