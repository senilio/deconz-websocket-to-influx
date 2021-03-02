FROM python:3
ADD websocket.py /
RUN pip install influxdb websockets
CMD ["python", "-u", "websocket.py"]
