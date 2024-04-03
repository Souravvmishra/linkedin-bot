
# Import the Flask module
from flask import Flask, jsonify
from gemini import get_tweet
# Initialize the Flask application
app = Flask(__name__)

# Define a route for the application
@app.route('/', methods=['GET'])
# Define a function for the route
def home():
    return  get_tweet()

app.run(host='0.0.0.0')
