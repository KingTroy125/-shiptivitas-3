import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Connect to database
conn = sqlite3.connect('shiptivity.db')

# First verify the table names
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Available tables:", [t[0] for t in tables])

# Query 1: Daily Active Users
df_users = pd.read_sql_query("""
    SELECT 
        date(timestamp) as day,
        COUNT(DISTINCT user_id) as daily_active_users,
        CASE 
            WHEN date(timestamp) < '2018-06-02' THEN 'Before Kanban'
            ELSE 'After Kanban'
        END as period
    FROM user_actions  -- This table name might need to be updated
    GROUP BY date(timestamp)
    ORDER BY day
""", conn)

# Query 2: Status Changes
df_changes = pd.read_sql_query("""
    SELECT 
        date(timestamp) as day,
        COUNT(*) as daily_status_changes,
        CASE 
            WHEN date(timestamp) < '2018-06-02' THEN 'Before Kanban'
            ELSE 'After Kanban'
        END as period
    FROM status_changes  -- This table name might need to be updated
    GROUP BY date(timestamp)
    ORDER BY day
""", conn)

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Plot 1: Daily Active Users
plt.figure(figsize=(12, 6))
plt.clf()  # Clear any existing plots
sns.lineplot(data=df_users, x='day', y='daily_active_users', hue='period')
plt.title('Daily Active Users Before and After Kanban Implementation')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/daily_users.png')

# Plot 2: Status Changes
plt.figure(figsize=(12, 6))
plt.clf()  # Clear any existing plots
sns.lineplot(data=df_changes, x='day', y='daily_status_changes', hue='period')
plt.title('Daily Status Changes Before and After Kanban Implementation')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/status_changes.png')

conn.close()