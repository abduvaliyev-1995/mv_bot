
import sqlite3

class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
                CREATE TABLE Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date_id BIGINT NOT NULL,
                    tg_id BIGINT NOT NULL,
                    name varchar(255) NOT NULL,
                    fullName varchar(255) NULL,
                    username varchar(255) NULL,
                    phone_num varchar(15) NULL,
                    address varchar(500) NULL,
                    appeal varchar NULL,
                    language varchar(3) NULL
                    );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        # print(sql)
        return sql, tuple(parameters.values())

    def add_user(self, date_id: int, tg_id: int, name: str, fullName: str=None, username: str=None, phone_num: str = None, address: str=None, appeal: str=None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
                INSERT INTO Users(date_id, tg_id, name, fullName, username, phone_num, address, appeal, language) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
        self.execute(sql, parameters=(date_id, tg_id, name, fullName, username, phone_num, address, appeal, language), commit=True)

    def select_all_users(self):
        sql = """
                SELECT * FROM Users
                """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_username(self, username, date_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
                UPDATE Users SET username=? WHERE date_id=?
                """
        return self.execute(sql, parameters=(username, date_id), commit=True)

    def update_user_phone_num(self, phone_num, date_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
                UPDATE Users SET phone_num=? WHERE date_id=?
                """
        return self.execute(sql, parameters=(phone_num, date_id), commit=True)

    def update_user_fullName(self, fullName, date_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
                UPDATE Users SET fullName=? WHERE date_id=?
                """
        return self.execute(sql, parameters=(fullName, date_id), commit=True)

    def update_user_address(self, address, date_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
                UPDATE Users SET address=? WHERE date_id=?
                """
        return self.execute(sql, parameters=(address, date_id), commit=True)

    def update_user_appeal(self, appeal, date_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
                UPDATE Users SET appeal=? WHERE date_id=?
                """
        return self.execute(sql, parameters=(appeal, date_id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

def logger(statement):
    print(f"""
        _____________________________________________________
        Executing:
        {statement}
        _____________________________________________________
        """)




