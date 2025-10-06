import sys
import pathlib
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QToolBar, QSplitter, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QAction, QIcon


class Filler(QWidget):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_main = QVBoxLayout()
        layout_main.addWidget(label)
        self.setLayout(layout_main)


class Window(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.setup_window()


    def setup_window(self):
        self.bt_split_hor = QPushButton('SplitH')
        self.bt_split_hor.clicked.connect(self.split_horizontal)
        self.bt_split_ver = QPushButton('SplitV')
        self.bt_split_ver.clicked.connect(self.split_vertical)
        self.cmb_select = QComboBox()


        items = [f'Some widget {x}' for x in range(5)]
        self.wgts = [Filler(x) for x in items]
        self.cmb_select.addItems(items)
        self.stacked = QStackedWidget()
        [self.stacked.addWidget(x) for x in self.wgts]


        layout_top = QHBoxLayout()
        layout_top.addWidget(self.bt_split_hor)
        layout_top.addWidget(self.bt_split_ver)
        layout_top.addWidget(self.cmb_select)

        self.layout_split = QVBoxLayout()
        self.layout_split.addWidget(self.stacked)
        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_top)
        layout_main.addLayout(self.layout_split)
        self.cmb_select.currentIndexChanged.connect(self.set_widget)

        container = QWidget()
        container.setLayout(layout_main)

        self.splitter = QSplitter()
        self.splitter.addWidget(container)
        self.setCentralWidget(self.splitter)

    def split_horizontal(self):
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.addWidget(Window())

    def split_vertical(self):
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(Window())

    def set_widget(self):
        index = self.cmb_select.currentIndex()
        self.stacked.setCurrentIndex(index)

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
