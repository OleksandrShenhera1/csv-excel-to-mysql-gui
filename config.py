STYLESHEET_WHITE = """
QWidget {
        background-color: #D6D8DF;
        color: #363C4D;
        font-size: 18px;
        font-family: 'Monaco', 'Courier New', monospace;
    }
    QMainWindow {
        background-color: #E6E7ED;
    }
    QGroupBox {
        border: 2px solid #C1C2C7;
        border-radius: 8px;
        font-weight: bold;
    }
    QPushButton#chg_theme {
        font-size: 18px;
        background-color: #DADCE3;
        color: #363C4D;
        border: 2px solid #C6C7CC;
        border-radius: 5px;
        padding: 3px;
    }
    QPushButton#chg_theme:hover {
        background-color: #C3C5CC;
    }
    QPushButton#chg_theme:pressed {
        background-color: #BCBEC4;
    }
    QPushButton#dir_dlt {
        font-size: 18px;
        background-color: #DADCE3;
        color: #363C4D;
        border: 2px solid #C6C7CC;
        border-radius: 5px;
        padding: 3px;
    }
    QPushButton#dir_dlt:hover {
        background-color: #C3C5CC;
    }
    QPushButton#dir_dlt:pressed {
        background-color: #BCBEC4;
    }
    QPushButton {
        background-color: #DADCE3;
        color: #363C4D;
        border: 2px solid #C6C7CC;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #C3C5CC;
    }
    QPushButton:pressed {
        background-color: #BCBEC4;
    }
    QLineEdit {
        background-color: #DADCE3;
        border: 2px solid #C6C7CC;
        border-radius: 5px;
        padding: 3px;
    }
    QLabel {
        font-weight: bold;
    }
    QTabWidget {
        background-color: #DADCE3;
        border: 2px solid #C6C7CC;
        border-radius: 5px;
        padding: 3px;
    }
    QTabBar::tab:selected {
        border: 1px solid #C6C7CC;
        border-radius: 5px;
        font-weight: bold;
    }
    QScrollBar:vertical {
        border: 1px solid #C6C7CC;
        background: #e0e0e0;
        border-radius: 10px;
        width: 14px;
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:vertical {
        border: 2px solid #BCBEC4;
        background: #C6C7CC;
        border-radius: 10px;
        min-height: 20px;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        background: none;
        border: none;
        height: 0px;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;
        border: none;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
    QScrollBar:horizontal {
        border: 1px solid #C6C7CC;
        background: #e0e0e0;
        border-radius: 10px;
        height: 14px;
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:horizontal {
        border: 2px solid #BCBEC4;
        background: #C6C7CC;
        border-radius: 10px;
        min-width: 20px;
    }
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        background: none;
        border: none;
        width: 0px;
    }
    QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
        background: none;
        border: none;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background: none;
    }
"""

STYLESHEET_DARK = """
QWidget {
        background-color: #1F2335;
        color: #738997;
        font-size: 18px;
        font-family: 'Monaco', 'Courier New', monospace;
    }
    QMainWindow {
        background-color: #1F2335;
    }
    QGroupBox {
        border: 2px solid #1C202F;
        border-radius: 8px;
        font-weight: bold;
    }
    QPushButton#chg_theme {
        font-size: 18px;
        background-color: #24283B;
        color: #738997;
        border: 2px solid #1C202F;
        border-radius: 5px;
        padding: 3px;
    }
    QPushButton#chg_theme:hover {
        background-color: #41496B;
    }
    QPushButton#chg_theme:pressed {
        background-color: #373F5B;
    }
    QPushButton#dir_dlt {
        font-size: 18px;
        background-color: #24283B;
        color: #738997;
        border: 2px solid #1C202F;
        border-radius: 5px;
        padding: 3px;
    }
    QPushButton#dir_dlt:hover {
        background-color: #41496B;
    }
    QPushButton#dir_dlt:pressed {
        background-color: #373F5B;
    }
    QPushButton {
        background-color: #24283B;
        color: #738997;
        border: 2px solid #1C202F;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #41496B;
    }
    QPushButton:pressed {
        background-color: #373F5B;
    }
    QLineEdit {
        background-color: #24283B;
        border: 2px solid #1C202F;
        border-radius: 5px;
        padding: 3px;
    }
    QLabel {
        font-weight: bold;
    }
    QTabWidget {
        background-color: #24283B;
        border: 2px solid #1C202F;
        border-radius: 5px;
        padding: 3px;
    }
    QTabBar::tab:selected {
        border: 1px solid #1C202F;
        border-radius: 5px;
        font-weight: bold;
    }
    QScrollBar:vertical {
        border: 1px solid #202334;
        background: #232538;
        border-radius: 8px;
        width: 14px;
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:vertical {
        background: #363a4e;
        border: 1px solid #34374d;
        min-height: 24px;
        border-radius: 8px;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        background: #202334;
        border: none;
        height: 0px;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;
        border: none;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
        QScrollBar:horizontal {
        border: 1px solid #202334;
        background: #232538;
        border-radius: 8px;
        height: 14px;
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:horizontal {
        background: #363a4e;
        border: 1px solid #34374d;
        min-width: 24px;
        border-radius: 8px;
    }
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        background: #202334;
        border: none;
        width: 0px;
    }
    QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
        background: none;
        border: none;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background: none;
    }
"""