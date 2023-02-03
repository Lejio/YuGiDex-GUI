from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFrame, QLabel
from components.titleButton import titleButton
from components.sideBar import sideBar

class App(QMainWindow):
    
    def __init__(self, x, y, width, height):
        
        super(App, self).__init__()
        self.setGeometry(x, y, width, height)
        self.currWidth = width
        self.currHeight = height
        self.setMinimumSize(width/2, height/2)
        
        # Opens the application in full screen mode.
        # self.showFullScreen()
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        
        # self.toolBarLayout = QVBoxLayout()
        # self.mainScreenLayout = QHBoxLayout()
        
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
        titleBarLayout.setContentsMargins(0, 0, 0, 0)
        
        appName = QLabel("YuGiDex")
        appName.setStyleSheet("""
                             border: 1px solid yellow;
                             """)
        
        # Generating title bar
        green = titleButton("green")
        green.clicked.connect(self.fullScreen)
        yellow = titleButton("yellow")
        yellow.clicked.connect(self.minimizeWindow)
        red = titleButton("red")
        red.clicked.connect(self.closeProgram)
        
        titleBarLayout.addWidget(appName)
        
        
        titleBarLayout.addWidget(green)
        titleBarLayout.addWidget(yellow)
        titleBarLayout.addWidget(red)
        
        # titleBarLayout.setSpacing(10)
        
        titleBar.setLayout(titleBarLayout)
        titleBar.setFixedHeight(30)
        titleBar.setStyleSheet("""
                                    background-color: red;
                                    """)
        return titleBar
    
    def buildMainSection(self):
        
        mainSection = QWidget()
        mainSectionLayout = QHBoxLayout()
        mainSectionLayout.setContentsMargins(0, 0, 0, 0)
        
        # This changes the padding between items in a layout.
        mainSectionLayout.setSpacing(0)
        
        SideBar = sideBar()
        label2 = QLabel("Main Content")
        label2.setStyleSheet("""
                             border: 1px solid yellow;
                             """)
        
        mainSectionLayout.addWidget(SideBar)
        mainSectionLayout.addWidget(label2)
        
        mainSection.setLayout(mainSectionLayout)
        
        return mainSection
    
    # Resized event ready for experimentation with custom flexbox
    # def resizeEvent(self, event):
    #     print("Window has been resized")
    #     QMainWindow.resizeEvent(self, event)
    
    ###############################################################################################
    # Assigned to the GREEN button. Allows full screening.                                        #
    ###############################################################################################
    def fullScreen(self):
        
        if not self.isFullScreen():
            print("Entering full screen.")
            self.showFullScreen()
            
        else:
            print("Exiting full screen.")
            self.showNormal()
    
    ###############################################################################################
    # Assigned to the YELLOW button. Allows minimizing.                                           #
    ###############################################################################################
    def minimizeWindow(self):
        
        print("Minimizing.")
        self.showMinimized()
    
    
    ###############################################################################################
    # Assigned to the RED button. Can exit the program.                                           #
    ###############################################################################################
    def closeProgram(self):
        
        print("Closing program")
        exit()
    