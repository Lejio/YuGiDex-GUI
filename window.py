from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFrame, QLabel
from components.titleButton import titleButton

class App(QMainWindow):
    
    def __init__(self, x, y, width, height):
        
        super(App, self).__init__()
        self.setGeometry(x, y, width, height)
        self.currWidth = width
        self.currHeight = height
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBarLayout = QVBoxLayout()
        self.mainScreenLayout = QHBoxLayout()
        
        titleBar = self.buildTitleBar()
        mainSection = self.buildMainSection()
        
        self.mainLayout.addWidget(titleBar)
        self.mainLayout.addWidget(mainSection)
        
        widget = QWidget()
        widget.setLayout(self.mainLayout)
        
        self.setCentralWidget(widget)
        self.setStyleSheet("""
                           background-color: gray;
                           padding: 0;
                           margin: 0;
                           """)
        
        
    def buildTitleBar(self):
        
        titleBar = QWidget()
        titleBarLayout = QHBoxLayout()
        
        appName = QLabel("YuGiDex")
        button1 = titleButton("green")
        button2 = titleButton("yellow")
        button3 = titleButton("red")
        
        titleBarLayout.addWidget(appName)
        titleBarLayout.addWidget(button1)
        titleBarLayout.addWidget(button2)
        titleBarLayout.addWidget(button3)
        
        titleBar.setLayout(titleBarLayout)
        titleBar.setFixedHeight(60)
        titleBar.setStyleSheet("""
                                    background-color: red;
                                    """)
        return titleBar
    
    def buildMainSection(self):
        
        mainSection = QWidget()
        mainSectionLayout = QHBoxLayout()
        
        label1 = QLabel("Menu Bar")
        label1.setStyleSheet("""
                             border: 2px solid yellow;
                             """)
        label2 = QLabel("Main Content")
        
        mainSectionLayout.addWidget(label1)
        mainSectionLayout.addWidget(label2)
        
        mainSection.setLayout(mainSectionLayout)
        
        return mainSection