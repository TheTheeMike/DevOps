import mysql.connector

mysql_config = {
    'host': 'mysql-server',
    'user': 'root',
    'password': 'password',
    'database': 'test_database',
}

try:
    connection = mysql.connector.connect(**mysql_config)
    print("Connected to MySQL!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")

