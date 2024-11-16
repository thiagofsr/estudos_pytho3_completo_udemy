# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, 
                               QMainWindow,
                               QVBoxLayout, QHBoxLayout, QGridLayout, )


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Nome da jamnela')
        
        # botoes
        self.button = QPushButton('Textodo Botão 1')
        self.button.setStyleSheet('font-size: 40px; background-color: red; color: white')
        self.button2 = QPushButton('Textodo Botão 2')
        self.button2.setStyleSheet('font-size:20px;')
        self.button3 = QPushButton('Textodo Botão 3')
        self.button3.setStyleSheet('font-size:20px;')


        # layout = QVBoxLayout() # cria o layati central no vaso vertical
        # layout = QHBoxLayout() # cria o layout Horizoltal 
        self.grig_layout = QGridLayout() # cria o layout
        self.central_widget.setLayout(self.grig_layout) # conecta o central widget com o layout 

        # layout.addWidget(button) # adiciona o botão 1 no layout
        # layout.addWidget(button2) # adiciona o botão
        # no caso de usar grid o addWidget rece a posiçãO, linhs e depois coluna, row spawm, col spam ( por padrão 1, 1):
        self.grig_layout.addWidget(self.button, 1, 1, 1, 2) # adiciona o botão 1 no layout
        self.grig_layout.addWidget(self.button2, 2, 1, 1, 1) # adiciona
        self.grig_layout.addWidget(self.button3, 2, 2, 1, 1) # adiciona


        #status bar ( barra inferior )
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('mensage,m na estatus bar ')

        # menuBar 
        self.menu = self.menuBar()
        self.menu_arquivos = self.menu.addMenu('Arquivo')
        
        self.item_1 = self.menu_arquivos.addAction('Novo')
        self.item_1.triggered.connect(self.acao_item1)

        self.item_2 = self.menu_arquivos.addAction('abrir')
        self.item_2.setCheckable(True)
        self.item_2.triggered.connect(self.acao_item2)
        self.item_2.hovered.connect(self.acao_item2)


    @Slot()
    def acao_item1(self):
        self.status_bar.showMessage('Item 1 do menu pressionado')

    @Slot()
    def acao_item2(self):
        print('Esta marcado', self.item_2.isChecked())









    # # funções
    # @slot()
    # def slot_exemple( msg ):
    #     status_bar.showMessage( msg )











if __name__ == '__main__':
    app = QApplication(sys.argv) # aplicação que sera rodadada
    window = MyWindow()
    window.show() # mostra o widget central 
    app.exec() # excevuta a apalicação em loop 





