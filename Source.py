from abc import ABC, abstractmethod
import pandas as pd
from ConnectObject import ConnectObject


class Source(ABC):
    _path: str
    _filename: str
    _sheetname: str
    _con: ConnectObject
    _sqlQuery: str
    dataframe: pd.DataFrame

    # constructor for files
    def __init__(self, path: str, filename: str, sheetname: str):
        self._path = path
        self._filename = filename
        self._sheetname = sheetname
        self.dataframe = self.loadFile()

    # constructor for sql
    def __int__(self, con: ConnectObject, sqlQuery: str) -> pd.DataFrame:
        ...

    def loadFile(self) -> pd.DataFrame:
        self.dataframe = self.read()
        df = self.validation(self.dataframe)
        return df

    @abstractmethod
    def read(self) -> pd.DataFrame: # loic for read frame
        ...

    @abstractmethod
    def validation(self, df: pd.DataFrame) -> pd.DataFrame:# Some logic for validation frame
        ...
