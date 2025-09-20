from flask import Flask
from flask_restful import Api
from models import db  
from controller import LibraryResource, LibraryListResource

app = Flask(__name__)
api = Api(app)

# DB Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db.init_app(app)

# Create tables once when the app starts
@app.before_request
def create_tables():
    db.create_all()

# Library routes
api.add_resource(LibraryListResource, '/api/library')
api.add_resource(LibraryResource, '/api/library/<string:isbn>')

if __name__ == "__main__":
    app.run(debug=True)
