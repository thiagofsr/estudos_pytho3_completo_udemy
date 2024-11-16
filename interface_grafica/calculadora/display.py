from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit

from variables import BIG_FONT_SIZE, MIMINUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configStyle()  # Configura estilo do display




    def configStyle(self):
        self.setStyleSheet(f'font-size:{BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)  # altura minima 2 vez para sobrar epsácao em branco 
        self.setMinimumWidth(MIMINUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # alinha texto a direita, com nas calculadores 
        self.setTextMargins(TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN)
