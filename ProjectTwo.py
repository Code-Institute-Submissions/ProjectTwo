from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB setup
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorUSA'
COLLECTION_NAME = 'projects'

# Flask Home page.
@app.route('/')
def home():
    return render_template('home.html')

# Flask About page.
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/issues')
def issues():
    return render_template('issues.html')

# Flask Education page.
@app.route('/education')
def education():
    return render_template('education.html')

# Flask view to serve projects data from MongoDB in JSON format.
@app.route('/donorUSA/projects')
def donor_projects():
    # A constant that defines the record fields that we wish to retrieve.
    FIELDS = {
        '_id': False, 'funding_status': True, 'school_state': True,
        'resource_type': True, 'poverty_level': True,
        'date_posted': True, 'total_donations': True
    }

    # Open a connection to MongoDB using a with statement such that the
    # connection will be closed as soon as we exit the with statement
    with MongoClient(MONGODB_HOST, MONGODB_PORT) as conn:
        # Define which collection we wish to access
        collection = conn[DBS_NAME][COLLECTION_NAME]
        # Retrieve a result set only with the fields defined in FIELDS
        # and limit the the results to 55000
        projects = collection.find(projection=FIELDS, limit=55000)
        # Convert projects to a list in a JSON object and return the JSON data
        return json.dumps(list(projects))

# Flask Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
