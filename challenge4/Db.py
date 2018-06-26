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

	def select(self, sql, as_dictionary=True):
		cursor = self.connection.cursor(dictionary=as_dictionary)

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