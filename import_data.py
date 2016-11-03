from app.db import database, cursor
import json
'''
	Parse stop data and import data into mysql database
'''

with open("data.json") as data_file:
	data = json.load(data_file)

for stops in data["stops"]:
	for stop in stops["stop_points"]:
		sql_query = "INSERT INTO Stops values('%s', '%s', '%s', %f, %f)" % (stop["stop_id"], 
			stop["code"], stop["stop_name"], stop["stop_lat"], stop["stop_lon"])
		cursor.execute(sql_query)
		database.commit()