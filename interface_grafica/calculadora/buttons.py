from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from display import Display
from PySide6.QtCore import Slot
from utils import isEmpty, isNUmOrDot


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.configStyle()
        
    def configStyle(self):
        # essa manaiera pode correr o risco de sobrescrever a fonteo 
        # self.setStyleSheet(f'font-size:{MEDIUM_FONT_SIZE}px;')
        
        
        # outra maneirao é criar uma variavel fonte para ter acesso as mudacas dessa variavel 
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        # font.setBold(True)
        # font.setItalic(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        

        


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='], 
        ]
        self.display = display
        self.makeGrid()
        
        
    def makeGrid(self):
        for i, rowDat in enumerate(self._gridMask):
            for j,  buttonText in enumerate(rowDat):
                button = Button(buttonText)
                
                if not isNUmOrDot(buttonText) and not isEmpty(buttonText):
                    # definindo a propriedade que esta no qss ( arquivo style.py)
                    button.setProperty('cssClass', 'specialButton')
                    
                self.addWidget(button, i, j)                
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)
                
    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):   #_ quando não se vai usar a variavel , pode colocar o _  
            func(*args, **kwargs)
        return realSlot
    
    def _insertButtonTextToDisplay(self, button):
        button_text = button.text()
        self.display.insert(button_text)
                
                
                