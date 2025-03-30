import sqlite3

conn = sqlite3.connect('shiptivity.db')
cursor = conn.cursor()

# Create tables
cursor.executescript("""
CREATE TABLE IF NOT EXISTS user_actions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    timestamp DATETIME,
    action TEXT
);

CREATE TABLE IF NOT EXISTS status_changes (
    id INTEGER PRIMARY KEY,
    card_id INTEGER,
    timestamp DATETIME,
    old_status TEXT,
    new_status TEXT
);

-- Add sample data
INSERT INTO user_actions (user_id, timestamp, action) VALUES 
    (1, '2018-05-01 10:00:00', 'login'),
    (2, '2018-05-01 11:00:00', 'view'),
    (1, '2018-06-03 09:00:00', 'login'),
    (2, '2018-06-03 10:00:00', 'edit');

INSERT INTO status_changes (card_id, timestamp, old_status, new_status) VALUES
    (1, '2018-05-01 10:30:00', 'todo', 'in_progress'),
    (2, '2018-05-01 11:30:00', 'todo', 'in_progress'),
    (1, '2018-06-03 09:30:00', 'in_progress', 'done'),
    (2, '2018-06-03 10:30:00', 'in_progress', 'done');
""")

conn.commit()
conn.close()
print("Database setup complete!")