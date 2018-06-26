import sys

from Properties import Properties
from Db import Db


class Migration_20180625:

	def __init__(self):
		self.properties = Properties.getProperties(False)

	def migrate(self):
		db = Db(self.properties);
		db.execute("CREATE SCHEMA FileStorage DEFAULT CHARACTER SET 'utf8';");

	def rollback(self):
		db = Db(self.properties);
		db.execute("DROP SCHEMA FileStorage;");

migration = Migration_20180625()

if len(sys.argv) != 2:
	raise Exception("Invalid number of command line arguments.")
if sys.argv[1] == "migrate":
	migration.migrate()
elif sys.argv[1] == "rollback":
	migration.rollback()
else:
	raise Exception("Invalid migration setting: {}".format(sys.argv[1]))