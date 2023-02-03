from PySide6.QtWidgets import QPushButton
        
'''
    Creates the title buttons, or more specifically, the green, yellow, red buttons.
'''
class titleButton(QPushButton):
    
    def __init__(self, color:str):
        super().__init__()
        
        FIXEDSIZE = 15
        
        self.color = color
        
        if color not in ["red", "yellow", "green"]:
            
            raise TypeError(f"The color '{self.color}' cannot be defined.")
        
        self.setFixedHeight(FIXEDSIZE)
        self.setFixedWidth(FIXEDSIZE)
        
        self.setStyleSheet(f"""
            border-radius: 7px;
            border: 1px solid black;
            background-color: {self.color};
            border: 2px solid yellow;
         """)
        
        # .setStyleSheet("""
        #                      border: 2px solid yellow;
        #                      """)
        
