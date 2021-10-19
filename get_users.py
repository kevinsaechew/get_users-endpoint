from flask import Flask
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

users_data = './users.csv'

class Users(Resource):
    def get(self):
        user_data = pd.read_csv(users_data).to_dict()
        return {'data': user_data}, 200

api.add_resource(Users, '/users')

if __name__ == "__main__":
    app.run()



