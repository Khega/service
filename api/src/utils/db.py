import mysql.connector

def db_get_data(query):

    db_config = {
        "host": "your_host",
        "user": "your_username",
        "password": "your_password",
        "database": "your_database",
    }

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()
        conn.close()
