from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QWidget
from components.styles.homeStyle import background

class home:
    
    def __init__(self) -> None:
        
        self.__layout = QHBoxLayout();
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__buildContent()
        
    
    def getWidget(self):
        
        export = QWidget()
        export.setLayout(self.__layout)
        return export
    
    def __buildContent(self):
        
        self.mainWidget = QWidget()
        self.mainWidget.setStyleSheet(background())
        
        self.secondWidget = QWidget()
        self.secondWidget.setStyleSheet("""
                                        background-color: gray;
                                        """)
        
        self.__layout.addWidget(self.mainWidget)
        self.__layout.addWidget(self.secondWidget)