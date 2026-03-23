from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def stop_work(self):
        pass
