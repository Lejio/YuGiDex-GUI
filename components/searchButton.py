from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QPropertyAnimation, QPoint
from components.styles.searchStyle import buttonStyle

class searchButton(QPushButton):
    
    def __init__(self, name:str) -> None:
        super(searchButton, self).__init__()
        
        self.setStyleSheet(buttonStyle())
        self.setText(name)
        
        # self.clicked.connect(self.processSearch)
        
    
    # def mousePressEvent(self, e):
        
    #     print("Starting animation.")
    #     self.anim = QPropertyAnimation(self.child, b"color")
        # self.anim.setEasingCurve(easing=)
        # self.anim.setEndValue(QPoint(400, 400))
        # self.anim.setDuration(1500)
        # self.anim.start()
        
    # def processSearch(self):
        
    #     print("Bruh")