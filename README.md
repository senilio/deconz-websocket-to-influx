# deconz-websocket-to-influx
Populate InfluxDB with sensor values from deCONZ. Uses websocket.

This script listens to deCONZ websocket events. If it finds one of the sensor attributes listed, it pushed the values to InfluxDB. Once we have the value in InfluxDB, we can easily display the sensors in Grafana.

I prefer this over periodic Prometheus polling, since different sensors report values in different intervals. For instance, it makes no sense to poll the deCONZ API every minute for temperature sensor values that updates every 15 minutes. Just as it makes no sense to poll every minute for power reading that updates every 5 seconds. This way, readings are triggered by websocket events as they are reported to the controller, and we only get what we need into the DB.


## Install

Clone the repo

Edit the environment variables in docker-compose.yml

Build the container

Launch the thing with `docker-compose up -d` 
