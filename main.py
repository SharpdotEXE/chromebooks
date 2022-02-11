import mysql.connector
from mysql.connector import Error

database = 'chromebooks'
pw = 'wav11@@wav11'
create_database_query = 'CREATE DATABASE chromebooks'

create_chromebook_table = """
CREATE TABLE chromebooks (
    cb_ID INT PRIMARY KEY,
    cb_location VARCHAR(15) NOT NULL,
    cb_service_tag VARCHAR(7) NOT NULL,
    cb_issue VARCHAR(40) NOT NULL,
    cb_status VARCHAR(15) NOT NULL,
    cb_date_acquired DATE,
    cb_warranty_exp DATE
    );
"""

cb_ID = 1
cb_location = 'Crowder'
cb_service_tag = 'ABC123'
cb_issue = 'Screen'
cb_status = 'On the way'
cb_date_acquired = '2021-01-15'
cb_warranty_exp = '2022-03-14'

add_chromebook = '''
INSERT INTO chromebooks (cb_ID, cb_location, cb_service_tag, cb_issue, cb_status, cb_date_acquired, cb_warranty_exp)
VALUES (%s, %s, %s, %s, %s, %s, %s)
'''

columns = [
    (cb_ID, cb_location, cb_service_tag, cb_issue, cb_status, cb_date_acquired, cb_warranty_exp)
]


drop_table = """
DROP TABLE chromebooks
"""


select_all = """
SELECT *
FROM chromebooks;
"""

delete_chromebook = """
DELETE FROM chromebooks WHERE cb_service_tag = %s;
"""
sn = [('ABC123')]


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Database created succesfully')
    except Error as err:
        print(f'Error: "{err}"')

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query successful')
    except Error as err:
        print(f'Error: "{err}"')

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f'Error: "{err}"')

def execute_add_chromebook(connection, add_chromebook, columns):
    cursor = connection.cursor()
    try:
        cursor.executemany(add_chromebook, columns)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def execute_delete_chromebook(connection, delete_chromebook, sn):
    cursor = connection.cursor()
    try:
        cursor.execute(delete_chromebook, sn)
        connection.commit()
        print('Query successful')
    except Error as err:
        print(f'Error: "{err}"')


connection = create_db_connection("localhost", "root", pw, database)
# create_database(connection, create_database_query)
# drop_and_add(connection)
# execute_query(connection, drop_table)
# execute_query(connection, create_chromebook_table)
# execute_add_chromebook(connection, add_chromebook, columns)
# execute_delete_chromebook(connection, delete_chromebook, sn)

results = read_query(connection, select_all)

for result in results:
  print(result)
