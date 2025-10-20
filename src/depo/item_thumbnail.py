import sys
import math
from fileseq import FileSequence, findSequencesOnDisk
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QHBoxLayout
from PySide6.QtGui import QPixmap, QMouseEvent, Qt


class ItemThumbnail(QLabel):
    def __init__(self, file_sequence: FileSequence, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(500, 500)
        self.sequence = file_sequence
        self.start = file_sequence.start()
        self.end = file_sequence.end()
        self.current_frame = self.start
        self.frame_pixmap = QPixmap(file_sequence.frame(self.current_frame))
        self.set_pixmap(self.frame_pixmap)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event: QMouseEvent, /):
        self.set_frame(event)

    def resizeEvent(self, event, /):
        self.set_pixmap(self.frame_pixmap)

    def set_pixmap(self, pixmap: QPixmap):
        aspect = Qt.AspectRatioMode.KeepAspectRatio
        transformation = Qt.TransformationMode.SmoothTransformation
        self.setPixmap(pixmap.scaled(self.size(), aspect, transformation))

    def set_frame(self, event: QMouseEvent):
        normalized_cursor_x = event.position().x() / self.size().width()
        seq_length = self.end - self.start
        self.current_frame = math.ceil(seq_length * normalized_cursor_x + self.start)
        self.frame_pixmap = QPixmap(self.sequence.frame(self.current_frame))
        self.set_pixmap(self.frame_pixmap)


if __name__ == '__main__':
    qapp = QApplication()
    sequence: FileSequence = findSequencesOnDisk('/home/ydanilovsky@nolabel.local/temp_sequence/seq.####.jpg')[0]
    w = QWidget()
    w.setLayout(QHBoxLayout())
    w.layout().addWidget(ItemThumbnail(sequence))
    w.layout().addWidget(ItemThumbnail(sequence))
    w.layout().addWidget(ItemThumbnail(sequence))
    w.show()
    sys.exit(qapp.exec())
