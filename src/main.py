import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
import subprocess
import tempfile
from tkinter import *
from tkinter import filedialog, messagebox

import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
# customtkinter.set_widget_scaling(1.1)  # widget dimensions and text size
# customtkinter.set_spacing_scaling(1.1)  # padding and place positions
# customtkinter.set_window_scaling(1.1)  # window geometry dimensions

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("1080x720")
root.title("M4M Configurator")
root.resizable(0, 0)

options_0 = ['On hold', 'On first release', 'On last release']
menu_0 = customtkinter.CTkOptionMenu(master=root, values=options_0, fg_color='grey')
menu_0.grid(padx=20, pady=10, column=0, row=1, sticky="w")
menu_0.set(options_0[1])

options_1 = ['xBtn1', 'xBtn1¦2', 'xBtn2', 'lBtn', 'rBtn']
menu_1 = customtkinter.CTkOptionMenu(master=root, values=options_1)
menu_1.grid(padx=20, pady=0, column=0, row=2, sticky="w")
menu_1.set(options_1[0])

options_2 = ['---', 'xBtn1', 'xBtn2', 'lBtn', 'rBtn', 'mBtn', 'wUp', 'wDown']
menu_2 = customtkinter.CTkOptionMenu(master=root, values=options_2)
menu_2.grid(padx=20, pady=0, column=0, row=3, sticky="w")
menu_2.set(options_2[0])

options_3 = ['---', 'xBtn1', 'xBtn2', 'lBtn', 'rBtn', 'mBtn', 'wUp', 'wDown']
menu_3 = customtkinter.CTkOptionMenu(master=root, values=options_3)
menu_3.grid(padx=20, pady=0, column=0, row=4, sticky="w")
menu_3.set(options_3[0])

all_combos = ['xBtn1__', 'xBtn1_', 'xBtn1__lBtn__', 'xBtn1__lBtn_', '_xBtn1__lBtn_', 'xBtn1__lBtn_xBtn2__',
              'xBtn1__lBtn_xBtn2_', '_xBtn1__lBtn_xBtn2_', 'xBtn1__lBtn_rBtn__', 'xBtn1__lBtn_rBtn_',
              '_xBtn1__lBtn_rBtn_', 'xBtn1__lBtn_mBtn__', 'xBtn1__lBtn_mBtn_', '_xBtn1__lBtn_mBtn_',
              'xBtn1__lBtn_wDown_', '_xBtn1__lBtn_wDown_', 'xBtn1__lBtn_wUp_', '_xBtn1__lBtn_wUp_', 'xBtn1__rBtn__',
              'xBtn1__rBtn_', '_xBtn1__rBtn_', 'xBtn1__rBtn_xBtn2__', 'xBtn1__rBtn_xBtn2_', '_xBtn1__rBtn_xBtn2_',
              'xBtn1__rBtn_lBtn__', 'xBtn1__rBtn_lBtn_', '_xBtn1__rBtn_lBtn_', 'xBtn1__rBtn_mBtn__',
              'xBtn1__rBtn_mBtn_', '_xBtn1__rBtn_mBtn_', 'xBtn1__rBtn_wDown_', '_xBtn1__rBtn_wDown_',
              'xBtn1__rBtn_wUp_', '_xBtn1__rBtn_wUp_', 'xBtn1__mBtn__', 'xBtn1__mBtn_', '_xBtn1__mBtn_',
              'xBtn1__mBtn_xBtn2__', 'xBtn1__mBtn_xBtn2_', '_xBtn1__mBtn_xBtn2_', 'xBtn1__mBtn_lBtn__',
              'xBtn1__mBtn_lBtn_', '_xBtn1__mBtn_lBtn_', 'xBtn1__mBtn_rBtn__', 'xBtn1__mBtn_rBtn_',
              '_xBtn1__mBtn_rBtn_', 'xBtn1__mBtn_wDown_', '_xBtn1__mBtn_wDown_', 'xBtn1__mBtn_wUp_',
              '_xBtn1__mBtn_wUp_', 'xBtn1__wDown_', '_xBtn1__wDown_', 'xBtn1__wDown_xBtn2__', 'xBtn1__wDown_xBtn2_',
              '_xBtn1__wDown_xBtn2_', 'xBtn1__wDown_lBtn__', 'xBtn1__wDown_lBtn_', '_xBtn1__wDown_lBtn_',
              'xBtn1__wDown_rBtn__', 'xBtn1__wDown_rBtn_', '_xBtn1__wDown_rBtn_', 'xBtn1__wDown_mBtn__',
              'xBtn1__wDown_mBtn_', '_xBtn1__wDown_mBtn_', 'xBtn1__wUp_', '_xBtn1__wUp_', 'xBtn1__wUp_xBtn2__',
              'xBtn1__wUp_xBtn2_', '_xBtn1__wUp_xBtn2_', 'xBtn1__wUp_lBtn__', 'xBtn1__wUp_lBtn_', '_xBtn1__wUp_lBtn_',
              'xBtn1__wUp_rBtn__', 'xBtn1__wUp_rBtn_', '_xBtn1__wUp_rBtn_', 'xBtn1__wUp_mBtn__', 'xBtn1__wUp_mBtn_',
              '_xBtn1__wUp_mBtn_', 'xBtn1¦2__', 'xBtn1¦2_', 'xBtn1¦2__lBtn__', 'xBtn1¦2__lBtn_', '_xBtn1¦2__lBtn_',
              'xBtn1¦2__lBtn_rBtn__', 'xBtn1¦2__lBtn_rBtn_', '_xBtn1¦2__lBtn_rBtn_', 'xBtn1¦2__lBtn_mBtn__',
              'xBtn1¦2__lBtn_mBtn_', '_xBtn1¦2__lBtn_mBtn_', 'xBtn1¦2__lBtn_wDown_', '_xBtn1¦2__lBtn_wDown_',
              'xBtn1¦2__lBtn_wUp_', '_xBtn1¦2__lBtn_wUp_', 'xBtn1¦2__rBtn__', 'xBtn1¦2__rBtn_', '_xBtn1¦2__rBtn_',
              'xBtn1¦2__rBtn_lBtn__', 'xBtn1¦2__rBtn_lBtn_', '_xBtn1¦2__rBtn_lBtn_', 'xBtn1¦2__rBtn_mBtn__',
              'xBtn1¦2__rBtn_mBtn_', '_xBtn1¦2__rBtn_mBtn_', 'xBtn1¦2__rBtn_wDown_', '_xBtn1¦2__rBtn_wDown_',
              'xBtn1¦2__rBtn_wUp_', '_xBtn1¦2__rBtn_wUp_', 'xBtn1¦2__mBtn__', 'xBtn1¦2__mBtn_', '_xBtn1¦2__mBtn_',
              'xBtn1¦2__mBtn_lBtn__', 'xBtn1¦2__mBtn_lBtn_', '_xBtn1¦2__mBtn_lBtn_', 'xBtn1¦2__mBtn_rBtn__',
              'xBtn1¦2__mBtn_rBtn_', '_xBtn1¦2__mBtn_rBtn_', 'xBtn1¦2__mBtn_wDown_', '_xBtn1¦2__mBtn_wDown_',
              'xBtn1¦2__mBtn_wUp_', '_xBtn1¦2__mBtn_wUp_', 'xBtn1¦2__wDown_', '_xBtn1¦2__wDown_',
              'xBtn1¦2__wDown_lBtn__', 'xBtn1¦2__wDown_lBtn_', '_xBtn1¦2__wDown_lBtn_', 'xBtn1¦2__wDown_rBtn__',
              'xBtn1¦2__wDown_rBtn_', '_xBtn1¦2__wDown_rBtn_', 'xBtn1¦2__wDown_mBtn__', 'xBtn1¦2__wDown_mBtn_',
              '_xBtn1¦2__wDown_mBtn_', 'xBtn1¦2__wUp_', '_xBtn1¦2__wUp_', 'xBtn1¦2__wUp_lBtn__', 'xBtn1¦2__wUp_lBtn_',
              '_xBtn1¦2__wUp_lBtn_', 'xBtn1¦2__wUp_rBtn__', 'xBtn1¦2__wUp_rBtn_', '_xBtn1¦2__wUp_rBtn_',
              'xBtn1¦2__wUp_mBtn__', 'xBtn1¦2__wUp_mBtn_', '_xBtn1¦2__wUp_mBtn_', 'xBtn2__', 'xBtn2_', 'xBtn2__lBtn__',
              'xBtn2__lBtn_', '_xBtn2__lBtn_', 'xBtn2__lBtn_xBtn1__', 'xBtn2__lBtn_xBtn1_', '_xBtn2__lBtn_xBtn1_',
              'xBtn2__lBtn_rBtn__', 'xBtn2__lBtn_rBtn_', '_xBtn2__lBtn_rBtn_', 'xBtn2__lBtn_mBtn__',
              'xBtn2__lBtn_mBtn_', '_xBtn2__lBtn_mBtn_', 'xBtn2__lBtn_wDown_', '_xBtn2__lBtn_wDown_',
              'xBtn2__lBtn_wUp_', '_xBtn2__lBtn_wUp_', 'xBtn2__rBtn__', 'xBtn2__rBtn_', '_xBtn2__rBtn_',
              'xBtn2__rBtn_xBtn1__', 'xBtn2__rBtn_xBtn1_', '_xBtn2__rBtn_xBtn1_', 'xBtn2__rBtn_lBtn__',
              'xBtn2__rBtn_lBtn_', '_xBtn2__rBtn_lBtn_', 'xBtn2__rBtn_mBtn__', 'xBtn2__rBtn_mBtn_',
              '_xBtn2__rBtn_mBtn_', 'xBtn2__rBtn_wDown_', '_xBtn2__rBtn_wDown_', 'xBtn2__rBtn_wUp_',
              '_xBtn2__rBtn_wUp_', 'xBtn2__mBtn__', 'xBtn2__mBtn_', '_xBtn2__mBtn_', 'xBtn2__mBtn_xBtn1__',
              'xBtn2__mBtn_xBtn1_', '_xBtn2__mBtn_xBtn1_', 'xBtn2__mBtn_lBtn__', 'xBtn2__mBtn_lBtn_',
              '_xBtn2__mBtn_lBtn_', 'xBtn2__mBtn_rBtn__', 'xBtn2__mBtn_rBtn_', '_xBtn2__mBtn_rBtn_',
              'xBtn2__mBtn_wDown_', '_xBtn2__mBtn_wDown_', 'xBtn2__mBtn_wUp_', '_xBtn2__mBtn_wUp_', 'xBtn2__wDown_',
              '_xBtn2__wDown_', 'xBtn2__wDown_xBtn1__', 'xBtn2__wDown_xBtn1_', '_xBtn2__wDown_xBtn1_',
              'xBtn2__wDown_lBtn__', 'xBtn2__wDown_lBtn_', '_xBtn2__wDown_lBtn_', 'xBtn2__wDown_rBtn__',
              'xBtn2__wDown_rBtn_', '_xBtn2__wDown_rBtn_', 'xBtn2__wDown_mBtn__', 'xBtn2__wDown_mBtn_',
              '_xBtn2__wDown_mBtn_', 'xBtn2__wUp_', '_xBtn2__wUp_', 'xBtn2__wUp_xBtn1__', 'xBtn2__wUp_xBtn1_',
              '_xBtn2__wUp_xBtn1_', 'xBtn2__wUp_lBtn__', 'xBtn2__wUp_lBtn_', '_xBtn2__wUp_lBtn_', 'xBtn2__wUp_rBtn__',
              'xBtn2__wUp_rBtn_', '_xBtn2__wUp_rBtn_', 'xBtn2__wUp_mBtn__', 'xBtn2__wUp_mBtn_', '_xBtn2__wUp_mBtn_',
              'lBtn__xBtn1__', 'lBtn__xBtn1_', '_lBtn__xBtn1_', 'lBtn__xBtn1_rBtn__', 'lBtn__xBtn1_rBtn_',
              '_lBtn__xBtn1_rBtn_', 'lBtn__xBtn1_mBtn__', 'lBtn__xBtn1_mBtn_', '_lBtn__xBtn1_mBtn_',
              'lBtn__xBtn1_wDown_', '_lBtn__xBtn1_wDown_', 'lBtn__xBtn1_wUp_', '_lBtn__xBtn1_wUp_', 'lBtn__xBtn2__',
              'lBtn__xBtn2_', '_lBtn__xBtn2_', 'lBtn__xBtn2_rBtn__', 'lBtn__xBtn2_rBtn_', '_lBtn__xBtn2_rBtn_',
              'lBtn__xBtn2_mBtn__', 'lBtn__xBtn2_mBtn_', '_lBtn__xBtn2_mBtn_', 'lBtn__xBtn2_wDown_',
              '_lBtn__xBtn2_wDown_', 'lBtn__xBtn2_wUp_', '_lBtn__xBtn2_wUp_', 'lBtn__rBtn__', 'lBtn__rBtn_',
              '_lBtn__rBtn_', 'lBtn__rBtn_xBtn1__', 'lBtn__rBtn_xBtn1_', '_lBtn__rBtn_xBtn1_', 'lBtn__rBtn_xBtn2__',
              'lBtn__rBtn_xBtn2_', '_lBtn__rBtn_xBtn2_', 'lBtn__rBtn_mBtn__', 'lBtn__rBtn_mBtn_', '_lBtn__rBtn_mBtn_',
              'lBtn__rBtn_wDown_', '_lBtn__rBtn_wDown_', 'lBtn__rBtn_wUp_', '_lBtn__rBtn_wUp_', 'lBtn__mBtn__',
              'lBtn__mBtn_', '_lBtn__mBtn_', 'lBtn__mBtn_xBtn1__', 'lBtn__mBtn_xBtn1_', '_lBtn__mBtn_xBtn1_',
              'lBtn__mBtn_xBtn2__', 'lBtn__mBtn_xBtn2_', '_lBtn__mBtn_xBtn2_', 'lBtn__mBtn_rBtn__', 'lBtn__mBtn_rBtn_',
              '_lBtn__mBtn_rBtn_', 'lBtn__mBtn_wDown_', '_lBtn__mBtn_wDown_', 'lBtn__mBtn_wUp_', '_lBtn__mBtn_wUp_',
              'lBtn__wDown_', '_lBtn__wDown_', 'lBtn__wDown_xBtn1__', 'lBtn__wDown_xBtn1_', '_lBtn__wDown_xBtn1_',
              'lBtn__wDown_xBtn2__', 'lBtn__wDown_xBtn2_', '_lBtn__wDown_xBtn2_', 'lBtn__wDown_rBtn__',
              'lBtn__wDown_rBtn_', '_lBtn__wDown_rBtn_', 'lBtn__wDown_mBtn__', 'lBtn__wDown_mBtn_',
              '_lBtn__wDown_mBtn_', 'lBtn__wUp_', '_lBtn__wUp_', 'lBtn__wUp_xBtn1__', 'lBtn__wUp_xBtn1_',
              '_lBtn__wUp_xBtn1_', 'lBtn__wUp_xBtn2__', 'lBtn__wUp_xBtn2_', '_lBtn__wUp_xBtn2_', 'lBtn__wUp_rBtn__',
              'lBtn__wUp_rBtn_', '_lBtn__wUp_rBtn_', 'lBtn__wUp_mBtn__', 'lBtn__wUp_mBtn_', '_lBtn__wUp_mBtn_',
              'rBtn__xBtn1__', 'rBtn__xBtn1_', '_rBtn__xBtn1_', 'rBtn__xBtn1_lBtn__', 'rBtn__xBtn1_lBtn_',
              '_rBtn__xBtn1_lBtn_', 'rBtn__xBtn1_mBtn__', 'rBtn__xBtn1_mBtn_', '_rBtn__xBtn1_mBtn_',
              'rBtn__xBtn1_wDown_', '_rBtn__xBtn1_wDown_', 'rBtn__xBtn1_wUp_', '_rBtn__xBtn1_wUp_', 'rBtn__xBtn2__',
              'rBtn__xBtn2_', '_rBtn__xBtn2_', 'rBtn__xBtn2_lBtn__', 'rBtn__xBtn2_lBtn_', '_rBtn__xBtn2_lBtn_',
              'rBtn__xBtn2_mBtn__', 'rBtn__xBtn2_mBtn_', '_rBtn__xBtn2_mBtn_', 'rBtn__xBtn2_wDown_',
              '_rBtn__xBtn2_wDown_', 'rBtn__xBtn2_wUp_', '_rBtn__xBtn2_wUp_', 'rBtn__lBtn__', 'rBtn__lBtn_',
              '_rBtn__lBtn_', 'rBtn__lBtn_xBtn1__', 'rBtn__lBtn_xBtn1_', '_rBtn__lBtn_xBtn1_', 'rBtn__lBtn_xBtn2__',
              'rBtn__lBtn_xBtn2_', '_rBtn__lBtn_xBtn2_', 'rBtn__lBtn_mBtn__', 'rBtn__lBtn_mBtn_', '_rBtn__lBtn_mBtn_',
              'rBtn__lBtn_wDown_', '_rBtn__lBtn_wDown_', 'rBtn__lBtn_wUp_', '_rBtn__lBtn_wUp_', 'rBtn__mBtn__',
              'rBtn__mBtn_', '_rBtn__mBtn_', 'rBtn__mBtn_xBtn1__', 'rBtn__mBtn_xBtn1_', '_rBtn__mBtn_xBtn1_',
              'rBtn__mBtn_xBtn2__', 'rBtn__mBtn_xBtn2_', '_rBtn__mBtn_xBtn2_', 'rBtn__mBtn_lBtn__', 'rBtn__mBtn_lBtn_',
              '_rBtn__mBtn_lBtn_', 'rBtn__mBtn_wDown_', '_rBtn__mBtn_wDown_', 'rBtn__mBtn_wUp_', '_rBtn__mBtn_wUp_',
              'rBtn__wDown_', '_rBtn__wDown_', 'rBtn__wDown_xBtn1__', 'rBtn__wDown_xBtn1_', '_rBtn__wDown_xBtn1_',
              'rBtn__wDown_xBtn2__', 'rBtn__wDown_xBtn2_', '_rBtn__wDown_xBtn2_', 'rBtn__wDown_lBtn__',
              'rBtn__wDown_lBtn_', '_rBtn__wDown_lBtn_', 'rBtn__wDown_mBtn__', 'rBtn__wDown_mBtn_',
              '_rBtn__wDown_mBtn_', 'rBtn__wUp_', '_rBtn__wUp_', 'rBtn__wUp_xBtn1__', 'rBtn__wUp_xBtn1_',
              '_rBtn__wUp_xBtn1_', 'rBtn__wUp_xBtn2__', 'rBtn__wUp_xBtn2_', '_rBtn__wUp_xBtn2_', 'rBtn__wUp_lBtn__',
              'rBtn__wUp_lBtn_', '_rBtn__wUp_lBtn_', 'rBtn__wUp_mBtn__', 'rBtn__wUp_mBtn_', '_rBtn__wUp_mBtn_']


def insert_combo():
    if '---' in menu_2.get() and '---' in menu_3.get():
        proposed_combo = f'{menu_1.get()}_'
    elif '---' not in [menu_2.get(), menu_3.get()]:
        proposed_combo = f'{menu_1.get()}__{menu_2.get()}_{menu_3.get()}_'
    elif '---' in menu_3.get():
        proposed_combo = f'{menu_1.get()}__{menu_2.get()}_'
    else:
        proposed_combo = ''

    if menu_0.get() == 'On hold':
        proposed_combo = proposed_combo + '_'
    elif menu_0.get() == 'On last release':
        proposed_combo = '_' + proposed_combo

    if proposed_combo in all_combos:
        # label_1.configure(text='')
        func = f'{proposed_combo}() {{\n    \n}}\n'
        if proposed_combo in editor_box.get('1.0', END):
            # label_1.configure(text='Combo already exists!', text_color='red')
            messagebox.showwarning(title=None, message='Combo already exists!')
        else:
            editor_box.insert('5.0', func)
            # dialog = customtkinter.CTkInputDialog(master=None, text=f'{proposed_combo}:', title='Configure')
            # print(f'{proposed_combo}() {dialog.get_input()}')
    else:
        # label_1.configure(text='Invalid combo!', text_color='red')
        messagebox.showerror(title=None, message='Invalid combo!')


# label_1 = customtkinter.CTkLabel(root, text='')
# label_1.grid(column=0, row=5, sticky="w")

insert_button = customtkinter.CTkButton(root, text="Insert", command=insert_combo, fg_color='green',
                                        hover_color='#006100')
# button.place(relx=0.5, rely=0.5, anchor=W)
insert_button.grid(padx=20, pady=0, column=0, row=6, sticky="w")

file_path = ''
tmp = ''
start = '#InstallKeybdHook\n#SingleInstance, Force\nSendMode Input\nSetWorkingDir, %A_ScriptDir%\n\n'
end = ';-----------------------------------------------------------------\n; Checks whether the active window is an exception\n;-----------------------------------------------------------------\nisException() {\n    WinGet, activeProcess, ProcessName, A\n    for index, value in exceptions\n        if (value = activeProcess)\n            return 1\n    return 0\n}\n\n;-----------------------------------------------------------------\n; Initializes variables\n;-----------------------------------------------------------------\ninitVar() {\n    ; Layer 1 is active when a (combo) function is executed on first release (by run_())\n    global isLayer1Active := 0\n    ; Reminder: A key is "used" as long as it has been engaged with\n    global xBtn1Used := xBtn2Used := lBtnUsed := rBtnUsed := mBtnUsed := wUpUsed := wDownUsed := 0\n    global xBtn1Count := xBtn2Count := lBtnCount := rBtnCount := wUpCount := wDownCount := 0\n}\n\n;-----------------------------------------------------------------\n; Execute functions responsible for combos\n;-----------------------------------------------------------------\nrun__(function) {\n    global funcName := function\n    %funcName%()\n}\n\nrun_(function="") {\n    global isLayer1Active := 1\n    global funcName\n    if (function) {\n        funcName := function\n    } else {\n        funcName := RegExReplace(funcName, "__$", "_")\n    }\n    %funcName%()\n}\n\n_run() {\n    for each, modifier in ["Ctrl", "LCtrl", "RCtrl", "Alt", "AltGr", "LAlt", "RAlt", "Shift", "LShift", "RShift", "Win", "LWin", "RWin"]\n        Send {%modifier% Up}\n    Send {Control}\n\n    global funcName\n    _%funcName%()\n}\n\n; ========================================= Main =========================================\n#if isException()\n    ~*XButton1::return\n    ~*XButton2::return\n    ~*LButton::return\n    ~*RButton::return\n    ~*MButton::return\n    ~*WheelUp::return\n    ~*WheelDown::return\n#if\n\n; ---------------------------------- XButton1/2 actions ----------------------------------\n#if _xBtn1Held\n    *XButton2::\n        global xBtn2Used := 1\n        global xBtn2Count ++\n\n        ; if (A_PriorKey = "LButton") {\n        ;     run__("xBtn1__lBtn_xBtn2__")\n        ; }      \n        ; else if (A_PriorKey = "RButton") {\n        ;     run__("xBtn1__rBtn_xBtn2__")\n        ; }\n        ; else if (A_PriorKey = "MButton") {\n        ;     run__("xBtn1__mBtn_xBtn2__")\n        ; }\n        ; else if (A_PriorKey = "WheelUp") {\n        ;     run__("xBtn1__wUp_xBtn2__")\n        ; }\n        ; else if (A_PriorKey = "WheelDown") {\n        ;     run__("xBtn1__wDown_xBtn2__")\n        ; }\n        ; else {\n            run__("xBtn1¦2__")\n        ; }\n        \n        KeyWait, XButton2\n        \n        if (isLayer1Active && A_PriorKey != "XButton2")\n            return\n\n        run_()\n    return\n\n    *LButton::\n        global lBtnUsed := 1\n        global lBtnCount ++\n\n        if (A_PriorKey = "XButton2") {\n            if (A_PriorKey = "RButton") {\n                run__("xBtn1¦2__rBtn_lBtn__")\n            }\n            else if (A_PriorKey = "MButton") {\n                run__("xBtn1¦2__mBtn_lBtn__")\n            }\n            else if (A_PriorKey = "WheelUp") {\n                run__("xBtn1¦2__wUp_lBtn__")\n            }\n            else if (A_PriorKey = "WheelDown") {\n                run__("xBtn1¦2__wDown_lBtn__")\n            }\n            else {\n                run__("xBtn1¦2__lBtn__")\n            }\n        }\n        else if (A_PriorKey = "RButton") {\n            run__("xBtn1__rBtn_lBtn__")\n        }\n        else if (A_PriorKey = "MButton") {\n            run__("xBtn1__mBtn_lBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("xBtn1__wUp_lBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("xBtn1__wDown_lBtn__")\n        }\n        else {\n            run__("xBtn1__lBtn__")\n        }\n\n        KeyWait, LButton\n\n        if (isLayer1Active && A_PriorKey != "LButton")\n            return\n\n        run_()\n    return\n\n    *RButton::\n        global rBtnUsed := 1\n        global rBtnCount ++\n\n        if (A_PriorKey = "XButton2") {\n            if (A_PriorKey = "LButton") {\n                run__("xBtn1¦2__lBtn_rBtn__")\n            }\n            else if (A_PriorKey = "MButton") {\n                run__("xBtn1¦2__mBtn_rBtn__")\n            }\n            else if (A_PriorKey = "WheelUp") {\n                run__("xBtn1¦2__wUp_rBtn__")\n            }\n            else if (A_PriorKey = "WheelDown") {\n                run__("xBtn1¦2__wDown_rBtn__")\n            }\n            else {\n                run__("xBtn1¦2__rBtn__")\n            }\n        }\n        else if (A_PriorKey = "LButton") {\n            run__("xBtn1__lBtn_rBtn__")\n        }\n        else if (A_PriorKey = "MButton") {\n            run__("xBtn1__mBtn_rBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("xBtn1__wUp_rBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("xBtn1__wDown_rBtn__")\n        }\n        else {\n            run__("xBtn1__rBtn__")\n        }\n\n        KeyWait, RButton\n\n        if (isLayer1Active && A_PriorKey != "RButton")\n            return\n\n        run_()\n    return\n\n    *MButton::\n        global mBtnUsed := 1\n        global mBtnCount ++\n\n        if (A_PriorKey = "XButton2") {\n            if (A_PriorKey = "LButton") {\n                run__("xBtn1¦2__lBtn_mBtn__")\n            }\n            else if (A_PriorKey = "RButton") {\n                run__("xBtn1¦2__rBtn_mBtn__")\n            }\n            else if (A_PriorKey = "WheelUp") {\n                run__("xBtn1¦2__wUp_mBtn__")\n            }\n            else if (A_PriorKey = "WheelDown") {\n                run__("xBtn1¦2__wDown_mBtn__")\n            }\n            else {\n                run__("xBtn1¦2__mBtn__")\n            }\n        }\n        else if (A_PriorKey = "LButton") {\n            run__("xBtn1__lBtn_mBtn__")\n        }   \n        else if (A_PriorKey = "RButton") {\n            run__("xBtn1__rBtn_mBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("xBtn1__wUp_mBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("xBtn1__wDown_mBtn__")\n        }\n        else {\n            run__("xBtn1__mBtn__")\n        }\n\n        KeyWait, MButton\n\n        if (isLayer1Active && A_PriorKey != "MButton")\n            return\n\n        run_()\n    return\n\n    *WheelUp::\n        global wUpUsed := 1\n        global wUpCount ++\n\n        if (A_PriorKey = "XButton2") {\n            if (A_PriorKey = "LButton") {\n                run_("xBtn1¦2__lBtn_wUp_")\n            }\n            else if (A_PriorKey = "RButton") {\n                run_("xBtn1¦2__rBtn_wUp_")\n            }\n            else if (A_PriorKey = "MButton") {\n                run_("xBtn1¦2__mBtn_wUp_")\n            }\n            else {\n                run_("xBtn1¦2__wUp_")\n            }\n        }\n        else if (A_PriorKey = "LButton") {\n            run_("xBtn1__lBtn_wUp_")\n        }\n        else if (A_PriorKey = "RButton") {\n            run_("xBtn1__rBtn_wUp_")\n        }\n        else if (A_PriorKey = "MButton") {\n            run_("xBtn1__mBtn_wUp_")\n        }\n        else {\n            run_("xBtn1__wUp_")\n        }\n    return\n\n    *WheelDown::\n        global wDownUsed := 1\n        global wDownCount ++\n\n        if (A_PriorKey = "XButton2") {\n            if (A_PriorKey = "LButton") {\n                run_("xBtn1¦2__lBtn_wDown_")\n            }\n            else if (A_PriorKey = "RButton") {\n                run_("xBtn1¦2__rBtn_wDown_")\n            }\n            else if (A_PriorKey = "MButton") {\n                run_("xBtn1¦2__mBtn_wDown_")\n            }\n            else {\n                run_("xBtn1¦2__wDown_")\n            }\n        }\n        else if (A_PriorKey = "LButton") {\n            run_("xBtn1__lBtn_wDown_")\n        }   \n        else if (A_PriorKey = "RButton") {\n            run_("xBtn1__rBtn_wDown_")\n        }\n        else if (A_PriorKey = "MButton") {\n            run_("xBtn1__mBtn_wDown_")\n        }\n        else {\n            run_("xBtn1__wDown_")\n        }\n    return\n#if\n\n#if _xBtn2Held\n    *XButton1::\n        global xBtn1Used := 1\n        global xBtn1Count ++\n\n        ; if (A_PriorKey = "LButton") {\n        ;     run__("xBtn2__lBtn_xBtn1__")\n        ; }      \n        ; else if (A_PriorKey = "RButton") {\n        ;     run__("xBtn2__rBtn_xBtn1__")\n        ; }\n        ; else if (A_PriorKey = "MButton") {\n        ;     run__("xBtn2__mBtn_xBtn1__")\n        ; }\n        ; else if (A_PriorKey = "WheelUp") {\n        ;     run__("xBtn2__wUp_xBtn1__")\n        ; }\n        ; else if (A_PriorKey = "WheelDown") {\n        ;     run__("xBtn2__wDown_xBtn1__")\n        ; }\n        ; else {\n            run__("xBtn1¦2__")\n        ; }\n\n        KeyWait, XButton1\n\n        if (isLayer1Active && A_PriorKey != "XButton1")\n            return\n\n        run_()\n    return\n    \n    *LButton::\n        global lBtnUsed := 1\n        global lBtnCount ++\n\n        if (A_PriorKey = "XButton1") {\n            if (A_PriorKey = "RButton") {\n                run__("xBtn1¦2__rBtn_lBtn__")\n            }\n            else if (A_PriorKey = "MButton") {\n                run__("xBtn1¦2__mBtn_lBtn__")\n            }\n            else if (A_PriorKey = "WheelUp") {\n                run__("xBtn1¦2__wUp_lBtn__")\n            }\n            else if (A_PriorKey = "WheelDown") {\n                run__("xBtn1¦2__wDown_lBtn__")\n            }\n            else {\n                run__("xBtn1¦2__lBtn__")\n            }\n        }\n        else if (A_PriorKey = "RButton") {\n            run__("xBtn2__rBtn_lBtn__")\n        }\n        else if (A_PriorKey = "MButton") {\n            run__("xBtn2__mBtn_lBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("xBtn2__wUp_lBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("xBtn2__wDown_lBtn__")\n        }\n        else {\n            run__("xBtn2__lBtn__")\n        }\n\n        KeyWait, LButton\n\n        if (isLayer1Active && A_PriorKey != "LButton")\n            return\n\n        run_()\n    return\n\n    *RButton::\n        global rBtnUsed := 1\n        global rBtnCount ++\n\n        if (A_PriorKey = "XButton1") {\n            if (A_PriorKey = "LButton") {\n                run__("xBtn1¦2__lBtn_rBtn__")\n            }\n            else if (A_PriorKey = "MButton") {\n                run__("xBtn1¦2__mBtn_rBtn__")\n            }\n            else if (A_PriorKey = "WheelUp") {\n                run__("xBtn1¦2__wUp_rBtn__")\n            }\n            else if (A_PriorKey = "WheelDown") {\n                run__("xBtn1¦2__wDown_rBtn__")\n            }\n            else {\n                run__("xBtn1¦2__rBtn__")\n            }\n        }\n        else if (A_PriorKey = "LButton") {\n            run__("xBtn2__lBtn_rBtn__")\n        }\n        else if (A_PriorKey = "MButton") {\n            run__("xBtn2__mBtn_rBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("xBtn2__wUp_rBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("xBtn2__wDown_rBtn__")\n        }\n        else {\n            run__("xBtn2__rBtn__")\n        }\n\n        KeyWait, RButton\n\n        if (isLayer1Active && A_PriorKey != "RButton")\n            return\n\n        run_()\n    return\n\n    *MButton::\n        global mBtnUsed := 1\n        global mBtnCount ++\n\n        if (A_PriorKey = "XButton1") {\n            if (A_PriorKey = "LButton") {\n                run__("xBtn1¦2__lBtn_mBtn__")\n            }\n            else if (A_PriorKey = "RButton") {\n                run__("xBtn1¦2__rBtn_mBtn__")\n            }\n            else if (A_PriorKey = "WheelUp") {\n                run__("xBtn1¦2__wUp_mBtn__")\n            }\n            else if (A_PriorKey = "WheelDown") {\n                run__("xBtn1¦2__wDown_mBtn__")\n            }\n            else {\n                run__("xBtn1¦2__mBtn__")\n            }\n        }\n        else if (A_PriorKey = "LButton") {\n            run__("xBtn2__lBtn_mBtn__")\n        }   \n        else if (A_PriorKey = "RButton") {\n            run__("xBtn2__rBtn_mBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("xBtn2__wUp_mBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("xBtn2__wDown_mBtn__")\n        }\n        else {\n            run__("xBtn2__mBtn__")\n        }\n\n        KeyWait, MButton\n\n        if (isLayer1Active && A_PriorKey != "MButton")\n            return\n\n        run_()\n    return\n\n    *WheelUp::\n        global wUpUsed := 1\n        global wUpCount ++\n\n        if (A_PriorKey = "XButton1") {\n            if (A_PriorKey = "LButton") {\n                run_("xBtn1¦2__lBtn_wUp_")\n            }\n            else if (A_PriorKey = "RButton") {\n                run_("xBtn1¦2__rBtn_wUp_")\n            }\n            else if (A_PriorKey = "MButton") {\n                run_("xBtn1¦2__mBtn_wUp_")\n            }\n            else {\n                run_("xBtn1¦2__wUp_")\n            }\n        }\n        else if (A_PriorKey = "LButton") {\n            run_("xBtn2__lBtn_wUp_")\n        }\n        else if (A_PriorKey = "RButton") {\n            run_("xBtn2__rBtn_wUp_")\n        }\n        else if (A_PriorKey = "MButton") {\n            run_("xBtn2__mBtn_wUp_")\n        }\n        else {\n            run_("xBtn2__wUp_")\n        }\n    return\n\n    *WheelDown::\n        global wDownUsed := 1\n        global wDownCount ++\n\n        if (A_PriorKey = "XButton1") {\n            if (A_PriorKey = "LButton") {\n                run_("xBtn1¦2__lBtn_wDown_")\n            }\n            else if (A_PriorKey = "RButton") {\n                run_("xBtn1¦2__rBtn_wDown_")\n            }\n            else if (A_PriorKey = "MButton") {\n                run_("xBtn1¦2__mBtn_wDown_")\n            }\n            else {\n                run_("xBtn1¦2__wDown_")\n            }\n        }\n        else if (A_PriorKey = "LButton") {\n            run_("xBtn2__lBtn_wDown_")\n        }   \n        else if (A_PriorKey = "RButton") {\n            run_("xBtn2__rBtn_wDown_")\n        }\n        else if (A_PriorKey = "MButton") {\n            run_("xBtn2__mBtn_wDown_")\n        }\n        else {\n            run_("xBtn2__wDown_")\n        }\n    return\n#if\n\n; ---------------------------------- L/RButton actions ----------------------------------\n#if _lBtnHeld\n    *XButton1::\n        global xBtn1Used := 1\n        global xBtn1Count ++\n\n        if (A_PriorKey = "RButton") {\n            run__("lBtn__rBtn_xBtn1__")\n        }\n        else if (A_PriorKey = "MButton") {\n            run__("lBtn__mBtn_xBtn1__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("lBtn__wUp_xBtn1__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("lBtn__wDown_xBtn1__")\n        }\n        else {\n            run__("lBtn__xBtn1__")\n        }\n\n        KeyWait, XButton1\n\n        if (isLayer1Active && A_PriorKey != "XButton1")\n            return\n\n        run_()\n    return\n\n    *XButton2::\n        global xBtn2Used := 1\n        global xBtn2Count ++\n\n        if (A_PriorKey = "RButton") {\n            run__("lBtn__rBtn_xBtn2__")\n        }\n        else if (A_PriorKey = "MButton") {\n            run__("lBtn__mBtn_xBtn2__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("lBtn__wUp_xBtn2__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("lBtn__wDown_xBtn2__")\n        }\n        else {\n            run__("lBtn__xBtn2__")\n        }\n        \n        KeyWait, XButton2\n\n        if (isLayer1Active && A_PriorKey != "XButton2")\n            return\n\n        run_()\n    return\n\n    *RButton::\n        global rBtnUsed := 1\n        global rBtnCount ++\n\n        if (A_PriorKey = "XButton1")  {\n            run__("lBtn__xBtn1_rBtn__")\n        }\n        else if (A_PriorKey = "XButton2")  {\n            run__("lBtn__xBtn2_rBtn__")\n        }\n        else if (A_PriorKey = "MButton")  {\n            run__("lBtn__mBtn_rBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("lBtn__wUp_rBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("lBtn__wDown_rBtn__")\n        }\n        else {\n            run__("lBtn__rBtn__")\n        }\n\n        KeyWait, RButton\n\n        if (isLayer1Active && A_PriorKey != "RButton")\n            return\n\n        run_()\n    return\n\n    *MButton::\n        global mBtnUsed := 1\n        global mBtnCount ++\n\n        if (A_PriorKey = "XButton1")  {\n            run__("lBtn__xBtn1_mBtn__")\n        }\n        else if (A_PriorKey = "XButton2")  {\n            run__("lBtn__xBtn2_mBtn__")\n        }\n        else if (A_PriorKey = "RButton")  {\n            run__("lBtn__rBtn_mBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("lBtn__wUp_mBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("lBtn__wDown_mBtn__")\n        }\n        else {\n            run__("lBtn__mBtn__")\n        }\n        \n        KeyWait, MButton\n\n        if (isLayer1Active && A_PriorKey != "MButton")\n            return\n\n        run_()\n    return\n\n    *WheelUp::\n        global wUpUsed := 1\n        global wUpCount ++\n\n        if (A_PriorKey = "XButton1") {\n            run_("lBtn__xBtn1_wUp_")\n        }\n        else if (A_PriorKey = "XButton2") {\n            run_("lBtn__xBtn2_wUp_")\n        }\n        else if (A_PriorKey = "RButton") {\n            run_("lBtn__rBtn_wUp_")\n        }\n        else if (A_PriorKey = "MButton")  {\n            run_("lBtn__mBtn_wUp_")\n        }\n        else {\n            run_("lBtn__wUp_")\n        }\n    return\n\n    *WheelDown::\n        global wDownUsed := 1\n        global wDownCount ++\n\n        if (A_PriorKey = "XButton1") {\n            run_("lBtn__xBtn1_wDown_")\n        }\n        else if (A_PriorKey = "XButton2") {\n            run_("lBtn__xBtn2_wDown_")\n        }\n        else if (A_PriorKey = "RButton") {\n            run_("lBtn__rBtn_wDown_")\n        }\n        else if (A_PriorKey = "MButton")  {\n            run_("lBtn__mBtn_wDown_")\n        }\n        else {\n            run_("lBtn__wDown_")\n        }\n    return\n#if\n\n#if _rBtnHeld\n    *XButton1::\n        global xBtn1Used := 1\n        global xBtn1Count ++\n\n        if (A_PriorKey = "LButton") {\n            msgbox % A_priorkey\n            run__("rBtn__lBtn_xBtn1__")\n        }\n        else if (A_PriorKey = "MButton") {\n            run__("rBtn__mBtn_xBtn1__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("rBtn__wUp_xBtn1__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("rBtn__wDown_xBtn1__")\n        }\n        else {\n            run__("rBtn__xBtn1__")\n        }\n\n        KeyWait, XButton1\n\n        if (isLayer1Active && A_PriorKey != "XButton1")\n            return\n\n        run_()\n    return\n\n    *XButton2::\n        global xBtn2Used := 1\n        global xBtn2Count ++\n\n        if (A_PriorKey = "LButton") {\n            run__("rBtn__lBtn_xBtn2__")\n        }\n        else if (A_PriorKey = "MButton") {\n            run__("rBtn__mBtn_xBtn2__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("rBtn__wUp_xBtn2__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("rBtn__wDown_xBtn2__")\n        }\n        else {\n            run__("rBtn__xBtn2__")\n        }\n\n        KeyWait, XButton2\n\n        if (isLayer1Active && A_PriorKey != "XButton2")\n            return\n\n        run_()\n    return\n\n    *LButton::\n        global lBtnUsed := 1\n        global lBtnCount ++\n\n        if (A_PriorKey = "XButton1")  {\n            run__("rBtn__xBtn1_lBtn__")\n        }\n        else if (A_PriorKey = "XButton2")  {\n            run__("rBtn__xBtn2_lBtn__")\n        }\n        else if (A_PriorKey = "MButton")  {\n            run__("rBtn__mBtn_lBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("rBtn__wUp_lBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("rBtn__wDown_lBtn__")\n        }\n        else {\n            run__("rBtn__lBtn__")\n        }\n\n        KeyWait, LButton\n\n        if (isLayer1Active && A_PriorKey != "LButton")\n            return\n\n        run_()\n    return\n\n    *MButton::\n        global mBtnUsed := 1\n        global mBtnCount ++\n\n        if (A_PriorKey = "XButton1")  {\n            run__("rBtn__xBtn1_mBtn__")\n        }\n        else if (A_PriorKey = "XButton2")  {\n            run__("rBtn__xBtn2_mBtn__")\n        }\n        else if (A_PriorKey = "LButton")  {\n            run__("rBtn__lBtn_mBtn__")\n        }\n        else if (A_PriorKey = "WheelUp") {\n            run__("rBtn__wUp_mBtn__")\n        }\n        else if (A_PriorKey = "WheelDown") {\n            run__("rBtn__wDown_mBtn__")\n        }\n        else {\n            run__("rBtn__mBtn__")\n        }\n\n        KeyWait, MButton\n\n        if (isLayer1Active && A_PriorKey != "MButton")\n            return\n\n        run_()\n    return\n\n    *WheelUp::\n        global wUpUsed := 1\n        global wUpCount ++\n\n        if (A_PriorKey = "XButton1") {\n            run_("rBtn__xBtn1_wUp_")\n        }\n        else if (A_PriorKey = "XButton2") {\n            run_("rBtn__xBtn2_wUp_")\n        }\n        else if (A_PriorKey = "LButton") {\n            run_("rBtn__lBtn_wUp_")\n        }\n        else if (A_PriorKey = "MButton")  {\n            run_("rBtn__mBtn_wUp_")\n        }\n        else {\n            run_("rBtn__wUp_")\n        }\n    return\n\n    *WheelDown::\n        global wDownUsed := 1\n        global wDownCount ++\n\n        if (A_PriorKey = "XButton1") {\n            run_("rBtn__xBtn1_wDown_")\n        }\n        else if (A_PriorKey = "XButton2") {\n            run_("rBtn__xBtn2_wDown_")\n        }\n        else if (A_PriorKey = "LButton") {\n            run_("rBtn__lBtn_wDown_")\n        }\n        else if (A_PriorKey = "MButton")  {\n            run_("rBtn__mBtn_wDown_")\n        }\n        else {\n            run_("rBtn__wDown_")\n        }\n    return\n#if\n\n; -------------------------------------- XButton1/2 --------------------------------------\n#if (!GetKeyState("LButton", "P") && !GetKeyState("RButton", "P"))\n    *XButton1::\n        initVar()\n\n        run__("xBtn1__")\n        \n        ; To activate #if blocks\n        _xBtn1Held := 1\n        KeyWait, XButton1\n        _xBtn1Held := 0\n\n        ; Restore/Customize normal functionality if used merely as a key\n        if (xBtn1Used + xBtn2Used + lBtnUsed + rBtnUsed + mBtnUsed + wUpUsed + wDownUsed = 0) {\n            run_()\n            return\n        }\n        \n        _run()\n    return\n\n    *XButton2::\n        initVar()\n\n        run__("xBtn2__")\n\n        _xBtn2Held := 1\n        KeyWait, XButton2\n        _xBtn2Held := 0\n\n        if (!isLayer1Active) {\n            run_()\n            return\n        }\n\n        _run()\n    return\n#if\n\n; -------------------------------------- L/RButton --------------------------------------\n#if (!GetKeyState("XButton1", "P") && !GetKeyState("XButton2", "P"))\n    ~*LButton::\n        initVar()\n\n        _lBtnHeld := 1\n        KeyWait, LButton\n        _lBtnHeld := 0\n\n        if (!isLayer1Active)\n            return\n\n        _run()\n    return\n\n    *RButton::\n        initVar()\n\n        _rBtnHeld := 1\n        KeyWait, RButton\n        _rBtnHeld := 0\n\n        if (!isLayer1Active) {\n            Send {RButton}\n            return\n        }\n\n        _run()\n    return\n#if\n\n; --------------------------------------- MButton ---------------------------------------\n#if (!GetKeyState("LButton", "P") && !GetKeyState("RButton", "P") && !GetKeyState("XButton1", "P") && !GetKeyState("XButton2", "P"))\n    ~MButton::\n    return\n#if\n\n; =========================================================================================\n; ========================================== END ==========================================\n; ========================================================================================='

def save():
    global file_path
    Files = [('AutoHotkey', '*.ahk')]
    file_path = filedialog.asksaveasfilename(filetypes=Files, defaultextension=Files)
    if file_path:
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(start + editor_box.get('1.0', END) + end)


save_button = customtkinter.CTkButton(root, text='Save as...', command=lambda: save(), fg_color='brown',
                                      hover_color='#831717')
save_button.grid(padx=20, pady=0, column=0, row=7, sticky="w")

# button = customtkinter.CTkButton(root, text='Run', command=run_ahk)
# button.grid(padx=20, pady=0, column=0, row=8, sticky="w")

switch_var = customtkinter.StringVar(value="off")


def switch_event():
    global tmp
    if switch_var.get() == 'on':
        tmp = tempfile.NamedTemporaryFile()
        with open(f'{tmp.name}.ahk', "w", encoding='utf-8') as f:
            f.write(start + editor_box.get('1.0', END) + end)
            subprocess.Popen(f'{tmp.name}.ahk', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    else:
        file_name = tmp.name.rsplit('\\', 1)[-1]
        subprocess.run(["powershell", "-windowstyle", "hidden", "-Command",
                        f'wmic process where "commandline like \'%%{file_name}.ahk%%\'" delete'])


switch_1 = customtkinter.CTkSwitch(master=root, text="Test script?", command=switch_event,
                                   variable=switch_var, onvalue="on", offvalue="off")
switch_1.grid(padx=20, pady=10, column=0, row=10, sticky="w")

editor_box = Text(root, width=98, height=37, bg="white", highlightthickness=.25, foreground="grey",
                  insertbackground="white", wrap="word")
editor_box.insert('0.0', '; ====================================== Exceptions ======================================\nglobal exceptions := ["csgo.exe", "r5apex.exe", "rainbowsix.exe"]\n\n; ======================================= Functions =======================================\nxBtn1_() {\n    if WinActive("ahk_exe Acrobat.exe") {\n        Send {LAlt down}{Left}{LAlt up}\n    }\n    else {\n        Send {XButton1}\n    }\n}\nxBtn1¦2__() {\n    Send {MButton down}\n    KeyWait, XButton2\n    Send {MButton up}\n}\nxBtn2_() {\n    if WinActive("ahk_exe Acrobat.exe") {\n        Send {LAlt down}{Right}{LAlt up}\n    }\n    else {\n        Send {XButton2}\n    }\n}\nlBtn__wUp_() {\n    Send {WheelUp}\n}\nlBtn__wDown_() {\n    Send {WheelDown}\n}\nrBtn__xBtn1__() {\n    Send !{Tab}\n}\nrBtn__xBtn1_wUp_() {\n    rBtn__wUp_()\n}\n_rBtn__xBtn1_wUp_() {\n    _rBtn__wUp_()\n}\nrBtn__xBtn1_wDown_() {\n    rBtn__wDown_()\n}\n_rBtn__xBtn1_wDown_() {\n    _rBtn__wDown_()\n}\nrBtn__wUp_() {\n    Send ^!+{tab}\n}\n_rBtn__wUp_() {\n    Send {Enter}\n}\nrBtn__wDown_() {\n    Send ^!{Tab}\n}\n_rBtn__wDown_() {\n    Send {Enter}\n}\n\n; --------------------------------------- Helpers ---------------------------------------')
editor_box.config(foreground="beige", background='#212325', font=("Consolas", 12))

# syntax highlighter patterns
KEYWORD = r"\b(?P<KEYWORD>if|else|Break|Continue|Critical|Exit|ExitApp|Gosub|Goto|New|OnExit|Pause|return|SetBatchLines|SetTimer|Suspend|Thread|Throw|Until|ahk_id|ahk_class|ahk_pid|ahk_exe|ahk_group)\b"
EXCEPTION = r"([^.'\"\\]\b|^)(?P<EXCEPTION>ArithmeticError|AssertionError|AttributeError|BaseException|BlockingIOError|BrokenPipeError|BufferError|BytesWarning|ChildProcessError|ConnectionAbortedError|ConnectionError|ConnectionRefusedError|ConnectionResetError|DeprecationWarning|EOFError|Ellipsis|EnvironmentError|Exception|FileExistsError|FileNotFoundError|FloatingPointError|FutureWarning|GeneratorExit|IOError|ImportError|ImportWarning|IndentationError|IndexError|InterruptedError|IsADirectoryError|KeyError|KeyboardInterrupt|LookupError|MemoryError|ModuleNotFoundError|NameError|NotADirectoryError|NotImplemented|NotImplementedError|OSError|OverflowError|PendingDeprecationWarning|PermissionError|ProcessLookupError|RecursionError|ReferenceError|ResourceWarning|RuntimeError|RuntimeWarning|StopAsyncIteration|StopIteration|SyntaxError|SyntaxWarning|SystemError|SystemExit|TabError|TimeoutError|TypeError|UnboundLocalError|UnicodeDecodeError|UnicodeEncodeError|UnicodeError|UnicodeTranslateError|UnicodeWarning|UserWarning|ValueError|Warning|WindowsError|ZeroDivisionError)\b"
BUILTIN = r"([^.'\"\\#]\b|^)(?P<BUILTIN>ComSpec|Clipboard|ClipboardAll|ErrorLevel)\b"
DOCSTRING = r"(?P<DOCSTRING>(?i:r|u|f|fr|rf|b|br|rb)?'''[^'\\]*((\\.|'(?!''))[^'\\]*)*(''')?|(?i:r|u|f|fr|rf|b|br|rb)?\"\"\"[^\"\\]*((\\.|\"(?!\"\"))[^\"\\]*)*(\"\"\")?)"
STRING = r"(?P<STRING>(?i:r|u|f|fr|rf|b|br|rb)?'[^'\\\n]*(\\.[^'\\\n]*)*'?|(?i:r|u|f|fr|rf|b|br|rb)?\"[^\"\\\n]*(\\.[^\"\\\n]*)*\"?)"
TYPES = r"\b(?P<TYPES>bool|bytearray|bytes|dict|float|int|list|str|tuple|object)\b"
NUMBER = r"\b(?P<NUMBER>((0x|0b|0o|#)[\da-fA-F]+)|((\d*\.)?\d+))\b"
CLASSDEF = r"(?<=\bclass)[ \t]+(?P<CLASSDEF>\w+)[ \t]*[:\(]"  # recolor of DEFINITION for class definitions
DECORATOR = r"(^[ \t]*(?P<DECORATOR>@[\w\d\.]+))"
INSTANCE = r"\b(?P<INSTANCE>super|self|cls)\b"
COMMENT = r"(?P<COMMENT>;[^\n]*)"
SYNC = r"(?P<SYNC>\n)"

PROG = rf"{KEYWORD}|{BUILTIN}|{EXCEPTION}|{TYPES}|{COMMENT}|{DOCSTRING}|{STRING}|{SYNC}|{INSTANCE}|{DECORATOR}|{NUMBER}|{CLASSDEF}"

IDPROG = r"\s+(\w+)"
# IDPROG = r"(?<!class)\s+(\w+)"

TAGDEFS = {'COMMENT': {'foreground': '#7F7F7F', 'background': None},
           'TYPES': {'foreground': '#8CDCF0', 'background': None},
           'NUMBER': {'foreground': '#007F00', 'background': None},
           'BUILTIN': {'foreground': '#7F7F00', 'background': None},
           'STRING': {'foreground': '#CE9178', 'background': None},
           'DOCSTRING': {'foreground': '#007F7F', 'background': None},
           'EXCEPTION': {'foreground': '#007F7F', 'background': None},
           'DEFINITION': {'foreground': '#007F7F', 'background': None},
           'DECORATOR': {'foreground': '#007F7F', 'background': None},
           'INSTANCE': {'foreground': '#007F7F', 'background': None},
           'KEYWORD': {'foreground': '#007F7F', 'background': None},
           'CLASSDEF': {'foreground': '#007F7F', 'background': None},
           }

cd = ic.ColorDelegator()
cd.prog = re.compile(PROG, re.S | re.M)
cd.idprog = re.compile(IDPROG, re.S)
cd.tagdefs = {**cd.tagdefs, **TAGDEFS}
ip.Percolator(editor_box).insertfilter(cd)

'''
#what literally happens to this data when it is applied
for tag, cfg in self.tagdefs.items():
    self.tag_configure(tag, **cfg)
'''

cd.tagdefs = {**cd.tagdefs, **TAGDEFS}

tex_scroll = customtkinter.CTkScrollbar(root, command=editor_box.yview)
# tex_scroll.config(command=text_box.yview, )
editor_box["yscrollcommand"] = tex_scroll.set

editor_box.grid(column=1, row=1, rowspan=10, sticky="e", padx=0, pady=6)
tex_scroll.grid(column=3, row=1, rowspan=10, sticky="nse")

root.mainloop()
