from easygui import *
text = "Selected any one item"
title = "Window Title GfG"
choices = ["Geek", "Super Geeek", "Super Geek 2", "Super Geek God"] 
output = choicebox(text, title, choices) 
title = "Message Box"
message = "You selected : " + str(output) 
msg = msgbox(message, title) 