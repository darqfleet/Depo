import sys

from PySide6.QtWidgets import QWidget, QApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('Test Slice')
        self.show()

if __name__ == '__main__':
    qapp = QApplication(sys.argv[:1])
    window = Window()
    sys.exit(qapp.exec())