import sqlite3
from datetime import datetime

conn = sqlite3.connect('cc_killer.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()


create_proxies_table = """
    CREATE TABLE IF NOT EXISTS proxies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        ip TEXT UNIQUE NOT NULL,
        port INTEGER NOT NULL,
        proxy_type TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        dead INTEGER DEFAULT 0
    );
"""

create_actions_table = """
    CREATE TABLE IF NOT EXISTS actions (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_command TEXT NOT NULL
    );

"""

create_users_table = """
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name text, 
    user_name text, 
    menu text, 
    last_used timestamp);
"""

############## SELECT

select_proxies = """
    SELECT * FROM proxies
"""

select_last_command = """
    SELECT * FROM actions
    WHERE user_id = ?;
"""

############## INSERT

insert_proxy = """
    INSERT INTO proxies (user_id, ip, port, proxy_type, updated_at)
    VALUES (?, ?, ?, ?, ?);
"""

############## UPDATE

upsert_user_action = """
        INSERT INTO actions (user_id, last_command)
        VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET last_command = excluded.last_command
    """

############## CHECK
check_user_exists = """
"""


def initialize_tables():
    cur.execute(create_proxies_table)
    cur.execute(create_actions_table)
    conn.commit()

def add_proxy(user_id, ip, port, proxy_type):
    try:        
        cur.execute(insert_proxy, (user_id, ip, port, proxy_type, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        
    except:
        pass

def add_update_action(user_id, action):
    try:        
        cur.execute(upsert_user_action, (user_id, action))
        conn.commit()
        
    except:
        pass
    
def get_user_action(user_id):
    try:        
        result = cur.execute(select_last_command, (user_id,))
        
        return result.fetchone()['last_command']
    
    except:
        pass
    
def get_proxies():
    try:        
        result = cur.execute(select_proxies)
        
        return result.fetchall()
    
    except:
        pass
