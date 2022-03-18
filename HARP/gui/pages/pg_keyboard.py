# -*- coding: utf-8 -*-

import sys
if sys.version_info.major == 3:
    print('Python3')
    from types import SimpleNamespace as sn
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter import PhotoImage
    from tkinter import HORIZONTAL
else:
    print('Python2')
    # import types_py2
    # sn = types.SimpleNamespace
    from types_py2 import SimpleNamespace as sn
    import Tkinter as tk
    import ttk
    import tkMessageBox as messagebox
    from Tkinter import PhotoImage
    from Tkinter import HORIZONTAL

import gui

def page(arg):
    master = arg.master;

    
    handle = sn(**{  # KEYBOARD PAGE#####################################
        "label": sn(**{
            "obj": ttk.Label(master, \
                text="",
                style="keyboard.TLabel",
                anchor=tk.CENTER),
            "pos": sn(**{
                "x": 0,
                "y": 0,
                "w": 15,
                "h": 1,
            }),
            "number" : True,
        }),
#        "~": sn(**{
#            "obj": ttk.Button(master, \
#                text="~", \
#                style="keyboard.TButton", \
#                command=lambda: gui.keyboardInput(arg, "~")),
#            "pos": sn(**{
#                "x": 0,
#                "y": 1,
#                "w": 1,
#                "h": 1,
#            }),
#            "shift": "`",
#
#        }),
        "1": sn(**{
            "obj": ttk.Button(master, \
                text="1", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "1")),
            "pos": sn(**{
                "x": 1,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "1",
            "number": True,
        }),
        "2": sn(**{
            "obj": ttk.Button(master, \
                text="2", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "2")),
            "pos": sn(**{
                "x": 2,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "2",
            "number": True,
        }),
        "3": sn(**{
            "obj": ttk.Button(master, \
                text="3", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "3")),
            "pos": sn(**{
                "x": 3,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "3",
            "number": True,
        }),
        "4": sn(**{
            "obj": ttk.Button(master, \
                text="4", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "4")),
            "pos": sn(**{
                "x": 4,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "4",
            "number": True,
        }),
        "5": sn(**{
            "obj": ttk.Button(master, \
                text="5", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "5")),
            "pos": sn(**{
                "x": 5,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "5",
            "number": True,
        }),
        "6": sn(**{
            "obj": ttk.Button(master, \
                text="6", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "6")),
            "pos": sn(**{
                "x": 6,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "6",
            "number": True,
        }),
        "7": sn(**{
            "obj": ttk.Button(master, \
                text="7", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "7")),
            "pos": sn(**{
                "x": 7,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "7",
            "number": True,
        }),
        "8": sn(**{
            "obj": ttk.Button(master, \
                text="8", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "8")),
            "pos": sn(**{
                "x": 8,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "8",
            "number": True,
        }),
        "9": sn(**{
            "obj": ttk.Button(master, \
                text="9", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "9")),
            "pos": sn(**{
                "x": 9,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "9",
            "number": True,
        }),
        "0": sn(**{
            "obj": ttk.Button(master, \
                text="0", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "0")),
            "pos": sn(**{
                "x": 10,
                "y": 1,
                "w": 1,
                "h": 1,
            }),
            "shift": "0",
            "number": True,
        }),
        # "-": sn(**{
        #     "obj": ttk.Button(master, \
        #         text="-", \
        #         style="keyboard.TButton", \
        #         command=lambda: gui.keyboardInput(arg, "-")),
        #     "pos": sn(**{
        #         "x": 11,
        #         "y": 1,
        #         "w": 1,
        #         "h": 1,
        #     }),
        #     "shift": "_",
        #     "date": True,
        # }),
#        "=": sn(**{
#            "obj": ttk.Button(master, \
#                text="=", \
#                style="keyboard.TButton", \
#                command=lambda: gui.keyboardInput(arg, "=")),
#            "pos": sn(**{
#                "x": 12,
#                "y": 1,
#                "w": 1,
#                "h": 1,
#            }),
#            "shift": "+",
#        }),
        "backspace": sn(**{
            "obj": ttk.Button(master, \
                text="←", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "backspace")),
            "pos": sn(**{
                "x": 13,
                "y": 1,
                "w": 2,
                "h": 1,
            }),
            "number" : True,
        }),
        "q": sn(**{
            "obj": ttk.Button(master, \
                text="q", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "q")),
            "pos": sn(**{
                "x": 1.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "Q",
        }),
        "w": sn(**{
            "obj": ttk.Button(master, \
                text="w", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "w")),
            "pos": sn(**{
                "x": 2.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "W",
        }),
        "e": sn(**{
            "obj": ttk.Button(master, \
                text="e", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "e")),
            "pos": sn(**{
                "x": 3.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "E",
        }),
        "r": sn(**{
            "obj": ttk.Button(master, \
                text="r", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "r")),
            "pos": sn(**{
                "x": 4.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "R",
        }),
        "t": sn(**{
            "obj": ttk.Button(master, \
                text="t", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "t")),
            "pos": sn(**{
                "x": 5.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "T",
        }),
        "y": sn(**{
            "obj": ttk.Button(master, \
                text="y", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "y")),
            "pos": sn(**{
                "x": 6.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "Y",
        }),
        "u": sn(**{
            "obj": ttk.Button(master, \
                text="u", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "u")),
            "pos": sn(**{
                "x": 7.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "U",
        }),
        "i": sn(**{
            "obj": ttk.Button(master, \
                text="i", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "i")),
            "pos": sn(**{
                "x": 8.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "I",
        }),
        "o": sn(**{
            "obj": ttk.Button(master, \
                text="o", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "o")),
            "pos": sn(**{
                "x": 9.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "O",
        }),
        "p": sn(**{
            "obj": ttk.Button(master, \
                text="p", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "p")),
            "pos": sn(**{
                "x": 10.5,
                "y": 2,
                "w": 1,
                "h": 1,
            }),
            "shift": "P",
        }),
        #        "[" : sn(**{
        #            "obj" : ttk.Button(master, \
        #                                   text="[", \
        #                                   style="keyboard.TButton", \
        #                                   command=lambda: gui.keyboardInput(master,handles,"[")),
        #            "pos" : sn(**{
        #                "x" : 11.5,
        #                "y" : 2,
        #                "w" : 1,
        #                "h" : 1,
        #            }),
        #            "shift" : "{",
        #        }),
        #        "]" : sn(**{
        #            "obj" : ttk.Button(master, \
        #                                   text="]", \
        #                                   style="keyboard.TButton", \
        #                                   command=lambda: gui.keyboardInput(master,handles,"]")),
        #            "pos" : sn(**{
        #                "x" : 12.5,
        #                "y" : 2,
        #                "w" : 1,
        #                "h" : 1,
        #            }),
        #            "shift" : "}",
        #        }),
        #        "\\" : sn(**{
        #            "obj" : ttk.Button(master, \
        #                                   text="\\", \
        #                                   style="keyboard.TButton", \
        #                                   command=lambda: gui.keyboardInput(master,handles,"\\")),
        #            "pos" : sn(**{
        #                "x" : 13.5,
        #                "y" : 2,
        #                "w" : 1.5,
        #                "h" : 1,
        #            }),
        #            "shift" : "|",
        #        }),
        "a": sn(**{
            "obj": ttk.Button(master, \
                text="a", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "a")),
            "pos": sn(**{
                "x": 2,
                "y": 3,
                "w": 1,
                "h": 1,
            }),
            "shift": "A",
        }),
        "s": sn(**{
            "obj": ttk.Button(master, \
                text="s", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "s")),
            "pos": sn(**{
                "x": 3,
                "y": 3,
                "w": 1,
                "h": 1,
            }),
            "shift": "S",
        }),
        "d": sn(**{
            "obj": ttk.Button(master, \
                text="d", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "d")),
            "pos": sn(**{
                "x": 4,
                "y": 3,
                "w": 1,
                "h": 1,
            }),
            "shift": "D",
        }),
        "f": sn(**{
            "obj": ttk.Button(master, \
                text="f", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "f")),
            "pos": sn(**{
                "x": 5,
                "y": 3,
                "w": 1,
                "h": 1,
            }),
            "shift": "F",
        }),
        "g": sn(**{
            "obj": ttk.Button(master, \
                text="g", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "g")),
            "pos": sn(**{
                "x": 6,
                "y": 3,
                "w": 1,
                "h": 1,
            }),
            "shift": "G",
        }),
        "h": sn(**{
            "obj": ttk.Button(master, \
                text="h", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "h")),
            "pos": sn(**{
                "x": 7,
                "y": 3,
                "w": 1,
                "h": 1,
            }),
            "shift": "H",
        }),
        "j": sn(**{
            "obj": ttk.Button(master, \
                text="j", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "j")),
            "pos": sn(**{
                "x": 8,
                "y": 3,
                "w": 1,
                "h": 1,
            }),
            "shift": "J",
        }),
        "k": sn(**{
            "obj": ttk.Button(master, \
                text="k", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "k")),
            "pos": sn(**{
                "x": 9,
                "y": 3,
                "w": 1,
                "h": 1,
            }),
            "shift": "K",
        }),
        "l": sn(**{
            "obj": ttk.Button(master, \
                text="l", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "l")),
            "pos": sn(**{
                "x": 10,
                "y": 3,
                "w": 1,
                "h": 1,
            }),
            "shift": "L",
        }),
        # ":" : sn(**{
        #     "obj" : ttk.Button(master, \
        #                            text=":", \
        #                            style="keyboard.TButton", \
        #                            command=lambda: gui.keyboardInput(arg,":")),
        #     "pos" : sn(**{
        #         "x" : 11,
        #         "y" : 3,
        #         "w" : 1,
        #         "h" : 1,
        #     }),
        #     "shift" : ":",
        #     "time": True,
        # }),
        #        "'" : sn(**{
        #            "obj" : ttk.Button(master, \
        #                                   text="'", \
        #                                   style="keyboard.TButton", \
        #                                   command=lambda: gui.keyboardInput(master,handles,"'")),
        #            "pos" : sn(**{
        #                "x" : 12,
        #                "y" : 3,
        #                "w" : 1,
        #                "h" : 1,
        #            }),
        #            "shift" : "\"",
        #        }),
        "enter": sn(**{
            "obj": ttk.Button(master, \
                text="OK", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "ok")),
            "pos": sn(**{
                "x": 13,
                "y": 3,
                "w": 2,
                "h": 1,
            }),
            "number" : True,
        }),
    
    
        "lshift": sn(**{
            "obj": ttk.Button(master, \
                text="SHIFT", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "shift")),
            "pos": sn(**{
                "x": 0,
                "y": 4,
                "w": 2.5,
                "h": 1,
            }),
        }),
    
        "z": sn(**{
            "obj": ttk.Button(master, \
                text="z", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "z")),
            "pos": sn(**{
                "x": 2.5,
                "y": 4,
                "w": 1,
                "h": 1,
            }),
            "shift": "Z",
        }),
        "x": sn(**{
            "obj": ttk.Button(master, \
                text="x", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "x")),
            "pos": sn(**{
                "x": 3.5,
                "y": 4,
                "w": 1,
                "h": 1,
            }),
            "shift": "X",
        }),
        "c": sn(**{
            "obj": ttk.Button(master, \
                text="c", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "c")),
            "pos": sn(**{
                "x": 4.5,
                "y": 4,
                "w": 1,
                "h": 1,
            }),
            "shift": "C",
        }),
        "v": sn(**{
            "obj": ttk.Button(master, \
                text="v", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "v")),
            "pos": sn(**{
                "x": 5.5,
                "y": 4,
                "w": 1,
                "h": 1,
            }),
            "shift": "V",
        }),
        "b": sn(**{
            "obj": ttk.Button(master, \
                text="b", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "b")),
            "pos": sn(**{
                "x": 6.5,
                "y": 4,
                "w": 1,
                "h": 1,
            }),
            "shift": "B",
        }),
        "n": sn(**{
            "obj": ttk.Button(master, \
                text="n", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "n")),
            "pos": sn(**{
                "x": 7.5,
                "y": 4,
                "w": 1,
                "h": 1,
            }),
            "shift": "N",
        }),
        "m": sn(**{
            "obj": ttk.Button(master, \
                text="m", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "m")),
            "pos": sn(**{
                "x": 8.5,
                "y": 4,
                "w": 1,
                "h": 1,
            }),
            "shift": "M",
        }),
        # ",": sn(**{
        #     "obj": ttk.Button(master, \
        #         text=",", \
        #         style="keyboard.TButton", \
        #         command=lambda: gui.keyboardInput(arg, ",")),
        #     "pos": sn(**{
        #         "x": 9.5,
        #         "y": 4,
        #         "w": 1,
        #         "h": 1,
        #     }),
        #     "shift": ",",
        # }),
        # ".": sn(**{
        #     "obj": ttk.Button(master, \
        #         text=".", \
        #         style="keyboard.TButton", \
        #         command=lambda: gui.keyboardInput(arg, ".")),
        #     "pos": sn(**{
        #         "x": 10.5,
        #         "y": 4,
        #         "w": 1,
        #         "h": 1,
        #     }),
        #     "shift": ".",
        # }),
        #        "/" : sn(**{
        #            "obj" : ttk.Button(master, \
        #                                   text="/", \
        #                                   style="keyboard.TButton", \
        #                                   command=lambda: gui.keyboardInput(master,handles,"/")),
        #            "pos" : sn(**{
        #                "x" : 11.5,
        #                "y" : 4,
        #                "w" : 1,
        #                "h" : 1,
        #            }),
        #            "shift" : "?",
        #        }),
        "rshift": sn(**{
            "obj": ttk.Button(master, \
                text="SHIFT", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "shift")),
            "pos": sn(**{
                "x": 12.5,
                "y": 4,
                "w": 2.5,
                "h": 1,
            }),
        }),
        "space": sn(**{
            "obj": ttk.Button(master, \
                text="", \
                style="keyboard.TButton", \
                command=lambda: gui.keyboardInput(arg, "space")),
            "pos": sn(**{
                "x": 4,
                "y": 5,
                "w": 7,
                "h": 1,
            }),
        }),
    })
    return handle;

