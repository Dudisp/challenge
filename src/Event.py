import json

EVENT_TYPE = "event_type"
DATA = "data"
TIMESTAMP = "timestamp"


class Event:
    def __init__(self, event_json: json):
        self.type = event_json[EVENT_TYPE]
        self.data = event_json[DATA]
        self.timestamp = event_json[TIMESTAMP]
