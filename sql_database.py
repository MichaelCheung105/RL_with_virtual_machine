import pyodbc

server = "enter server name"
database = 'enter database name'
username = "enter user name"
password = "enter password"
driver = '{ODBC Driver 17 for SQL Server}'


class SqlDB:
    def __init__(self):
        cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.cnxn = cnxn
        self.cursor = cnxn.cursor()

    def create_table_as_experience_pool(self, table_name: str, table_cols: dict, is_overwrite=False):
        if not is_overwrite:
            raise Exception ("Table: '{0}' already exist. Killing programme now".format(table_name))
        else:
            # Completing drop_table_string
            drop_table_string = "DROP TABLE IF EXISTS {0}".format(table_name)

            # Completing create_table_string
            create_table_string = "CREATE TABLE {0} (".format(table_name)
            for key, values in table_cols.items():
                col_name = key
                data_type = values['data_type']
                constraint = values['constraint']
                create_table_string += "{0} {1} {2}, ".format(col_name, data_type, constraint)
            create_table_string.rstrip(", ")
            create_table_string += ")"

            # Execute drop table and create table
            self.cursor.execute(drop_table_string)
            print("Successfully dropped table: {0}".format(table_name))
            self.cursor.execute(create_table_string)
            print("Successfully created table: {0}".format(table_name))
            self.cnxn.commit()
            print("Table dropping and creation command committed")

    def insert_experience(self, table_name: str, experience_tuple: tuple):
        try:
            insert_row_string = "INSERT INTO {0} values {1}".format(table_name, str(experience_tuple))
            self.cursor.execute(insert_row_string)
            self.cnxn.commit()
        except Exception as e:
            print("Fail to insert experience. See Exception\n")
            print(e)

    def extract_experience_pool(self, table_name: str):
        try:
            select_statement_string = "SELECT * FROM {0}".format(table_name)
            self.cursor.execute(select_statement_string)
            return self.cursor.fetchall()
        except Exception as e:
            print("Fail to extract experience. See Exception\n")
            print(e)
