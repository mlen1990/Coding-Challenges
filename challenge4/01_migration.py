from Properties import Properties
from Db import Db

properties = Properties.getProperties(False)

db = Db(properties);
db.execute("CREATE SCHEMA FileStorage DEFAULT CHARACTER SET 'utf8';");