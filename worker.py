
import pandas as pd
from PyQt6.QtCore import pyqtSignal, QObject
from my_SQL import pushToSql


class StartWorker(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    def __init__(self, directory, ext, basename):
        super().__init__()
        self.directory = directory
        self.ext = ext
        self.basename = basename
    def run(self):
        try:
            if self.ext == '.csv':
                dfcsv = pd.read_csv(self.directory)
                pushToSql(dfcsv, self.basename)
            elif self.ext == '.json':
                dfjson = pd.read_json(self.directory)
                pushToSql(dfjson, self.basename)
            else:
                dfxml = pd.read_xml(self.directory)
                pushToSql(dfxml, self.basename)

            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

