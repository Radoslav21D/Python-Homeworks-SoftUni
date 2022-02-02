from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.min_speed_limit = int
        self.max_speed_limit = int
        self.is_taken = False
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if len(self.model) < 4:
            raise ValueError(f"Model {self.model} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if self.min_speed_limit > self.max_speed_limit or self.max_speed_limit < self.min_speed_limit:
            raise ValueError(f"Invalid speed limit! Must be between {self.min_speed_limit} and {self.max_speed_limit}!")
        self.__speed_limit = value




