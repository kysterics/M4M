Macro for Mouse - M4M
===========================================
### A ***Mouse Macro** configurator/program for Windows*
![image](https://github.com/kysterics/M4M/assets/63026996/d308b8e5-7095-419b-81c9-1332de587652)
<br>
<br>
What Is This?
-----------------------------
* **M4M** is a portable macro configurator (built using CustomTkinter) that generates/tests `.ahk` scripts for mouse button combos
* M4M can map macros to different mouse combos, for example, setting holding right click then left clicking once as the combo to perform <kbd>Alt</kbd>+<kbd>Tab</kbd>
* 146 distinct combos—also known as functions—can be defined to perform actions. Each of these combos has at most 3 and at least 2 ways of activation

Note
-----------------------------
* Combos with the same keys but different order are distinct from each other
* The original functions of your mouse buttons are retained by default
* Currently, any button/wheel/action (e.g. XButton3, mouse wheel tilt) other than the standard ones (left/right click, mouse wheel click/up/down, back and forward) cannot be mapped
* Basic knowledge of the AHK scripting langauge is required

Getting M4M up and running
---------------------------
* Download and install AutoHotkey v1.1
* Download `M4M_Configurator.zip` and run the `.exe` file
* **Alternatively:** Simply begin by defining macros under the 'Functions' section directly in the `.ahk` file
* Test the script after finishing editing by running it!

Keys for defining macros
---------------------------
* All available keys: `xBtn1`, `xBtn1¦2`, `xBtn2`, `lBtn`, `rBtn`, `mBtn`, `wUp`, `wDown`, where `xBtn1¦2` refers to XButton1 and XButton2 held down together, regardless of order

* Available 'modifier' keys: `xBtn1`, `xBtn1¦2`, `xBtn2`, `lBtn`, `rBtn`

About function names
---------------------------
1. '_' at the start indicates that the function only runs when nothing is held down
1. '_' after a key refers to it having been used or it being held down
1. '_' at the end also implies that the function will only be activated after the last key in the combo 1 been released (given there is no '_' at the start)
1. '__' after a key means that the function will only be activated while it is held down
1. '__' at the end also implies that the function activates while the last key in the combo is being held down (given there is no '_' at the start)

For example, if `lBtn__rBtn__()`, `lBtn__rBtn_()` and `_lBtn__rBtn_()` are all defined, they will be activated in this order. `lBtn__rBtn__()` on hold, `lBtn__rBtn_()` on release of the last key in the combo, and `_lBtn__rBtn_()` lastly. Also note that for example, `_lBtn__rBtn_()` is valid whereas `_lBtn__rBtn__()` is not.

Conditions that can be used in functions
---------------------------
1. `xBtn1Used`, `xBtn2Used`, `lBtnUsed`, `rBtnUsed`, `mBtnUsed`, `wUpUsed`, `wDownUsed`
1. `xBtn1Count`, `xBtn2Count`, `lBtnCount`, `rBtnCount`, `mBtnCount`, `wUpCount`, `wDownCount`
For `xxxHeld` conditions, use `GetKeyState("xxx", "P")`

Remarks
---------------------------
1. Add programs in which this script is not desired to be active to `exceptions`
1. Right-click drag is disabled by default due to performance complications
1. 'Holding' and 'using' actions are not set apart for the second key in a 3-key combo. For example, `xBtn1__lBtn__rBtn_` does not exist, but `xBtn1__lBtn_rBtn_`. This is to allow for quick actions (like `xBtn2__rBtn__` as opposed to `_xBtn2__rBtn_`), hold (like `xBtn2__rBtn__wUp_` [which is not a valid function]) and deadkey actions to exist in the same function to reduce clutter
1. The 'l/rBtn__xBtn1¦2' combos are not available due to various complications. The 'l/rBtn__xBtn1/2' combos should be used instead (together with conditions)

To-Do
---------------------------
1. Default to original function when the last key in a combo is triggered if the comobo is not defined
2. In GUI, add an option to disable the above feauture
3. Make combos involving XButton*N* configurable, where *N* > 2 and *N* $\in \mathbb{N}$
