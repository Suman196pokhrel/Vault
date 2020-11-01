import mysql.connector


class sqlConnections:

    def __init__(self):
        self.mydb = None
        self.mycursor = None

    def establish_connection(self):
        self.mydb = mysql.connector.connect(host='your_local_host_name',
                                            user="Your Server Usermane",
                                            password="Server password",
                                            database='Your databse Name')

    def create_database(self, createDB_querry='CREATE DATABASE Your Database Name'):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(createDB_querry)

    def delete_database(self, dropDB_querry='DROP DATABASE Your Database Name'):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(dropDB_querry)

        # def create_table(createTBL_querry='CREATE TABLE General_Client_Inforation(First_Name VARCHAR(100), Last_Name VARCHAR(100),Contact_Number VARCHAR(20),Username VARCHAR(100),Password VARCHAR(100))'):
        #     self.mycursor = self.mydb.cursor()
        #     self.mycursor.execute(createTBL_querry)

    def create_table(self, Username='Any_Name'):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            f'CREATE TABLE {Username} (Email VARCHAR(100),Password VARCHAR(100))')

    def show_tables(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('SHOW TABLES')
        for x in self.mycursor:
            print(x)

    def add_row_in_general(self,table_name= 'general_client_inforation',values=''):
        self.mycursor = self.mydb.cursor()
        sql = f'INSERT INTO {table_name}(First_Name,Last_Name,Contact_Number,Username,Password) VALUES (%s, %s, %s, %s, %s)'
        val = values
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def add_row_in_personal(self, table_name='', values=''):
        self.mycursor = self.mydb.cursor()
        sql = f'INSERT INTO {table_name}(Email,Password) VALUES (%s, %s)'
        val = values

        self.mycursor.execute(sql,val)
        self.mydb.commit()

    def read_data(self,table_name = 'general_client_information'):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(f'SELECT Username,Password FROM {table_name}')
        records = self.mycursor.fetchall()
        # print(records)
        return records

    def row_col_count (self,table_name):
        self.mycursor = self.mydb.cursor()
        rows = self.mycursor.execute(f'SELECT * FROM {table_name}')
        print('Qyerry Executed')
        data = self.mycursor.fetchall()
        print(data)
        if not data:
            return 0,0,0
        else:
            columns = len(data[0])
            rows =  len(data)
            print('Data Fetched')
            return rows,columns,data

    def delete_all_rows(self,Username_1):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(f'DELETE FROM {Username_1}')





if __name__ == '__main__':
    obj = sqlConnections()
    obj.establish_connection()
    # create_database()
    # delete_database()
    # obj.add_row()
    # obj.create_table()
    # obj.show_tables()
    obj.read_data()
