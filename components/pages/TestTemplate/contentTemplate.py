from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QWidget
from components.styles.testStyles import background

class test:
    
    def __init__(self, color:str) -> None:
        
        self.__layout = QHBoxLayout();
        self.__buildContent(color=color)
        
    
    def getWidget(self):
        
        w = QWidget()
        w.setLayout(self.__layout)
        return w
    
    def __buildContent(self, color):
        
        self.mainWidget = QWidget()
        self.mainWidget.setStyleSheet(background(color))
        
        self.__layout.addWidget(self.mainWidget)