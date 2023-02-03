
def borderHighlight():
    
    return """
border: 1px solid #F5D491;
"""

def defaultBackground():
    
    return """
background-color: gray;
"""

def titleBarStyle():
    
    return """
background-color: #61A0AF;
"""

def sideBarStyle():
    
    style = borderHighlight()
    print("Adding Style.")
    return style 
# + """
# background-color: #F06C9B;
# """

def sideBarButtonStyle():
    
    return """
border-radius: 10px;
border: 1px solid green;
background-color: #96C9DC;
color: black;
"""