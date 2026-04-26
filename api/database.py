import sqlite3
import json
from .config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            history TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_session_history(session_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT history FROM sessions WHERE session_id = ?", (session_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return json.loads(row[0])
    return []

def save_session_history(session_id, history):
    # Keep only last 20 messages
    if len(history) > 20:
        history = history[-20:]
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO sessions (session_id, history)
        VALUES (?, ?)
    ''', (session_id, json.dumps(history)))
    conn.commit()
    conn.close()
