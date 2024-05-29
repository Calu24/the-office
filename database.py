import datetime
import pyodbc

class Database:    
    EMPLOYEE = 'employee'
    EMPLOYEE_ID = 'emp_id'
    BRANCH = 'branch'
    BRANCH_ID = 'branch_id'
    CLIENT = 'client'
    CLIENT_ID = 'client_id'
    WORKS_WITH = 'works_with'
    BRANCH_SUPPLIER = 'branch_supplier'
    
    def __init__(self, connection_string: str):
        self.conn = pyodbc.connect(connection_string)
    
    def get_by_db_name(self, db_name: str):
        query = f"SELECT TOP (1000) * FROM [dbo].[{db_name}]"

        cursor = self.conn.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        result = []
        for row in rows:
            d = {}
            for i, col in enumerate(cursor.description):
                if isinstance(row[i], datetime.date):
                    d[col[0]] = row[i].isoformat()
                else:
                    d[col[0]] = row[i]
            result.append(d)
                
        data = {
            "data": result
        }
        return data
    
    def insert_by_db_name(self, db_name: str, data: dict):
        cursor = self.conn.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' * len(data))
        values = [value for value in data.values()]
        
        cursor.execute(f"INSERT INTO {db_name} ({columns}) VALUES ({placeholders})", values)
        self.conn.commit()
    
    def delete_by_name_and_id(self, db_name: str, db_id: str, id_row: int):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM {db_name} WHERE {db_id} = ?", (id_row,))
        self.conn.commit()
    
    def delete_by_name_and_supplier_name(self, db_name: str, supplier_name: str):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM {db_name} WHERE supplier_name = ?", (supplier_name,))
        self.conn.commit()
    
    def delete_by_name_and_employee_id_and_client_id(self, db_name: str, employee_id: int, client_id: int):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM {db_name} WHERE emp_id = ? AND client_id = ?", (employee_id, client_id))
        self.conn.commit()
    
    def close_connection(self):
        self.conn.close()