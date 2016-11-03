import unittest
from app.db import database, cursor

class DatabaseTestCase(unittest.TestCase):

	def test_cursor(self):
		sql_command = "Select * from Stops"
		cursor.execute(sql_command)
		assert cursor.rowcount == 2497