import sys

import yaml
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QPushButton
from PySide6.QtGui import QFont, QFontDatabase
with open('/config/theme/gruvbox-dark-hard.yaml', 'r') as file:
    colors = yaml.safe_load(file)

schema = {k: f"#{v}" for k, v in colors.items() if k.startswith('base')}



def apply_schema(schema, style:str):
    for k, v in schema.items():
        style = style.replace(f'${k}', v)
    return style


class Pallete(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setMinimumSize(400,400)
        self.setObjectName('default')
        for k, v in colors.items():
            if k.startswith('base'):
                label = QLabel(k)
                label.setMinimumWidth(350)
                # label.setFont(QFont())
                # label.setStyleSheet(f'background-color: #{v}')
                # self.layout.addWidget(label)
                self.layout.addWidget(QPushButton(k))
        self.setLayout(self.layout)
if __name__ == '__main__':
    qapp = QApplication()

    id = QFontDatabase().addApplicationFont('/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/config/fonts/JetBrainsMonoNL-Bold.ttf')
    families = QFontDatabase.applicationFontFamilies(id)
    print(families[0])


    qapp.setFont(QFont(families[0], 10))
    window = Pallete()
    window.show()
    sys.exit(qapp.exec())
