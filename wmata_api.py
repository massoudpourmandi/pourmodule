import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = <YOUR_API_KEY_HERE>
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
  # create an empty list called 'incidents'

  # use 'requests' to do a GET request to the WMATA Incidents API
  # retrieve the JSON from the response

  # iterate through the JSON response and retrieve all incidents matching 'unit_type'
  # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
  #   -StationCode, StationName, UnitType, UnitName
  # add each incident dictionary object to the 'incidents' list

  # return the list of incident dictionaries using json.dumps()

if __name__ == '__main__':
    app.run(debug=True)
