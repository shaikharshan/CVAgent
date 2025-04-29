import sqlite3
from datetime import date
import time

DB_PATH = r"db\CVAgentDB.db"  # Adjust path if needed

# Function to connect to the DB
def connect_db():
    conn = sqlite3.connect(DB_PATH, timeout=10, isolation_level=None)  # isolation_level=None enables autocommit
    conn.execute("PRAGMA journal_mode=WAL")  # Enable WAL for concurrent access
    return conn


# Function to get a user by credentials
def getUser(email: str, password: str, role: str):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM User WHERE email=? AND password=? AND role=?
            """, (email, password, role))
            return cursor.fetchone()
    except Exception as e:
        return None

