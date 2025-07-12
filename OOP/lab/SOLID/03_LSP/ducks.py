from abc import abstractmethod, ABC


class SquizableToy(ABC):
    @staticmethod
    @abstractmethod
    def make_sound(self):
        pass


class Duck(ABC):

    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck(SquizableToy):
    @staticmethod
    def make_sound(self):
        return "Squeek"


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == self.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
