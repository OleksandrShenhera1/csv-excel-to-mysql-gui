
import pandas as pd
from PyQt6.QtCore import pyqtSignal, QObject
from my_SQL import pushToSql, readDf

class StartWorker(QObject):
    finished = pyqtSignal(dict, dict)
    error = pyqtSignal(str)
    def __init__(self, directory, ext, basename):
        super().__init__()
        self.directory = directory
        self.ext = ext
        self.basename = basename
    def run(self):
        try:
            if self.ext == '.csv':
                df = pd.read_csv(self.directory)

            elif self.ext == '.json':
                df = pd.read_json(self.directory)

            else:
                df = pd.read_xml(self.directory)


            res = pushToSql(df, self.basename)
            dfs = readDf(self.basename)
            info = {self.basename: res[self.basename]}
            dfs = {self.basename: df}
            self.finished.emit(info, dfs)
        except Exception as e:
            self.error.emit(str(e))

