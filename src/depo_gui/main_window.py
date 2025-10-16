import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QStatusBar
from PySide6.QtGui import QAction, QFontDatabase, QFont
from theme import style, apply_schema, schema


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Depo')
        self.setGeometry(250, 250, 1000, 500)
        self.setObjectName('main')
        self.setStatusBar(QStatusBar())
        self.create_actions()
        self.create_menu()
        self.bind_actions()

    def create_actions(self):
        self.act_quit = QAction('Qiut')
        self.act_quit.setShortcut('Ctrl+q')
        self.act_quit.setStatusTip('Exit from Depo')
        self.act_quit.triggered.connect(self.quit)
        self.act_test = QAction('Test')
        self.act_test.setShortcut('Test test')
        self.act_test.setStatusTip('Proste testowanie')

    def create_menu(self):
        self.menu_depo = self.menuBar().addMenu('Depo')
        self.menu_view = self.menuBar().addMenu('View')
        self.menu_settings = self.menuBar().addMenu('Settings')

    def bind_actions(self):
        self.menu_depo.addAction(self.act_quit)
        self.menu_view.addAction(self.act_test)

    def quit(self):
        self.close()


if __name__ == '__main__':
    qapp = QApplication()
    id = QFontDatabase().addApplicationFont(
        '/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/config/fonts/JetBrainsMonoNL-Bold.ttf')
    families = QFontDatabase.applicationFontFamilies(id)

    style = apply_schema(schema, style)

    qapp.setStyleSheet(style)
    qapp.setFont(QFont(families[0], 10))
    window = MainWindow()
    window.show()
    sys.exit(qapp.exec())
