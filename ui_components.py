from random import paretovariate

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QGroupBox,
    QComboBox, QLabel, QLineEdit, QProgressBar, QTextEdit, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal

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

    parent_window.result = QLineEdit()
    parent_window.result.setReadOnly(True)
    parent_window.result.setMinimumHeight(550)
    parent_window.result.setMinimumWidth(1000)

    bottom_layout.addWidget(parent_window.result)

    main_layout.addWidget(bottom_group)

    return central_widget

