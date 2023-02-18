import abc
import json


class DataStore(abc.ABC):

    @staticmethod
    def readfromFile(filename) -> object:
        with open(filename, "r") as f:
            return json.loads(f.read())

    @staticmethod
    def writetoFile(data, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(data))

    @abc.abstractmethod
    def saveData(self):
        pass

    @abc.abstractmethod
    def readData(self):
        pass
