from PySide6.QtWidgets import QPushButton
        
'''
    Creates the title buttons, or more specifically, the green, yellow, red buttons.
'''
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
        
