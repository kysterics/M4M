#InstallKeybdHook
#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

; ====================================== Exceptions ======================================
global exceptions := ["csgo.exe", "r5apex.exe", "rainbowsix.exe"]

; ======================================= Functions =======================================
xBtn1_() {
    if WinActive("ahk_exe Acrobat.exe") {
        Send {LAlt down}{Left}{LAlt up}
    }
    else {
        Send {XButton1}
    }
}
xBtn1¦2__() {
    Send {MButton down}
    KeyWait, XButton2
    Send {MButton up}
}
xBtn2_() {
    if WinActive("ahk_exe Acrobat.exe") {
        Send {LAlt down}{Right}{LAlt up}
    }
    else {
        Send {XButton2}
    }
}
lBtn__wUp_() {
    Send {WheelUp}
}
lBtn__wDown_() {
    Send {WheelDown}
}
rBtn__xBtn1__() {
    Send !{Tab}
}
rBtn__xBtn1_wUp_() {
    rBtn__wUp_()
}
_rBtn__xBtn1_wUp_() {
    _rBtn__wUp_()
}
rBtn__xBtn1_wDown_() {
    rBtn__wDown_()
}
_rBtn__xBtn1_wDown_() {
    _rBtn__wDown_()
}
rBtn__wUp_() {
    Send ^!+{tab}
}
_rBtn__wUp_() {
    Send {Enter}
}
rBtn__wDown_() {
    Send ^!{Tab}
}
_rBtn__wDown_() {
    Send {Enter}
}

; --------------------------------------- Helpers ---------------------------------------
;-----------------------------------------------------------------
; Checks whether the active window is an exception
;-----------------------------------------------------------------
isException() {
    WinGet, activeProcess, ProcessName, A
    for index, value in exceptions
        if (value = activeProcess)
            return 1
    return 0
}

;-----------------------------------------------------------------
; Initializes variables
;-----------------------------------------------------------------
initVar() {
    ; Layer 1 is active when a (combo) function is executed on first release (by run_())
    global isLayer1Active := 0
    ; Reminder: A key is "used" as long as it has been engaged with
    global xBtn1Used := xBtn2Used := lBtnUsed := rBtnUsed := mBtnUsed := wUpUsed := wDownUsed := 0
    global xBtn1Count := xBtn2Count := lBtnCount := rBtnCount := wUpCount := wDownCount := 0
}

;-----------------------------------------------------------------
; Execute functions responsible for combos
;-----------------------------------------------------------------
run__(function) {
    global funcName := function
    %funcName%()
}

run_(function="") {
    global isLayer1Active := 1
    global funcName
    if (function) {
        funcName := function
    } else {
        funcName := RegExReplace(funcName, "__$", "_")
    }
    %funcName%()
}

_run() {
    for each, modifier in ["Ctrl", "LCtrl", "RCtrl", "Alt", "AltGr", "LAlt", "RAlt", "Shift", "LShift", "RShift", "Win", "LWin", "RWin"]
        Send {%modifier% Up}
    Send {Control}

    global funcName
    _%funcName%()
}

; ========================================= Main =========================================
#if isException()
    ~*XButton1::return
    ~*XButton2::return
    ~*LButton::return
    ~*RButton::return
    ~*MButton::return
    ~*WheelUp::return
    ~*WheelDown::return
#if

; ---------------------------------- XButton1/2 actions ----------------------------------
#if _xBtn1Held
    *XButton2::
        global xBtn2Used := 1
        global xBtn2Count ++

        ; if (A_PriorKey = "LButton") {
        ;     run__("xBtn1__lBtn_xBtn2__")
        ; }      
        ; else if (A_PriorKey = "RButton") {
        ;     run__("xBtn1__rBtn_xBtn2__")
        ; }
        ; else if (A_PriorKey = "MButton") {
        ;     run__("xBtn1__mBtn_xBtn2__")
        ; }
        ; else if (A_PriorKey = "WheelUp") {
        ;     run__("xBtn1__wUp_xBtn2__")
        ; }
        ; else if (A_PriorKey = "WheelDown") {
        ;     run__("xBtn1__wDown_xBtn2__")
        ; }
        ; else {
            run__("xBtn1¦2__")
        ; }
        
        KeyWait, XButton2
        
        if (isLayer1Active && A_PriorKey != "XButton2")
            return

        run_()
    return

    *LButton::
        global lBtnUsed := 1
        global lBtnCount ++

        if (A_PriorKey = "XButton2") {
            if (A_PriorKey = "RButton") {
                run__("xBtn1¦2__rBtn_lBtn__")
            }
            else if (A_PriorKey = "MButton") {
                run__("xBtn1¦2__mBtn_lBtn__")
            }
            else if (A_PriorKey = "WheelUp") {
                run__("xBtn1¦2__wUp_lBtn__")
            }
            else if (A_PriorKey = "WheelDown") {
                run__("xBtn1¦2__wDown_lBtn__")
            }
            else {
                run__("xBtn1¦2__lBtn__")
            }
        }
        else if (A_PriorKey = "RButton") {
            run__("xBtn1__rBtn_lBtn__")
        }
        else if (A_PriorKey = "MButton") {
            run__("xBtn1__mBtn_lBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("xBtn1__wUp_lBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("xBtn1__wDown_lBtn__")
        }
        else {
            run__("xBtn1__lBtn__")
        }

        KeyWait, LButton

        if (isLayer1Active && A_PriorKey != "LButton")
            return

        run_()
    return

    *RButton::
        global rBtnUsed := 1
        global rBtnCount ++

        if (A_PriorKey = "XButton2") {
            if (A_PriorKey = "LButton") {
                run__("xBtn1¦2__lBtn_rBtn__")
            }
            else if (A_PriorKey = "MButton") {
                run__("xBtn1¦2__mBtn_rBtn__")
            }
            else if (A_PriorKey = "WheelUp") {
                run__("xBtn1¦2__wUp_rBtn__")
            }
            else if (A_PriorKey = "WheelDown") {
                run__("xBtn1¦2__wDown_rBtn__")
            }
            else {
                run__("xBtn1¦2__rBtn__")
            }
        }
        else if (A_PriorKey = "LButton") {
            run__("xBtn1__lBtn_rBtn__")
        }
        else if (A_PriorKey = "MButton") {
            run__("xBtn1__mBtn_rBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("xBtn1__wUp_rBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("xBtn1__wDown_rBtn__")
        }
        else {
            run__("xBtn1__rBtn__")
        }

        KeyWait, RButton

        if (isLayer1Active && A_PriorKey != "RButton")
            return

        run_()
    return

    *MButton::
        global mBtnUsed := 1
        global mBtnCount ++

        if (A_PriorKey = "XButton2") {
            if (A_PriorKey = "LButton") {
                run__("xBtn1¦2__lBtn_mBtn__")
            }
            else if (A_PriorKey = "RButton") {
                run__("xBtn1¦2__rBtn_mBtn__")
            }
            else if (A_PriorKey = "WheelUp") {
                run__("xBtn1¦2__wUp_mBtn__")
            }
            else if (A_PriorKey = "WheelDown") {
                run__("xBtn1¦2__wDown_mBtn__")
            }
            else {
                run__("xBtn1¦2__mBtn__")
            }
        }
        else if (A_PriorKey = "LButton") {
            run__("xBtn1__lBtn_mBtn__")
        }   
        else if (A_PriorKey = "RButton") {
            run__("xBtn1__rBtn_mBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("xBtn1__wUp_mBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("xBtn1__wDown_mBtn__")
        }
        else {
            run__("xBtn1__mBtn__")
        }

        KeyWait, MButton

        if (isLayer1Active && A_PriorKey != "MButton")
            return

        run_()
    return

    *WheelUp::
        global wUpUsed := 1
        global wUpCount ++

        if (A_PriorKey = "XButton2") {
            if (A_PriorKey = "LButton") {
                run_("xBtn1¦2__lBtn_wUp_")
            }
            else if (A_PriorKey = "RButton") {
                run_("xBtn1¦2__rBtn_wUp_")
            }
            else if (A_PriorKey = "MButton") {
                run_("xBtn1¦2__mBtn_wUp_")
            }
            else {
                run_("xBtn1¦2__wUp_")
            }
        }
        else if (A_PriorKey = "LButton") {
            run_("xBtn1__lBtn_wUp_")
        }
        else if (A_PriorKey = "RButton") {
            run_("xBtn1__rBtn_wUp_")
        }
        else if (A_PriorKey = "MButton") {
            run_("xBtn1__mBtn_wUp_")
        }
        else {
            run_("xBtn1__wUp_")
        }
    return

    *WheelDown::
        global wDownUsed := 1
        global wDownCount ++

        if (A_PriorKey = "XButton2") {
            if (A_PriorKey = "LButton") {
                run_("xBtn1¦2__lBtn_wDown_")
            }
            else if (A_PriorKey = "RButton") {
                run_("xBtn1¦2__rBtn_wDown_")
            }
            else if (A_PriorKey = "MButton") {
                run_("xBtn1¦2__mBtn_wDown_")
            }
            else {
                run_("xBtn1¦2__wDown_")
            }
        }
        else if (A_PriorKey = "LButton") {
            run_("xBtn1__lBtn_wDown_")
        }   
        else if (A_PriorKey = "RButton") {
            run_("xBtn1__rBtn_wDown_")
        }
        else if (A_PriorKey = "MButton") {
            run_("xBtn1__mBtn_wDown_")
        }
        else {
            run_("xBtn1__wDown_")
        }
    return
#if

#if _xBtn2Held
    *XButton1::
        global xBtn1Used := 1
        global xBtn1Count ++

        ; if (A_PriorKey = "LButton") {
        ;     run__("xBtn2__lBtn_xBtn1__")
        ; }      
        ; else if (A_PriorKey = "RButton") {
        ;     run__("xBtn2__rBtn_xBtn1__")
        ; }
        ; else if (A_PriorKey = "MButton") {
        ;     run__("xBtn2__mBtn_xBtn1__")
        ; }
        ; else if (A_PriorKey = "WheelUp") {
        ;     run__("xBtn2__wUp_xBtn1__")
        ; }
        ; else if (A_PriorKey = "WheelDown") {
        ;     run__("xBtn2__wDown_xBtn1__")
        ; }
        ; else {
            run__("xBtn1¦2__")
        ; }

        KeyWait, XButton1

        if (isLayer1Active && A_PriorKey != "XButton1")
            return

        run_()
    return
    
    *LButton::
        global lBtnUsed := 1
        global lBtnCount ++

        if (A_PriorKey = "XButton1") {
            if (A_PriorKey = "RButton") {
                run__("xBtn1¦2__rBtn_lBtn__")
            }
            else if (A_PriorKey = "MButton") {
                run__("xBtn1¦2__mBtn_lBtn__")
            }
            else if (A_PriorKey = "WheelUp") {
                run__("xBtn1¦2__wUp_lBtn__")
            }
            else if (A_PriorKey = "WheelDown") {
                run__("xBtn1¦2__wDown_lBtn__")
            }
            else {
                run__("xBtn1¦2__lBtn__")
            }
        }
        else if (A_PriorKey = "RButton") {
            run__("xBtn2__rBtn_lBtn__")
        }
        else if (A_PriorKey = "MButton") {
            run__("xBtn2__mBtn_lBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("xBtn2__wUp_lBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("xBtn2__wDown_lBtn__")
        }
        else {
            run__("xBtn2__lBtn__")
        }

        KeyWait, LButton

        if (isLayer1Active && A_PriorKey != "LButton")
            return

        run_()
    return

    *RButton::
        global rBtnUsed := 1
        global rBtnCount ++

        if (A_PriorKey = "XButton1") {
            if (A_PriorKey = "LButton") {
                run__("xBtn1¦2__lBtn_rBtn__")
            }
            else if (A_PriorKey = "MButton") {
                run__("xBtn1¦2__mBtn_rBtn__")
            }
            else if (A_PriorKey = "WheelUp") {
                run__("xBtn1¦2__wUp_rBtn__")
            }
            else if (A_PriorKey = "WheelDown") {
                run__("xBtn1¦2__wDown_rBtn__")
            }
            else {
                run__("xBtn1¦2__rBtn__")
            }
        }
        else if (A_PriorKey = "LButton") {
            run__("xBtn2__lBtn_rBtn__")
        }
        else if (A_PriorKey = "MButton") {
            run__("xBtn2__mBtn_rBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("xBtn2__wUp_rBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("xBtn2__wDown_rBtn__")
        }
        else {
            run__("xBtn2__rBtn__")
        }

        KeyWait, RButton

        if (isLayer1Active && A_PriorKey != "RButton")
            return

        run_()
    return

    *MButton::
        global mBtnUsed := 1
        global mBtnCount ++

        if (A_PriorKey = "XButton1") {
            if (A_PriorKey = "LButton") {
                run__("xBtn1¦2__lBtn_mBtn__")
            }
            else if (A_PriorKey = "RButton") {
                run__("xBtn1¦2__rBtn_mBtn__")
            }
            else if (A_PriorKey = "WheelUp") {
                run__("xBtn1¦2__wUp_mBtn__")
            }
            else if (A_PriorKey = "WheelDown") {
                run__("xBtn1¦2__wDown_mBtn__")
            }
            else {
                run__("xBtn1¦2__mBtn__")
            }
        }
        else if (A_PriorKey = "LButton") {
            run__("xBtn2__lBtn_mBtn__")
        }   
        else if (A_PriorKey = "RButton") {
            run__("xBtn2__rBtn_mBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("xBtn2__wUp_mBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("xBtn2__wDown_mBtn__")
        }
        else {
            run__("xBtn2__mBtn__")
        }

        KeyWait, MButton

        if (isLayer1Active && A_PriorKey != "MButton")
            return

        run_()
    return

    *WheelUp::
        global wUpUsed := 1
        global wUpCount ++

        if (A_PriorKey = "XButton1") {
            if (A_PriorKey = "LButton") {
                run_("xBtn1¦2__lBtn_wUp_")
            }
            else if (A_PriorKey = "RButton") {
                run_("xBtn1¦2__rBtn_wUp_")
            }
            else if (A_PriorKey = "MButton") {
                run_("xBtn1¦2__mBtn_wUp_")
            }
            else {
                run_("xBtn1¦2__wUp_")
            }
        }
        else if (A_PriorKey = "LButton") {
            run_("xBtn2__lBtn_wUp_")
        }
        else if (A_PriorKey = "RButton") {
            run_("xBtn2__rBtn_wUp_")
        }
        else if (A_PriorKey = "MButton") {
            run_("xBtn2__mBtn_wUp_")
        }
        else {
            run_("xBtn2__wUp_")
        }
    return

    *WheelDown::
        global wDownUsed := 1
        global wDownCount ++

        if (A_PriorKey = "XButton1") {
            if (A_PriorKey = "LButton") {
                run_("xBtn1¦2__lBtn_wDown_")
            }
            else if (A_PriorKey = "RButton") {
                run_("xBtn1¦2__rBtn_wDown_")
            }
            else if (A_PriorKey = "MButton") {
                run_("xBtn1¦2__mBtn_wDown_")
            }
            else {
                run_("xBtn1¦2__wDown_")
            }
        }
        else if (A_PriorKey = "LButton") {
            run_("xBtn2__lBtn_wDown_")
        }   
        else if (A_PriorKey = "RButton") {
            run_("xBtn2__rBtn_wDown_")
        }
        else if (A_PriorKey = "MButton") {
            run_("xBtn2__mBtn_wDown_")
        }
        else {
            run_("xBtn2__wDown_")
        }
    return
#if

; ---------------------------------- L/RButton actions ----------------------------------
#if _lBtnHeld
    *XButton1::
        global xBtn1Used := 1
        global xBtn1Count ++

        if (A_PriorKey = "RButton") {
            run__("lBtn__rBtn_xBtn1__")
        }
        else if (A_PriorKey = "MButton") {
            run__("lBtn__mBtn_xBtn1__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("lBtn__wUp_xBtn1__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("lBtn__wDown_xBtn1__")
        }
        else {
            run__("lBtn__xBtn1__")
        }

        KeyWait, XButton1

        if (isLayer1Active && A_PriorKey != "XButton1")
            return

        run_()
    return

    *XButton2::
        global xBtn2Used := 1
        global xBtn2Count ++

        if (A_PriorKey = "RButton") {
            run__("lBtn__rBtn_xBtn2__")
        }
        else if (A_PriorKey = "MButton") {
            run__("lBtn__mBtn_xBtn2__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("lBtn__wUp_xBtn2__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("lBtn__wDown_xBtn2__")
        }
        else {
            run__("lBtn__xBtn2__")
        }
        
        KeyWait, XButton2

        if (isLayer1Active && A_PriorKey != "XButton2")
            return

        run_()
    return

    *RButton::
        global rBtnUsed := 1
        global rBtnCount ++

        if (A_PriorKey = "XButton1")  {
            run__("lBtn__xBtn1_rBtn__")
        }
        else if (A_PriorKey = "XButton2")  {
            run__("lBtn__xBtn2_rBtn__")
        }
        else if (A_PriorKey = "MButton")  {
            run__("lBtn__mBtn_rBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("lBtn__wUp_rBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("lBtn__wDown_rBtn__")
        }
        else {
            run__("lBtn__rBtn__")
        }

        KeyWait, RButton

        if (isLayer1Active && A_PriorKey != "RButton")
            return

        run_()
    return

    *MButton::
        global mBtnUsed := 1
        global mBtnCount ++

        if (A_PriorKey = "XButton1")  {
            run__("lBtn__xBtn1_mBtn__")
        }
        else if (A_PriorKey = "XButton2")  {
            run__("lBtn__xBtn2_mBtn__")
        }
        else if (A_PriorKey = "RButton")  {
            run__("lBtn__rBtn_mBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("lBtn__wUp_mBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("lBtn__wDown_mBtn__")
        }
        else {
            run__("lBtn__mBtn__")
        }
        
        KeyWait, MButton

        if (isLayer1Active && A_PriorKey != "MButton")
            return

        run_()
    return

    *WheelUp::
        global wUpUsed := 1
        global wUpCount ++

        if (A_PriorKey = "XButton1") {
            run_("lBtn__xBtn1_wUp_")
        }
        else if (A_PriorKey = "XButton2") {
            run_("lBtn__xBtn2_wUp_")
        }
        else if (A_PriorKey = "RButton") {
            run_("lBtn__rBtn_wUp_")
        }
        else if (A_PriorKey = "MButton")  {
            run_("lBtn__mBtn_wUp_")
        }
        else {
            run_("lBtn__wUp_")
        }
    return

    *WheelDown::
        global wDownUsed := 1
        global wDownCount ++

        if (A_PriorKey = "XButton1") {
            run_("lBtn__xBtn1_wDown_")
        }
        else if (A_PriorKey = "XButton2") {
            run_("lBtn__xBtn2_wDown_")
        }
        else if (A_PriorKey = "RButton") {
            run_("lBtn__rBtn_wDown_")
        }
        else if (A_PriorKey = "MButton")  {
            run_("lBtn__mBtn_wDown_")
        }
        else {
            run_("lBtn__wDown_")
        }
    return
#if

#if _rBtnHeld
    *XButton1::
        global xBtn1Used := 1
        global xBtn1Count ++

        if (A_PriorKey = "LButton") {
            msgbox % A_priorkey
            run__("rBtn__lBtn_xBtn1__")
        }
        else if (A_PriorKey = "MButton") {
            run__("rBtn__mBtn_xBtn1__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("rBtn__wUp_xBtn1__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("rBtn__wDown_xBtn1__")
        }
        else {
            run__("rBtn__xBtn1__")
        }

        KeyWait, XButton1

        if (isLayer1Active && A_PriorKey != "XButton1")
            return

        run_()
    return

    *XButton2::
        global xBtn2Used := 1
        global xBtn2Count ++

        if (A_PriorKey = "LButton") {
            run__("rBtn__lBtn_xBtn2__")
        }
        else if (A_PriorKey = "MButton") {
            run__("rBtn__mBtn_xBtn2__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("rBtn__wUp_xBtn2__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("rBtn__wDown_xBtn2__")
        }
        else {
            run__("rBtn__xBtn2__")
        }

        KeyWait, XButton2

        if (isLayer1Active && A_PriorKey != "XButton2")
            return

        run_()
    return

    *LButton::
        global lBtnUsed := 1
        global lBtnCount ++

        if (A_PriorKey = "XButton1")  {
            run__("rBtn__xBtn1_lBtn__")
        }
        else if (A_PriorKey = "XButton2")  {
            run__("rBtn__xBtn2_lBtn__")
        }
        else if (A_PriorKey = "MButton")  {
            run__("rBtn__mBtn_lBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("rBtn__wUp_lBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("rBtn__wDown_lBtn__")
        }
        else {
            run__("rBtn__lBtn__")
        }

        KeyWait, LButton

        if (isLayer1Active && A_PriorKey != "LButton")
            return

        run_()
    return

    *MButton::
        global mBtnUsed := 1
        global mBtnCount ++

        if (A_PriorKey = "XButton1")  {
            run__("rBtn__xBtn1_mBtn__")
        }
        else if (A_PriorKey = "XButton2")  {
            run__("rBtn__xBtn2_mBtn__")
        }
        else if (A_PriorKey = "LButton")  {
            run__("rBtn__lBtn_mBtn__")
        }
        else if (A_PriorKey = "WheelUp") {
            run__("rBtn__wUp_mBtn__")
        }
        else if (A_PriorKey = "WheelDown") {
            run__("rBtn__wDown_mBtn__")
        }
        else {
            run__("rBtn__mBtn__")
        }

        KeyWait, MButton

        if (isLayer1Active && A_PriorKey != "MButton")
            return

        run_()
    return

    *WheelUp::
        global wUpUsed := 1
        global wUpCount ++

        if (A_PriorKey = "XButton1") {
            run_("rBtn__xBtn1_wUp_")
        }
        else if (A_PriorKey = "XButton2") {
            run_("rBtn__xBtn2_wUp_")
        }
        else if (A_PriorKey = "LButton") {
            run_("rBtn__lBtn_wUp_")
        }
        else if (A_PriorKey = "MButton")  {
            run_("rBtn__mBtn_wUp_")
        }
        else {
            run_("rBtn__wUp_")
        }
    return

    *WheelDown::
        global wDownUsed := 1
        global wDownCount ++

        if (A_PriorKey = "XButton1") {
            run_("rBtn__xBtn1_wDown_")
        }
        else if (A_PriorKey = "XButton2") {
            run_("rBtn__xBtn2_wDown_")
        }
        else if (A_PriorKey = "LButton") {
            run_("rBtn__lBtn_wDown_")
        }
        else if (A_PriorKey = "MButton")  {
            run_("rBtn__mBtn_wDown_")
        }
        else {
            run_("rBtn__wDown_")
        }
    return
#if

; -------------------------------------- XButton1/2 --------------------------------------
#if (!GetKeyState("LButton", "P") && !GetKeyState("RButton", "P"))
    *XButton1::
        initVar()

        run__("xBtn1__")
        
        ; To activate #if blocks
        _xBtn1Held := 1
        KeyWait, XButton1
        _xBtn1Held := 0

        ; Restore/Customize normal functionality if used merely as a key
        if (xBtn1Used + xBtn2Used + lBtnUsed + rBtnUsed + mBtnUsed + wUpUsed + wDownUsed = 0) {
            run_()
            return
        }
        
        _run()
    return

    *XButton2::
        initVar()

        run__("xBtn2__")

        _xBtn2Held := 1
        KeyWait, XButton2
        _xBtn2Held := 0

        if (!isLayer1Active) {
            run_()
            return
        }

        _run()
    return
#if

; -------------------------------------- L/RButton --------------------------------------
#if (!GetKeyState("XButton1", "P") && !GetKeyState("XButton2", "P"))
    ~*LButton::
        initVar()

        _lBtnHeld := 1
        KeyWait, LButton
        _lBtnHeld := 0

        if (!isLayer1Active)
            return

        _run()
    return

    *RButton::
        initVar()

        _rBtnHeld := 1
        KeyWait, RButton
        _rBtnHeld := 0

        if (!isLayer1Active) {
            Send {RButton}
            return
        }

        _run()
    return
#if

; --------------------------------------- MButton ---------------------------------------
#if (!GetKeyState("LButton", "P") && !GetKeyState("RButton", "P") && !GetKeyState("XButton1", "P") && !GetKeyState("XButton2", "P"))
    ~MButton::
    return
#if

; =========================================================================================
; ========================================== END ==========================================
; =========================================================================================