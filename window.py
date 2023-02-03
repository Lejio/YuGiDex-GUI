from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from components.titleButton import titleButton
from components.sideBar import sideBar
from components.styles.default import *

class App(QMainWindow):
    
    def __init__(self, x, y, width, height):
        
        super(App, self).__init__()
        self.__sizeSetup(x, y, width, height)
        
        self.__mainLayout = QVBoxLayout()
        self.__mainLayout.setContentsMargins(0, 0, 0, 0)
        self.__mainLayout.setSpacing(0)
        
        # self.toolBarLayout = QVBoxLayout()
        # self.mainScreenLayout = QHBoxLayout()
        
        titleBar = self.__buildTitleBar()
        mainSection = self.__buildMainSection()
        
        self.__mainLayout.addWidget(titleBar)
        self.__mainLayout.addWidget(mainSection)
        
        widget = QWidget()
        widget.setLayout(self.__mainLayout)
        
        self.setCentralWidget(widget)
        self.setStyleSheet(defaultBackground())
        
    
    def __sizeSetup(self, x, y, width, height):
        self.setGeometry(x, y, width, height)
        self.currWidth = width
        self.currHeight = height
        self.setMinimumSize(width/2, height/2)
        
    def __buildTitleBar(self) -> QWidget:
        
        titleBar = QWidget()
        titleBarLayout = QHBoxLayout()
        titleBarLayout.setContentsMargins(0, 0, 0, 0)
        
        appName = QLabel("YuGiDex")
        appName.setStyleSheet(borderHighlight())
        
        # Generating title bar
        green = titleButton("green")
        green.clicked.connect(self.__fullScreen)
        yellow = titleButton("yellow")
        yellow.clicked.connect(self.__minimizeWindow)
        red = titleButton("red")
        red.clicked.connect(self.__closeProgram)
        
        titleBarLayout.addWidget(appName)
        
        titleBarLayout.addWidget(green)
        titleBarLayout.addWidget(yellow)
        titleBarLayout.addWidget(red)
                
        titleBar.setLayout(titleBarLayout)
        titleBar.setFixedHeight(30)
        titleBar.setStyleSheet(titleBarStyle())
        return titleBar
    
    def __buildMainSection(self) -> QWidget:
        
        mainSection = QWidget()
        mainSectionLayout = QHBoxLayout()
        mainSectionLayout.setContentsMargins(0, 0, 0, 0)
        
        # This changes the padding between items in a layout.
        mainSectionLayout.setSpacing(0)
        
        SideBar = sideBar()
        label2 = QLabel("Main Content")
        label2.setStyleSheet(borderHighlight())
        
        mainSectionLayout.addWidget(SideBar)
        mainSectionLayout.addWidget(label2)
        
        mainSection.setLayout(mainSectionLayout)
        
        return mainSection
    
    
    ###############################################################################################
    # Resized event ready for experimentation with custom flexbox. As of right now there is no    
    # concept of "flex-box" in PySide6 (that I am aware of). If I do want to implement flex-box   
    # properties (wrapping) I am afraid I have to do it manually.                                 
    ###############################################################################################
    # def resizeEvent(self, event):
    #     print("Window has been resized")
    #     QMainWindow.resizeEvent(self, event)
    
    ###############################################################################################
    # Assigned to the GREEN button. Allows full screening.                                        
    ###############################################################################################
    def __fullScreen(self):
        if not self.isFullScreen():
            self.showFullScreen()
            
        else:
            self.showNormal()
    
    ###############################################################################################
    # Assigned to the YELLOW button. Allows minimizing.                                           
    ###############################################################################################
    def __minimizeWindow(self):
        self.showMinimized()
    
    
    ###############################################################################################
    # Assigned to the RED button. Can exit the program.                                           
    ###############################################################################################
    def __closeProgram(self):
        exit()
    