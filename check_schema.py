import sqlite3

def check_schema():
    conn = sqlite3.connect('shiptivity.db')
    cursor = conn.cursor()
    
    print("Available tables:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        print(f"\nTable: {table[0]}")
        cursor.execute(f"PRAGMA table_info({table[0]})")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  Column: {col[1]} ({col[2]})")
    
    conn.close()

if __name__ == "__main__":
    check_schema()