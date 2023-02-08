from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt
from components.searchButton import searchButton
from components.styles.searchStyle import *

class search:
    
    def __init__(self) -> None:
        
        self.__layout = QHBoxLayout();
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__buildContent()
        
    
    def getWidget(self):
        
        w = QWidget()
        w.setLayout(self.__layout)
        return w
    
    def __buildContent(self):
        
        self.mainWidget = QWidget()
        self.mainWidget.setStyleSheet(background())
        
        self.searchBar = QLineEdit()
        # self.searchBar.setText("Enter Card Name")
        self.searchBar.setFixedSize(400, 50)
        
        # self.searchButton = searchButton("Search")
        # self.searchButton = searchButton("Search")
        self.searchButton = QPushButton("Search")
        self.searchButton.setStyleSheet(buttonStyle())
        self.searchButton.clicked.connect(self.__processSearch)
        
        self.searchLabel = QLabel("Yu-Gi-Oh Database")
        self.searchLabel.setStyleSheet(labelStyle())

        
        self.mainWidgetLayout = QVBoxLayout()
        self.mainWidgetLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainWidgetLayout.addWidget(self.searchLabel)
        self.mainWidgetLayout.addWidget(self.searchBar)
        self.mainWidgetLayout.addWidget(self.searchButton)
        
        # print("bruh")
        
        self.mainWidget.setLayout(self.mainWidgetLayout)

        self.__layout.addWidget(self.mainWidget)
        
    def getSearchButton(self):
        
        # print(a)
        return self.searchButton
    
    def __processSearch(self):
        
        print(self.searchBar.text())
        print("Search in Progress.")
        