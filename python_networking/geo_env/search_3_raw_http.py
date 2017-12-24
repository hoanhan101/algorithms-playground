#!/usr/bin/env python3
# Making a Raw HTTP Connection to Google Maps

import http.client
import json
from urllib.parse import quote_plus
base = '/maps/api/geocode/json'

def geocode(address):
    # Construct a path
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    
    # Make a connection to Google map
    connection = http.client.HTTPConnection('maps.google.com')
    
    # Issue a GET request
    connection.request('GET', path)

    # Read the raw reply from the connection
    rawreply = connection.getresponse().read()

    # Convert to JSON
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
