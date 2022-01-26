import mysql.connector
from mysql.connector import Error
import pandas as pd

database = 'chromebooks'
pw = 'wav11@@wav11'
create_database_query = 'CREATE DATABASE chromebooks'

from_db = []
columns = ['ID', 'Location', 'Service Tag', 'Issue', 'Status', 'Date Acquired', 'Warranty Expiration Date']


create_chromebook_table = """
CREATE TABLE chromebooks (
    cb_id INT PRIMARY KEY,
    cb_location VARCHAR(15) NOT NULL,
    cb_service_tag VARCHAR(7) NOT NULL,
    cb_issue VARCHAR(40) NOT NULL,
    cb_status VARCHAR(15) NOT NULL,
    cb_date_acquired DATE,
    cb_warranty_expiration DATE
    );
"""

cb_ID = 0
cb_location = 'Krebs'
cb_service_tag = 'ABCD123'
cb_issue = 'Broken screen'
cb_status = 'box on way'
cb_date_acquired = '2021-12-15'
cb_warranty_exp = '2022-01-25'




add_chromebook = f"""
INSERT INTO chromebooks VALUES
({cb_ID}, {cb_location}, {cb_service_tag}, {cb_issue}, {cb_status}, {cb_date_acquired}, {cb_warranty_exp});
""".format(cb_ID = cb_ID, cb_location = cb_location, cb_service_tag = cb_service_tag, cb_issue = cb_issue,
           cb_status = cb_status, cb_date_acquired = cb_date_acquired, cb_warranty_exp = cb_warranty_exp)

drop_table = """
DROP TABLE chromebooks
"""


query1 = """
SELECT *
FROM chromebooks WHERE Location = Krebs;
"""

delete_chromebook = """
DELETE FROM chromebooks WHERE cb_location = cb_location;
"""



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


connection = create_db_connection("localhost", "root", pw, database)
# create_database(connection, create_database_query)
# execute_query(connection, drop_table)
# execute_query(connection, create_chromebook_table)
execute_query(connection, add_chromebook)
# execute_query(connection, delete_chromebook)

# results = read_query(connection, q5)
#
# for result in results:
#   print(result)
