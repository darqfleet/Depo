import sys
import pathlib
from PySide6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QHBoxLayout,
                               QLabel, QMainWindow, QToolBar, QSplitter,
                               QPushButton, QComboBox, QStackedWidget,
                               QSizePolicy, QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QAction, QIcon, QFont, QRawFont



class Filler(QWidget):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_main = QVBoxLayout()
        layout_main.addWidget(label)
        self.setLayout(layout_main)


class SplitWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_window()



    def setup_window(self):
        self.bt_maximize_pane = QPushButton('M')
        self.bt_maximize_pane.setFixedSize(20,20)
        self.bt_maximize_pane.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.bt_options = QPushButton('^')
        self.bt_options.setFixedSize(20,20)
        self.bt_options.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.top_frame = QFrame()
        self.top_frame.setObjectName('top')# = QFrame()





        self.bt_split_hor = QPushButton('SplitH')
        self.bt_split_hor.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
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
        # layout_top.setObjectName('top')
        layout_top.setContentsMargins(0,0,0,0)
        layout_top.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout_top.addWidget(self.bt_maximize_pane, 0, alignment=Qt.AlignmentFlag.AlignRight)
        layout_top.addWidget(self.bt_options, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.top_frame.setLayout(layout_top)


        # layout_top.addWidget(self.cmb_select)

        self.layout_split = QVBoxLayout()
        self.layout_split.addWidget(self.stacked)
        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(0,0,0,0)
        layout_main.addWidget(self.top_frame)
        # layout_main.addLayout(layout_top)
        layout_main.addLayout(self.layout_split)
        self.cmb_select.currentIndexChanged.connect(self.set_widget)

        container = QWidget()
        container.setLayout(layout_main)

        self.splitter = QSplitter()
        self.splitter.addWidget(container)
        self.setCentralWidget(self.splitter)

    def split_horizontal(self):
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.addWidget(SplitWindow())

    def split_vertical(self):
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(SplitWindow())

    def set_widget(self):
        index = self.cmb_select.currentIndex()
        self.stacked.setCurrentIndex(index)


if __name__ == '__main__':
    qApp = QApplication()
    w = SplitWindow()
    w.show()
    sys.exit(qApp.exec())