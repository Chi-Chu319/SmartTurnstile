from server_visitor import visitorAPI
from server_admin import adminAPI
from server_iot import iotAPI
from flask import Flask



app = Flask(__name__)
# the secret key encrypts the session data 
app.secret_key = "Key"

# TODO add the index route

app.register_blueprint(visitorAPI)
app.register_blueprint(adminAPI)
app.register_blueprint(iotAPI)


if __name__ == "__main__":
	app.run(debug=True, host= '0.0.0.0')
