from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from components.sideBarButtons import sideBarButton

class sideBar(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.barLayout = QVBoxLayout()
        self.setFixedWidth(150)
        self.setStyleSheet("""
                           border: 1px solid yellow;
                           """)

        self.buildBar()
        
    def buildBar(self):
        
        home = sideBarButton("Home")
        news = sideBarButton("News")
        search = sideBarButton("Search")
        build = sideBarButton("Build")
        unpack = sideBarButton("Unbox")
        settings = sideBarButton("Settings")
        
        # home = QPushButton("Home")
        # news = QPushButton("News")
        # search = QPushButton("Search")
        # build = QPushButton("Build")
        # unpack = QPushButton("Unbox")
        # settings = QPushButton("Settings")
        
        self.barLayout.addWidget(home)
        self.barLayout.addWidget(news)
        self.barLayout.addWidget(search)
        self.barLayout.addWidget(build)
        self.barLayout.addWidget(unpack)
        self.barLayout.addWidget(settings)
        
        self.setLayout(self.barLayout)
        
    
    