import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase, QFont
from src.depo.main_window import MainWindow

if __name__ == '__main__':
    qapp = QApplication(sys.argv[1:])
    window = MainWindow(qapp)
    window.show()
    sys.exit(qapp.exec())