import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon

from main_window import MainWindow
from display import Display
from info import Info
from buttons import ButtonsGrid
from style import setupTheme

from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme(app) # configura o tema da janela
    window = MainWindow() # cria com base na classe MainWindow que criamso no outro arquivo

    # ======== defione o icom e configura na app
    icon = QIcon(str(WINDOW_ICON_PATH)) # importante não esquecer de convertar para str 
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    
    # window.label1 = QLabel('Texte.........')
    # window.label1.setStyleSheet('font-size:70px; ')
    # # window.v_layout.addWidget(window.label1)
    # window.addWidgetToVLayout(window.label1)

    #============info superior
    info = Info("44 * 44 = 1234123")
    window.addWidgetToVLayout(info)

    # disp[lay da calcuulatora
    display = Display()
    window.addWidgetToVLayout(display)
  
    #========grid com os botões 
    buttonsGrid = ButtonsGrid(display)
    # aqui adicionamos um butoins, no layoiut que esta dentro de Vlayou
    window.vLayout.addLayout(buttonsGrid)


    # chama a função que criamos para ajustar a janala para oa tamanho do que foi criado 
    window.adjustFixedSize()

    window.show()
    app.exec()