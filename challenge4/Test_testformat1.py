import os
import csv
from Properties import Properties
from Db import Db

class Test_testformat1:

	def test1(self):
		function_map = {
			"TEXT": str,
			"INTEGER": int,
			"BOOLEAN": int
		}

		properties = Properties.getProperties()
		db = Db(properties)

		spec_files = os.listdir("specs")
		data_files = os.listdir("data")

		file_map = {}
		for data_file in data_files:
			file_info = data_file.split("_")
			if not file_info[0] in file_map:
				file_map[file_info[0]] = []
			file_map[file_info[0]].append(data_file)

		for spec_filename in spec_files:
			with open("specs/" + spec_filename, "rt") as spec_file:
				filename_info = spec_filename.split(".")
				file = csv.reader(spec_file, delimiter=",")
				next(file) # Skip first row
				columns = []
				for column in file:
					columns.append({"name": column[0], "width": int(column[1]), "data_type": column[2]})
				if filename_info[0] in file_map:
					for data_filename in file_map[filename_info[0]]:
						with open("data/" + data_filename, "rt") as data_file:
							for line in data_file:
								sql = "SELECT count(*) as total FROM {} WHERE ".format(filename_info[0])
								index = 0
								fields = []
								for column in columns:
									fields.append(column["name"] + " = '" + str(function_map[column["data_type"]](line[index:(index + column["width"])])) + "'")
									index += column["width"]
								sql += " AND ".join(fields)
								row = db.select(sql)[0]
								if row["total"]	!= 1:
									raise Exception("Line: {} was not inserted".format(line.strip()))
		print("Test 1: PASSED!")



	def test(self):
		self.test1()
		# Test_testformat1.test1()

test = Test_testformat1()
test.test()