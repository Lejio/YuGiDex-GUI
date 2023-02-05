from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QWidget
from components.styles.settingsStyle import background

class settings:
    
    def __init__(self) -> None:
        
        self.__layout = QHBoxLayout();
        self.__buildContent()
        
    
    def getWidget(self):
        
        w = QWidget()
        w.setLayout(self.__layout)
        return w
    
    def __buildContent(self):
        
        self.mainWidget = QWidget()
        self.mainWidget.setStyleSheet(background())
        
        self.__layout.addWidget(self.mainWidget)