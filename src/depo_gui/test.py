from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QFont, QFontDatabase
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.setWindowTitle("CodersLegacy")
        self.setContentsMargins(20, 20, 20, 20)
        id = QFontDatabase.addApplicationFont("/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/config/fonts/JetBrainsMonoNL-Bold.ttf")
        id = QFontDatabase.addApplicationFont("/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/config/fonts/JetBrainsMonoNL-Medium.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)
        print(families)

        label = QLabel("Hello World", self)
        label.setFont(QFont(families[0], 80))
        label.move(50, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())