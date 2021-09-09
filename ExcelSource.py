import pandas as pd
from Source import Source

class ExcelSource(Source):

    __fileExtension: str = '.xlsx'

    def read(self) ->  pd.DataFrame:
        return pd.read_excel(self._path+'/'+self._filename+self.__fileExtension, sheet_name=self._sheetname)

    def validation(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.dataframe


# exc = ExcelSource('C://Users//Кедрун Никита//PycharmProjects//akz_//input','УКПФ','Выпуск ГП')
#
# print(exc.loadFile())

        