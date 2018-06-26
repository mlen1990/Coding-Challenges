import mysql.connector

from mysql.connector import errorcode

class Db: 

	def __init__(self, properties):
		self.connection = mysql.connector.connect(**properties)

	def insert(self, sql):
		self.execute(sql)
		self.connection.commit()

	def update(self, sql):
		self.execute(sql)
		self.connection.commit()

	def select(self, sql, dictionary=True):
		if dictionary:
			cursor = self.connection.cursor(cursor_class=MySQLCursorDict)
		else:
			cursor = self.connection.cursor()
		cursor.execute(sql)

		rows = cursor.fetchall()
		cursor.close()
		return rows;

	def execute(self, sql):
		cursor = self.connection.cursor()
		try:
			cursor.execute(sql)
		except mysql.connector.Error as err:
			print("Error executing: " + sql)
			print(err)
		cursor.close()

class MySQLCursorDict(mysql.connector.cursor.MySQLCursor):
    def _row_to_python(self, rowdata, desc=None):
        row = super(MySQLCursorDict, self)._row_to_python(rowdata, desc)
        if row:
            return dict(zip(self.column_names, row))
        return None

