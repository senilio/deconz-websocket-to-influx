# deconz-websocket-to-influx
This script listens to deCONZ websocket stream. If it finds a sensor with the "whitelisted" attributes, it pushes the value to InfluxDB. Once we have the value in InfluxDB, we can easily display the sensors in Grafana.

I prefer this over periodic Prometheus polling, since different sensors report values in different intervals. For instance, it makes no sense to poll the deCONZ API every minute for temperature sensor values that updates every 15 minutes. Just as it makes no sense to poll every minute for power reading that updates every 5 seconds. With this method, DB writes are triggered by websocket events, and we only get what we need into the DB.


## Install

Clone the repo

Edit the environment variables in docker-compose.yml

`docker build -t deconz-websocket-to-influx .` 

Launch the thing with `docker-compose up -d` 
