import sys
from PySide6.QtWidgets import QApplication
from src.depo.window import MainWindow


if __name__ == '__main__':
    qApp = QApplication(sys.argv[1:])
    window = MainWindow(qApp)
    window.show()
    sys.exit(qApp.exec())
