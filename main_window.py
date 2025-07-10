from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QListWidgetItem

from ui_components import create_main_window
from config import STYLESHEET_WHITE, STYLESHEET_DARK

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Search")
        self.setGeometry(100, 100, 1200, 800)

        main_widget = create_main_window(self)
        self.setCentralWidget(main_widget)


        self.style = STYLESHEET_WHITE

        self.setStyleSheet(self.style)

    def start_check(self):
        errors = []
        file_dir = self.search_line.text().strip()
        if not file_dir:
            errors.append("Choose file before start.")

        if errors:
            QMessageBox.warning(self, "Error", "\n".join(errors))
            return


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
        file_dir, _ = QFileDialog.getOpenFileName(self, "Choose File", "", "All Files (*)")
        if file_dir:
            self.dir_line.setText(file_dir)
            QMessageBox.information(self, "Success", "File Added.")