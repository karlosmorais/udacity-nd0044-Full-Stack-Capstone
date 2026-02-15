
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_db():
    try:
        # Connect to the default postgres database
        conn = psycopg2.connect("user=postgres password=postgres host=localhost port=5432 dbname=postgres")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        
        # Check if database exists
        cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'casting_agency'")
        exists = cur.fetchone()
        
        if not exists:
            cur.execute("CREATE DATABASE casting_agency")
            print("Database 'casting_agency' created successfully.")
        else:
            print("Database 'casting_agency' already exists.")
            
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error creating database: {e}")

if __name__ == "__main__":
    create_db()
