from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QHoverEvent

# class titleButton:
    
#     def __init__(self, color:str):
                
        # self.color = color
        
        # if color not in ["red", "yellow", "green"]:
            
        #     raise TypeError(f"The color '{self.color}' cannot be defined.")
        
#         self.__button = QPushButton()
#         self.__button.setFixedHeight(20)
#         self.__button.setFixedWidth(20)
        
#         self.__style()
        
#     def __style(self) -> None:
        
#         self.__button.setStyleSheet(f"""
#                                     border-radius: 10px;
#                                     border: 1px solid black;
#                                     background-color: {self.color};
#                                     """)
    
#     def getButton(self) -> QPushButton:
        
#         return self.__button
        
        
class titleButton(QPushButton):
    
    def __init__(self, color:str):
        super().__init__()
        
        self.color = color
        
        if color not in ["red", "yellow", "green"]:
            
            raise TypeError(f"The color '{self.color}' cannot be defined.")
        
        self.setFixedHeight(20)
        self.setFixedWidth(20)
        
        self.setStyleSheet(f"""
            border-radius: 10px;
            border: 1px solid black;
            background-color: {self.color};
         """)
        
    # def QHoverEvent