from flask import Flask
# from flask_jwt import JWT
from flask_restful import Api
from flask_cors import CORS

from evaluation.array_diff import ArrayDiff

# from evaluation.security import authenticate, identity

app = Flask(__name__)

# TODO configure cors for security in production
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# TODO move key to private data configuration at deployment
app.secret_key = 'taz'
api = Api(app)


# jwt = JWT(app, authenticate, identity)


api.add_resource(ArrayDiff, "/array-diff")


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
