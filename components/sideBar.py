from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from components.sideBarButtons import sideBarButton
from components.styles.default import sideBarStyle

class sideBar(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.barLayout = QVBoxLayout()
        self.setFixedWidth(150)

        self.buildBar()
        self.setStyleSheet(sideBarStyle())
        
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
        
        self.setLayout(self.barLayout)
        
    
    