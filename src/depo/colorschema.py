import os
from typing import List
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QApplication, QListWidget, QListWidgetItem, \
    QPushButton
from PySide6.QtGui import QFontDatabase, QFont

from src.depo import CONFIG_PATH
from src.depo.stylesheet import template
from src.depo.config import Config


class ColorSchemaPreview(QWidget):
    def __init__(self, ):
        super().__init__()
        self.colors: List[QLabel] = []
        self.layout_main = QVBoxLayout()
        self.setMinimumWidth(250)
        self.init_ui()

    def init_ui(self):
        for i in range(16):
            label = QLabel()
            label.setStyleSheet(f'background-color: white')
            self.colors.append(label)
            self.layout_main.addWidget(label)
        self.setLayout(self.layout_main)

    def configure(self, data):
        count = 0
        for k, v in data.items():
            if k.startswith('base'):
                self.colors[count].setStyleSheet(f'background-color: #{v}')
                count += 1


class ColorSchema(QWidget):
    def __init__(self, app: QApplication, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_application = app
        self.config = Config(CONFIG_PATH / 'theme')
        self.schema_list = self.config.all_configs
        self.schema = {}
        self.stylesheet_template = template
        self.stylesheet: str
        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True)
        self.list_widget.itemClicked.connect(self.item_clicked)
        self.color_preview_widget = ColorSchemaPreview()
        self.btn_apply = QPushButton('Apply')
        self.btn_apply.clicked.connect(self.apply)
        self.btn_cancel = QPushButton('Cancel')
        self.btn_cancel.clicked.connect(self.close)
        self.layout_main = QVBoxLayout()
        self.layout_buttons = QHBoxLayout()
        self.layout_item_and_preview = QHBoxLayout()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Color Schema Settings')
        self.layout_main = QVBoxLayout()
        self.layout_item_and_preview.addWidget(self.list_widget)
        self.layout_item_and_preview.addWidget(self.color_preview_widget)
        self.layout_buttons.addWidget(self.btn_cancel)
        self.layout_buttons.addWidget(self.btn_apply)
        self.layout_main.addLayout(self.layout_item_and_preview)
        self.layout_main.addLayout(self.layout_buttons)
        self.item_setup()
        self.current_schema()
        self.setLayout(self.layout_main)

    def item_setup(self):
        for i in self.schema_list:
            item = QListWidgetItem()
            item.setText(i)
            self.list_widget.addItem(item)

    def item_clicked(self, item: QListWidgetItem):
        self.set_schema(item.text())

    def current_schema(self):
        name = os.environ.get('DEPO_THEME')
        self.set_schema(name)

    def set_schema(self, name: str):
        config_path = self.config.get_one(name)
        schema = self.config.config_data(config_path)
        self.schema = schema
        self.color_preview_widget.configure(self.schema)

    def apply(self):
        self.apply_stylesheet_schema()
        self.main_application.setStyleSheet(self.stylesheet)
        self.set_font()

    def apply_stylesheet_schema(self):
        template = self.stylesheet_template
        for k, v in self.schema.items():
            template = template.replace(f'${k}', f'#{v}')
        self.stylesheet = template

    def set_font(self):
        fonts = Config(CONFIG_PATH / 'fonts')
        font_db = QFontDatabase()
        for font in fonts.all_configs.values():
            font_db.addApplicationFont(str(font))
        self.main_application.setFont(QFont('JetBrains Mono NL', 10))
