import sys
if sys.version_info.major == 3: from tkinter import ttk
else: import ttk

import g

def setup():
    ######## Pre-defined Styles ########
    styles = ttk.Style()
    
    styles.configure('labelTitle.TLabel',
                     font=('Arial', 16, 'bold'),
                     background=g.bgColor)
    
    styles.configure('labelPrompt.TLabel',
                     font=('Arial', 12),
                     background='#FFFFFF')


    styles.configure('button.TButton',
                     font=('Arial', 12, 'bold'))
    

    
    
    ### KEYBOAD FONTS
    styles.configure('keyboard.TButton', font=('Verdana', 16, 'bold'))

    return styles