from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QEvent
from components.styles.searchStyle import buttonStyle

class searchButton(QPushButton):
    
    def __init__(self, name:str) -> None:
        super(searchButton, self).__init__()
        
        self.setStyleSheet(buttonStyle())
        self.setText(name)
        
        # self.clicked.connect(self.processSearch)
        
    
    def mousePressEvent(self, e):
        
        print("Pressed")
        
    # def processSearch(self):
        
    #     print("Bruh")