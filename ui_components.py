from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QGroupBox,
    QComboBox, QLabel, QLineEdit, QProgressBar, QTextEdit, QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal


class TabsWidget(QWidget):
    def __init__(self, table_dict=None, dfs=None, parent=None):
        super().__init__(parent)
        main_layout = QHBoxLayout()
        self.tabs = QTabWidget(self)
        self.tabs.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)
        self.seen_tables: list[str] = []

        if table_dict and dfs:
            self.update_tabs(table_dict, dfs)

    def fill_table_from_dataframe(self, table_widget, df):
        if df is None or df.empty:
            return
        table_widget.setRowCount(df.shape[0])
        table_widget.setColumnCount(df.shape[1])
        table_widget.setHorizontalHeaderLabels([str(col) for col in df.columns])
        table_widget.setVerticalHeaderLabels([str(idx + 1) for idx in range(df.shape[0])])
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iat[row, col]))
                table_widget.setItem(row, col, item)

    def add_tab(self, name, row, col, df):
        tab = QWidget()
        layout = QVBoxLayout()
        table = QTableWidget(row, col)
        table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(table)
        tab.setLayout(layout)
        self.tabs.addTab(tab, name)
        self.tabs.updateGeometry()
        self.tabs.repaint()
        self.fill_table_from_dataframe(table, df)

    def update_tabs(self, table_dict, dfs):
        for table, (row, col) in table_dict.items():
            if table not in self.seen_tables:
                df = dfs.get(table, None)
                self.add_tab(table, row, col, df)
                self.seen_tables.append(table)



def create_main_window(parent_window):
    central_widget = QWidget()
    main_layout = QVBoxLayout(central_widget)



    # Search Block

    upper_group = QGroupBox()
    upper_layout = QVBoxLayout(upper_group)

    theme_layout = QHBoxLayout()
    dir_layout = QHBoxLayout()

    parent_window.title_label = QLabel("Text Search")
    parent_window.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    parent_window.search_line = QLineEdit()
    parent_window.search_line.setPlaceholderText("Enter key words")
    parent_window.find_btn = QPushButton("Find")
    parent_window.find_btn.setObjectName("chg_theme")
    parent_window.find_btn.clicked.connect(parent_window.finddb)
    parent_window.theme_btn = QPushButton("White")
    parent_window.theme_btn.setObjectName("chg_theme")
    parent_window.theme_btn.clicked.connect(parent_window.changetheme)
    parent_window.dir_line = QLineEdit()
    parent_window.dir_line.setPlaceholderText("Directory")
    parent_window.dir_line.setReadOnly(True)
    parent_window.dir_dlt = QPushButton(" X ")
    parent_window.dir_dlt.clicked.connect(parent_window.browseclear)
    parent_window.dir_dlt.setObjectName("dir_dlt")
    parent_window.add_text = QPushButton("Browse File")
    parent_window.add_text.clicked.connect(parent_window.browsedir)
    parent_window.start_search = QPushButton("Search")
    parent_window.start_search.clicked.connect(parent_window.start_check)

    upper_layout.addWidget(parent_window.title_label)
    theme_layout.addWidget(parent_window.search_line)
    theme_layout.addWidget(parent_window.find_btn)
    theme_layout.addWidget(parent_window.theme_btn)
    upper_layout.addLayout(theme_layout)
    dir_layout.addWidget(parent_window.dir_line)
    dir_layout.addWidget(parent_window.dir_dlt)
    upper_layout.addLayout(dir_layout)
    upper_layout.addWidget(parent_window.add_text)
    upper_layout.addWidget(parent_window.start_search)

    main_layout.addWidget(upper_group)

    # Result Block

    bottom_group = QGroupBox()
    bottom_layout = QHBoxLayout(bottom_group)

    parent_window.result = TabsWidget()
    parent_window.result.setMinimumHeight(550)
    parent_window.result.setMinimumWidth(1000)

    bottom_layout.addWidget(parent_window.result)

    main_layout.addWidget(bottom_group)

    return central_widget

