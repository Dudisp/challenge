from collections import defaultdict
from typing import Dict

from src.Event import Event


class StatisticsManager:
    def __init__(self):
        self.types_to_counter = defaultdict(lambda: 0)
        self.data_words_to_counter = defaultdict(lambda: 0)
        
    def add_to_statistics(self, event: Event):
        self.add_to_dict(dictionary=self.types_to_counter, key=event.type)
        self.add_to_data_words_dict(event.data)

    def add_to_data_words_dict(self, data: str):
        words_array = data.split()
        for word in words_array:
            self.add_to_dict(dictionary=self.data_words_to_counter, key=word)

    def add_to_dict(self, dictionary: Dict[str, int], key: str):
        dictionary[key] = dictionary[key] + 1

