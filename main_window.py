from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from ui_components import create_main_window

from config import STYLESHEET_WHITE, STYLESHEET_DARK

from worker import StartWorker
from my_SQL import table_list

import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Search")
        self.setGeometry(100, 100, 1200, 800)

        main_widget = create_main_window(self)
        self.setCentralWidget(main_widget)

        self.Tlist = table_list
        if self.Tlist:
            self.add_tabs(self.Tlist)

        self.style = STYLESHEET_WHITE

        self.setStyleSheet(self.style)

    def add_tabs(self, Tlist):
        self.result.update_tabs(Tlist)
    def start_check(self):
        errors = []
        file_dir = self.dir_line.text().strip()
        if not file_dir:
            errors.append("Choose file before start.")

        if errors:
            QMessageBox.warning(self, "Error", "\n".join(errors))
            return


        ext = os.path.splitext(file_dir)[1]
        basename = os.path.basename(file_dir)
        self.start_worker(file_dir, ext, basename)

    def start_worker(self, directory, ext, basename):
        if directory and ext:
            self.start_search.setEnabled(False)

            self.thread = QThread(self)
            self.worker = StartWorker(directory, ext, basename)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.on_finished)
            self.worker.error.connect(self.on_error)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.finished.connect(self.thread.quit)
            self.thread.start()

    def on_finished(self):
        self.start_search.setEnabled(True)
        QMessageBox.information(self, "Success", "File Uploaded Successfully.")

    def on_error(self, error):
        print(error)

    def finddb(self):
        if not self.search_line.text():
            QMessageBox.warning(self, "Error", "Enter keys before find information.")

    def changetheme(self):
        if self.style == STYLESHEET_WHITE:
            self.style = STYLESHEET_DARK
            self.theme_btn.setText("Dark")
            self.setStyleSheet(self.style)
        else:
            self.style = STYLESHEET_WHITE
            self.theme_btn.setText("White")
            self.setStyleSheet(self.style)

        QMessageBox.information(self, "Success", "Theme Changed.")

    def browseclear(self):
        directory = self.dir_line.text().strip()
        if directory:
            self.dir_line.clear()
            QMessageBox.information(self, "Success", "File Removed.")
        else:
            QMessageBox.warning(self, "Warning", "File Already Removed.")

    def browsedir(self):
        file_dir, _ = QFileDialog.getOpenFileName(self, "Choose File", "", "csv file (*.csv);; excel file (*.xls *.xlsx *.xlsm *.xlsb);; json file (*.json)")
        if file_dir:
            self.dir_line.setText(file_dir)
            QMessageBox.information(self, "Success", "File Added.")