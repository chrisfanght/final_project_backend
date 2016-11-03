from flask import Flask, request
from oauth2client import client, crypt
from db import database, cursor

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"

@app.route("/signin", methods=["POST"])
def signin():
	if request.method == "POST":
		google_token = request.json["token"]
		'''
			Check if the google token is valid using Google Oauth2 Client
		'''
		try:
			idinfo = client.verify_id_token(token, CLIENT_ID)
			if idinfo['aud'] not in [ANDROID_CLIENT_ID, IOS_CLIENT_ID, WEB_CLIENT_ID]:
				raise crypt.AppIdentityError("Unrecognized client.")
			if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
				raise crypt.AppIdentityError("Wrong issuer.")
			if idinfo['hd'] != APPS_DOMAIN_NAME:
				raise crypt.AppIdentityError("Wrong hosted domain.")
		except crypt.AppIdentityError:
			return "Invalid token"

		'''
			Check if the user token is already in the database
			If not, create a new user
		'''
		sql_query = "SELECT * FROM Users WHERE GoogleIdToken='%s'" % google_token
		cursor.execute(sql_query)
		if cursor.rowcount == 0:
			sql_query = "INSERT INTO Users(GoogleIdToken) values('%s')" % google_token
			cursor.execute(sql_query)
			database.commit()
		return "Success"

if __name__ == "__main__":
  app.run(host="0.0.0.0")
