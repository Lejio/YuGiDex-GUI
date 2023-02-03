from PySide6.QtWidgets import QPushButton, QMainWindow
from components.styles.default import sideBarButtonStyle

class sideBarButton(QPushButton):
    
    def __init__(self, name:str):
        super().__init__()
        
        self.setText(name)
        # self.clicked.connect(self.fullScreen())
        self.setStyleSheet(sideBarButtonStyle())
        
    # def fullScreen(self):
        
    #     print("clicked")
    #     QMainWindow.showFullScreen()