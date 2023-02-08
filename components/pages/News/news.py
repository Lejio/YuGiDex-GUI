from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt
from components.styles.newsStyle import *

class news:
    
    def __init__(self) -> None:
        
        self.__layout = QHBoxLayout();
        # self.__layout.setContentsMargins(0, 0, 0, 0)
        # self.__buildContent()
        
    
    def getWidget(self):
        
        # w = QWidget()
        # w.setLayout(self.__layout)
        return self.mainWidget
    
    def buildContent(self):
        
        self.mainWidget = QWidget()
        self.mainWidget.setStyleSheet(background())
        
        self.searchBar = QLineEdit("Enter Card Name")
        self.searchBar.setFixedSize(400, 50)
        self.searchButton = QPushButton("Search")
        # self.searchButton.setStyleSheet(buttonStyle())
        
        self.searchLabel = QLabel("Yu-Gi-Oh Database")
        

        self.mainWidgetLayout = QVBoxLayout()
        self.mainWidgetLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.mainWidgetLayout.setGeometry(500, 50)
        self.mainWidgetLayout.addWidget(self.searchLabel)
        self.mainWidgetLayout.addWidget(self.searchBar)
        self.mainWidgetLayout.addWidget(self.searchButton)
        
        self.mainWidget.setLayout(self.mainWidgetLayout)
        
        self.searchButton.clicked.connect(self.print_hello)

        
        # self.__layout.addWidget(self.mainWidget)
        
    def print_hello():
        
        print("Hello")