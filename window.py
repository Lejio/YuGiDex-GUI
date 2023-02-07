from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QStackedLayout
from components.titleButton import titleButton
from components.sideBar import sideBar
from components.styles.default import *
# from components.pages.Build.build import build
# from components.pages.Home.home import home
# from components.pages.News.news import news
# from components.pages.Search.search import search
# from components.pages.Settings.settings import settings
# from components.pages.Unbox.unbox import unbox

from components.pages.TestTemplate.contentTemplate import test
from components.pages.TestTemplate.widgetStackTemplate import stack

class App(QMainWindow):
    
    def __init__(self, x, y, width, height):
        
        super(App, self).__init__()
        self.__sizeSetup(x, y, width, height)
        
        self.__mainLayout = QVBoxLayout()
        self.__mainLayout.setContentsMargins(0, 0, 0, 0)
        self.__mainLayout.setSpacing(0)
        
        # self.toolBarLayout = QVBoxLayout()
        # self.mainScreenLayout = QHBoxLayout()
        
        self.__mainContentLayout = QStackedLayout()
        self.__mainContent = QWidget()
        
        titleBar = self.__buildTitleBar()
        mainSection = self.__buildMainSection()
        
        # Main layout consists of both the scroll bar and the content area.
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
        sideButtons = SideBar.sideButtons
        sideButtons["Menu"].clicked.connect(self.__openMenuPage)
        sideButtons["Home"].clicked.connect(self.__openHomePage)
        sideButtons["News"].clicked.connect(self.__openNewsPage)
        sideButtons["Search"].clicked.connect(self.__openSearchPage)
        sideButtons["Build"].clicked.connect(self.__openBuildPage)
        sideButtons["Unbox"].clicked.connect(self.__openUnboxPage)
        sideButtons["Settings"].clicked.connect(self.__openSettingsPage)
        
        self.__preloadProcedure()
        
        self.__mainContent.setLayout(self.__mainContentLayout)
        mainSectionLayout.addWidget(SideBar)
        mainSectionLayout.addWidget(self.__mainContent)
        
        mainSection.setLayout(mainSectionLayout)
        
        return mainSection
    
    def __preloadProcedure(self):
        
        menuPage = test("red")
        homePage = test("blue")
        newsPage = test("yellow")
        searchPage = test("orange")
        buildPage = test("green")
        unboxPage = test("blue")
        settingsPage = test("purple")
        
        self.__mainContentLayout.addWidget(menuPage.getWidget())
        self.__mainContentLayout.addWidget(homePage.getWidget())
        self.__mainContentLayout.addWidget(newsPage.getWidget())
        self.__mainContentLayout.addWidget(searchPage.getWidget())
        self.__mainContentLayout.addWidget(buildPage.getWidget())
        self.__mainContentLayout.addWidget(unboxPage.getWidget())
        self.__mainContentLayout.addWidget(settingsPage.getWidget())
    
    def __openMenuPage(self):
        
        self.__mainContentLayout.setCurrentIndex(0)
        
    def __openHomePage(self):
        
        self.__mainContentLayout.setCurrentIndex(1)
        
    def __openNewsPage(self):
        
        self.__mainContentLayout.setCurrentIndex(2)
        
    def __openSearchPage(self):
        
        self.__mainContentLayout.setCurrentIndex(3)
        
    def __openBuildPage(self):
        
        self.__mainContentLayout.setCurrentIndex(4)
        
    def __openUnboxPage(self):
        
        self.__mainContentLayout.setCurrentIndex(5)
        
    def __openSettingsPage(self):
        
        self.__mainContentLayout.setCurrentIndex(6)
    
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
    