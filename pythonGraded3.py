import configparser
import json
from flask import Flask, jsonify

## Third question : automating configuration management tasks is essential for maintaining consistency and 
## managing infrastructure efficiently

# Read the configuration file

#After running below file GO TO - http://localhost:5000/get_config

def read_config(filename):
    config = configparser.ConfigParser()
    try:
        config.read(filename)
    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return None
    return config

# Convert the configuration to a dictionary
def config_to_dict(config):
    config_dict = {}
    for section in config.sections():
        config_dict[section] = dict(config[section])
    return config_dict

# Create a Flask web service
app = Flask(__name__)

@app.route('/get_config', methods=['GET'])
def get_config():
    config = read_config('config.ini')
    if config:
        config_dict = config_to_dict(config)
        return jsonify(config_dict)

if __name__ == "__main__":
    app.run(debug=True)
