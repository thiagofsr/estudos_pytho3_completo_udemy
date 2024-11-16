from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import SMALL_FONT_SIZE

class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configStyle()

    def configStyle(self):
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet(f'font-size:{SMALL_FONT_SIZE}px;')
