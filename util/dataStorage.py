import abc


class DataStore(abc.ABC):

    @abc.abstractmethod
    def saveData(self):
        pass

    @abc.abstractmethod
    def readData(self):
        pass
