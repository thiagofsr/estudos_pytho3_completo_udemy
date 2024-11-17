from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QKeyEvent
from ui_window import Ui_MainWindow
from PySide6.QtCore import QObject, QEvent

from typing import cast


import sys

class MainWindo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # metodo que precisa se chamaddo para criar o interface, esta no arquivo gerado pelo qtdesigner
        self.setupUi(self)
        
        self.btn_send.clicked.connect(self.changeLabel)
        
        self.txb_name.installEventFilter(self)
        
    def changeLabel(self):
        text = self.txb_name.text()
        self.lbl_results.setText(text)
        
        
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        # filtrar o eneto desejado
        if event.type() == QEvent.Type.KeyPress:      
            event = cast(QKeyEvent, event)    
            text = self.txb_name.text()
            self.lbl_results.setText(text + event.text())

            
        return super().eventFilter(watched, event)

        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindo()
    mainWindow.show()
    app.exec()
        