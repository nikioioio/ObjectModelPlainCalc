from abc import ABC, abstractmethod


class ConnectObject(ABC):

    _driver: object
    _host: str
    _port: str
    _dbName: str
    _user: str
    _password: str

    def __int__(self, driver: object, host: str, port: str, dbName: str, user: str, password:str ):

        self._driver = driver
        self._host = host
        self._port = port
        self._dbName = dbName
        self._user = user
        self._password

    @abstractmethod
    def getConn(self) -> object:
        ...


