import os
import json
import asyncio
import websockets
from datetime import datetime
from influxdb import InfluxDBClient

#################################################
# What state attributes are we interested in?
attributes = ["power", "temperature", "humidity"]
#################################################

# Write to DB
def push_to_influx(x):
    client.write([x],{'db':db_name}, 204, 'line')

# Filter and name websocket events
def verify(x):
    for attribute in attributes:
        try:
            payload = '%s %s=%i' % (x["id"], attribute, x["state"][attribute])
            print('%s - %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), payload))
            push_to_influx(payload)
        except KeyError:
            pass

# Websocket listener function
async def hello():
    async with websockets.connect(deconz_websocket_uri) as websocket:
        while 1:
            verify(json.loads(await websocket.recv()))

# First read environment variables provided by docker
db_name = os.environ['INFLUX_DB_NAME']
db_host = os.environ['INFLUX_DB_HOST']
db_port = os.environ['INFLUX_DB_PORT']
deconz_websocket_uri = os.environ['DECONZ_WEBSOCKET_URI']

# Initialize connection to Influx
client = InfluxDBClient(host=db_host, port=db_port, database=db_name)

# Kick off eternal websocket event listener
asyncio.get_event_loop().run_until_complete(hello())
