import os
import csv
from Properties import Properties
from Db import Db

function_map = {
	"TEXT": str,
	"INTEGER": int,
	"BOOLEAN": int,
	"DATE": str
}

properties = Properties.getProperties()
db = Db(properties)

spec_files = os.listdir("specs")
data_files = os.listdir("data")

# map files into a dictionary
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
		create_table_sql = "CREATE TABLE " + filename_info[0] + "(id INT NOT NULL AUTO_INCREMENT"
		for column in file:
			create_table_sql += ", {} {}".format(column[0], column[2])
			columns.append({"name": column[0], "width": int(column[1]), "data_type": column[2]})
		create_table_sql += ", PRIMARY KEY (id));"
		db.execute(create_table_sql);
		if filename_info[0] in file_map:
			for data_filename in file_map[filename_info[0]]:
				with open("data/" + data_filename, "rt") as data_file:
					for line in data_file:
						sql = "INSERT INTO " + filename_info[0] + " SET "
						index = 0
						fields = []
						for column in columns:
							fields.append(column["name"] + " = '" + str(function_map[column["data_type"]](line[index:(index + column["width"])])) + "'")
							index += column["width"]
						sql += ", ".join(fields)
						db.insert(sql)

