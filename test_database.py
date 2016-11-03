import unittest
from app.db import database, cursor

class TestDatabase(unittest.TestCase):

	def test_database_size(self):
		sql_command = "SELECT * FROM Stops"
		cursor.execute(sql_command)
		row = cursor.fetchall()
		self.assertEqual(len(row), 2497)

	def test_retrival(self):
		sql_command = "SELECT * FROM Stops WHERE StopId = '150DOD:5'"
		cursor.execute(sql_command)
		row = cursor.fetchall();
		self.assertEqual(len(row), 1)
		self.assertEqual(row[0][0], '150DOD:5')
		self.assertEqual(row[0][1], 'MTD2634')


if __name__ == '__main__':
	unittest.main()
