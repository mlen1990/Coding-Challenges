import mysql.connector

from mysql.connector import errorcode

class Db: 

	def __init__(self, properties):
		self.connection = mysql.connector.connect(**properties)

	def insert(self, sql):
		print(sql)

	def update(self, sql):
		print(sql)

	def select(self, sql):
		print(sql)


	def execute(self, sql):
		cursor = self.connection.cursor()
		try:
			cursor.execute(sql)
		except mysql.connector.Error as err:
			print("Error executing: " + sql)
		cursor.close()