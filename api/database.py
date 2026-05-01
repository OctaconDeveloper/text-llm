import aiosqlite
import sqlite3
import json
from .config import DB_PATH
from .cache import cache

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        # Enable WAL mode for better concurrency
        await db.execute("PRAGMA journal_mode=WAL")
        await db.execute("PRAGMA synchronous=NORMAL")
        
        await db.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                history TEXT
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
                profile_id TEXT PRIMARY KEY,
                traits TEXT
            )
        ''')
        await db.commit()

async def create_profile(profile_id, traits):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT INTO profiles (profile_id, traits)
            VALUES (?, ?)
        ''', (profile_id, json.dumps(traits)))
        await db.commit()
    
    # Update cache
    await cache.set(f"profile:{profile_id}", traits)

async def get_profile(profile_id):
    # Try cache first
    cached = await cache.get(f"profile:{profile_id}")
    if cached:
        return cached

    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT traits FROM profiles WHERE profile_id = ?", (profile_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                traits = json.loads(row[0])
                # Populate cache
                await cache.set(f"profile:{profile_id}", traits)
                return traits
    return None

async def get_session_history(session_id):
    # Try cache first
    cached = await cache.get(f"session:{session_id}")
    if cached:
        return cached

    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT history FROM sessions WHERE session_id = ?", (session_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                history = json.loads(row[0])
                # Populate cache
                await cache.set(f"session:{session_id}", history)
                return history
    return []

async def save_session_history(session_id, history, limit=20):
    # Keep only last N messages if limit is provided
    if limit is not None and len(history) > limit:
        history = history[-limit:]
    
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT OR REPLACE INTO sessions (session_id, history)
            VALUES (?, ?)
        ''', (session_id, json.dumps(history)))
        await db.commit()
    
    # Update cache
    await cache.set(f"session:{session_id}", history)
