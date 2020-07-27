import threading

from src.Event import Event
from src.StatisticsManager import StatisticsManager
from src.consumer.Consumer import Consumer
from src.httpserver.server import start_server

if __name__ == '__main__':
    statistics_manager = StatisticsManager()
    threading.Thread(target=start_server, args=(statistics_manager,)).start()
    consumer = Consumer()
    consumer.start()
    while True:
        event_json = consumer.get_event_from_consumer()
        event = Event(event_json)
        statistics_manager.add_to_statistics(event)