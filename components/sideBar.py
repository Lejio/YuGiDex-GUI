from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from components.sideBarButtons import sideBarButton
from components.styles.default import sideBarStyle

class sideBar(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.barLayout = QVBoxLayout()
        self.setFixedWidth(150)

        self.container = QWidget()
        self.sideButtons = {}
        self.__buildBar()
                
    def __buildBar(self):
        
        self.__buildButtons()
        
        self.container.setLayout(self.barLayout)
        
        self.layoutContainer = QVBoxLayout()
        self.layoutContainer.setContentsMargins(0, 0, 0, 0)
        self.container.setStyleSheet(sideBarStyle())
        
        self.layoutContainer.addWidget(self.container)
        
        self.setLayout(self.layoutContainer)
        
        
    def __buildButtons(self):
        
        self.sideButtons["Menu"] = sideBarButton("Menu")
        self.sideButtons["Home"] = sideBarButton("Home")
        self.sideButtons["News"] = sideBarButton("News")
        self.sideButtons["Search"] = sideBarButton("Search")
        self.sideButtons["Build"] = sideBarButton("Build")
        self.sideButtons["Unbox"] = sideBarButton("Unbox")
        self.sideButtons["Settings"] = sideBarButton("Settings")
                
        self.barLayout.addWidget(self.sideButtons["Menu"])
        self.barLayout.addWidget(self.sideButtons["Home"])
        self.barLayout.addWidget(self.sideButtons["News"])
        self.barLayout.addWidget(self.sideButtons["Search"])
        self.barLayout.addWidget(self.sideButtons["Build"])
        self.barLayout.addWidget(self.sideButtons["Unbox"])
        self.barLayout.addWidget(self.sideButtons["Settings"])

        self.barLayout.setAlignment(Qt.AlignmentFlag.AlignTop)