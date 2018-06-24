class Properties:

	user = "root"
	password = "froebielsm"
	host = '127.0.0.1'
	schema = "FileStorage"

	@staticmethod
	def getProperties(include_schema=True):
		properties = {
			"user": Properties.user,
			"password": Properties.password,
			"host": Properties.host
		}
		if include_schema:
			properties["database"] = Properties.schema
		return properties