import os
import csv
from Properties import Properties
from Db import Db

class TestSuite:

	def test(self, spec_filename):
		function_map = {
			"TEXT": str,
			"INTEGER": int,
			"BOOLEAN": int,
			"DATE": str
		}

		properties = Properties.getProperties()
		db = Db(properties)

		data_files = os.listdir("data")

		file_map = {}
		for data_file in data_files:
			file_info = data_file.split("_")
			if not file_info[0] in file_map:
				file_map[file_info[0]] = []
			file_map[file_info[0]].append(data_file)

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



	def run_tests(self):
		number_of_tests = 2
		passed = number_of_tests
		# Test 1
		try:
			spec_file = "testformat1.csv"
			self.test(spec_file)
			print("Test 1: {} -- PASSED!".format(spec_file))
		except Exception as e:
			print("Test 1: {} -- FAILED!".format(spec_file))
			passed -= 1

		# Test 2
		try:
			spec_file = "testformat2.csv"
			self.test(spec_file)
			print("Test 2: {} -- PASSED!".format(spec_file))
		except Exception as e:
			print("Test 2: {} -- FAILED!".format(spec_file))
			passed -= 1
		if passed == number_of_tests:
			print("All Tests PASSED :)")
		else:
			print("{} out of 2 Tests PASSED".format(passed))

test = TestSuite()
test.run_tests()