import json
import os
import queue
import subprocess
import threading

from src.consumer.Validator import Validator

GENERATOR_FILENAME = "generator-windows-amd64.exe"


class Consumer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.json_events_queue = queue.Queue()

    def run(self):
        directory = os.path.dirname(__file__)
        p = subprocess.Popen([directory + "\\" + GENERATOR_FILENAME, ""], stdout=subprocess.PIPE)

        while True:
            json_line = p.stdout.readline()
            j = Validator.validate_line_as_json(json_line)
            if j is not None:
                self.json_events_queue.put(j)
            print(f"put() qsize: {self.json_events_queue.qsize()}")

    def get_event_from_consumer(self) -> json:
        print(f"get() qsize: {self.json_events_queue.qsize()}")
        return self.json_events_queue.get()
