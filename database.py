import psycopg2

# PostgreSQL connection parameters
DB_NAME = "zeeproc_chatbot"
DB_USER = "postgres"  # Change if you have a different username
DB_PASSWORD = "aryan"  # Replace with your PostgreSQL password
DB_HOST = "localhost"
DB_PORT = "5432"  # Default PostgreSQL port

def connect_db():
    """Establishes a connection to PostgreSQL and returns the connection object."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("✅ Successfully connected to the database.")
        return conn
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return None

# Test the connection
if __name__ == "__main__":
    conn = connect_db()
    if conn:
        conn.close()
        print("✅ Connection closed successfully.")
