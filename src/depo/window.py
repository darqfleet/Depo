import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QStatusBar, QToolBar, QComboBox
from PySide6.QtGui import QAction, QFontDatabase, QFont
from PySide6.QtCore import Qt, QSize
from src.depo.colorschema import ColorSchema
from src.depo.config import Config
from src.depo import CONFIG_PATH


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_application = app
        self.color_schema = ColorSchema(self.main_application)
        self.init_ui()

    def init_ui(self):
        self.color_schema.apply()
        self.setWindowTitle('Depo')
        self.setGeometry(250, 250, 1000, 500)
        self.setObjectName('main')
        self.setStatusBar(QStatusBar())
        self.create_toolbar()
        self.create_actions()
        self.create_menu()
        self.bind_actions()


    def create_actions(self):
        self.act_quit = QAction('Quit')
        self.act_quit.setShortcut('Ctrl+q')
        self.act_quit.setStatusTip('Exit from Depo')
        self.act_quit.triggered.connect(self.quit)
        self.act_theme = QAction('Theme')
        self.act_theme.setStatusTip('Color Schemas')
        self.act_theme.setShortcut('Ctrl+t')
        self.act_theme.triggered.connect(self.settings_theme)
        self.act_test = QAction('Test')
        self.act_test.setShortcut('Test test')
        self.act_test.setStatusTip('Proste testowanie')
        self.act_toolbar_toggle = self.toolbar.toggleViewAction()
        self.act_toolbar_toggle.setText('Toolbar')
        self.act_toolbar_toggle.setStatusTip('Enable or Disable main toolbar')

    def create_toolbar(self):
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        self.toolbar.setOrientation(Qt.Orientation.Horizontal)
        self.toolbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea)
        self.toolbar.setFloatable(False)
        self.toolbar.setIconSize(QSize(32, 32))
        cmb_box = QComboBox()
        cmb_box.addItems(['sdad', 'asdad'])
        # self.toolbar.addWidget(cmb_box)

    def create_menu(self):
        self.menu_depo = self.menuBar().addMenu('Depo')
        self.menu_depo.setStatusTip('Main menu for opening depo projects')
        self.menu_view = self.menuBar().addMenu('View')
        self.menu_settings = self.menuBar().addMenu('Settings')

    def bind_actions(self):
        self.menu_depo.addAction(self.act_quit)
        self.menu_view.addAction(self.act_toolbar_toggle)
        self.menu_settings.addAction(self.act_theme)

    def quit(self):
        self.close()

    def settings_theme(self):
        self.color_schema.show()
