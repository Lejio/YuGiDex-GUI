from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from components.sideBarButtons import sideBarButton
from components.styles.default import sideBarStyle

class sideBar(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.barLayout = QVBoxLayout()
        self.setFixedWidth(150)

        # self.container = QWidget()
        self.buildBar()
                
    def buildBar(self):
        
        menu = sideBarButton("Menu")
        home = sideBarButton("Home")
        news = sideBarButton("News")
        search = sideBarButton("Search")
        build = sideBarButton("Build")
        unpack = sideBarButton("Unbox")
        settings = sideBarButton("Settings")
        
        self.barLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.barLayout.addWidget(menu)
        self.barLayout.addWidget(home)
        self.barLayout.addWidget(news)
        self.barLayout.addWidget(search)
        self.barLayout.addWidget(build)
        self.barLayout.addWidget(unpack)
        self.barLayout.addWidget(settings)
        
        # self.container.setLayout(self.barLayout)
        
        # self.layoutContainer = QVBoxLayout()
        # self.container.setStyleSheet(sideBarStyle())

        
        # self.layoutContainer.addWidget(self.container)
        
        # self.setLayout(self.layoutContainer)
        
        self.setLayout(self.barLayout)
                
    
    