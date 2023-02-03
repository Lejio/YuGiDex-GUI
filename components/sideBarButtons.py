from PySide6.QtWidgets import QPushButton, QMainWindow

class sideBarButton(QPushButton):
    
    def __init__(self, name:str):
        super().__init__()
        
        self.setText(name)
        # self.clicked.connect(self.fullScreen())
        self.setStyleSheet("""
                           border-radius: 10px;
                           border: 1px solid green;
                           background-color: #96C9DC;
                           color: black;
                           """)
        
    # def fullScreen(self):
        
    #     print("clicked")
    #     QMainWindow.showFullScreen()