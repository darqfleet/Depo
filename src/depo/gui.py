import pathlib
import sys

from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QToolBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QAction, QIcon

icon_path = pathlib.Path(__file__).parent.parent.parent / 'icons'

class Filler(QWidget):
    def __init__(self, icon='nuke.svg', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = icon
        self.init_ui()
    def init_ui(self):
        self.set_window_widgets()
    def set_window_widgets(self):
        label = QLabel()
        logo_pix = QPixmap(f'{icon_path}/{self.icon}')
        label.setPixmap(logo_pix)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_main = QVBoxLayout()
        layout_main.addWidget(label)
        # self.setLayout(layout_main)


class Window(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Test Slice')
        self.setup_window()
        self.setCentralWidget(Filler())


    def setup_window(self):
        self.act_split = QAction(icon=QIcon(f'{icon_path}/nuke.svg'),iconText='Split')
        self.act_split.triggered.connect(self.split_window)
        self.toolbar = QToolBar()
        self.toolbar.addAction(self.act_split)
        self.addToolBar(self.toolbar)
    def split_window(self):
        self.parent.main_layout.addWidget(Window(self.parent))
        print('split')

class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wgt = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(Window(self))
        self.wgt.setLayout(self.main_layout)
        self.setCentralWidget(self.wgt)


if __name__ == '__main__':
    qapp = QApplication(sys.argv[:1])
    window = MainAppWindow()
    window.show()
    sys.exit(qapp.exec())
