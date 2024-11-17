
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, 
                               QWidget)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        #configurar janela layout básico
        self.cw = QWidget() # cria widget central 
        self.vLayout = QVBoxLayout() 
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
        
        # adiciona titulo da janela principal
        self.setWindowTitle("Calculadora - Thiago")

        # configura janiela para tamanho fixo



    # funçã que ajusta tamanho da tala para o tamanho dos widgets, e fixar. 
    def adjustFixedSize(self):
        # ultima coisa a ser feita antes de criar a janela 
        # depende de criar todos os widgets 
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

        

    # com oboa pratica é interenssante sempre que se tem 3 niveis 
    # cria-se uma função para isso , caso da função abaixo
    def addWidgetToVLayout(self, widget: QWidget): #Esse final é para indicar que a tipagel do parametro é QWidiget 
        #adiciona widget no layout
        self.vLayout.addWidget(widget)


