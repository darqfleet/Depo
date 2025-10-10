from PySide6.QtWidgets import QListWidget, QListWidgetItem, QApplication, QPushButton, QWidget, QHBoxLayout, QLabel


class WagonWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.layout.addWidget(QLabel('Test'))
        self.layout.addWidget(QPushButton('Push'))
        self.setLayout(self.layout)


if __name__ == '__main__':
    qapp = QApplication()
    w = QListWidget()
    w.setAlternatingRowColors(True)

    itms = [QListWidgetItem()  for x in range(10)]
    for i in itms:
        w.addItem(i)
        w.setItemWidget(i, WagonWidget())
    w.show()
    qapp.exec()