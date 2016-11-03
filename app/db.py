import mysql.connector as connector
'''
	Backend database connector
'''

database = connector.connect(user='root',
        password='fht940826',
        database='bus_tracker')

cursor = database.cursor()