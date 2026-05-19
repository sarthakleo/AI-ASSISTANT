import sqlite3
from config import DB_PATH
from datetime import datetime

def init_db():
    """Create leads table if it does not exist."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
    CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    company TEXT,
    service TEXT,
    budget TEXT,
    message TEXT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def save_lead(name, email, phone, company, service, budget, message=''):
    """Save one business lead to SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        '''INSERT INTO leads
(name, email, phone, company, service, budget, message)
VALUES (?,?,?,?,?,?,?)''',
        (name, email, phone, company, service, budget, message)
    )
    conn.commit()
    conn.close()

def get_all_leads():
    """Return all leads as list of dicts."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        'SELECT * FROM leads ORDER BY timestamp DESC'
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]

# Auto-init when imported
init_db()