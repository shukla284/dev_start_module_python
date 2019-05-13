import pyautogui
import pygetwindow as gw
import time
import new_codeforces as cff


def perform_automation():
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 1

    time.sleep(5)

    devWindow = gw.getWindowsWithTitle("Dev-C++ 5.11")[0]

    print("Maximized Status " + str(devWindow.isMaximized))
    print("Active Status " + str(devWindow.isActive))

    if devWindow.isMaximized:
        if not devWindow.isActive:
            devWindow.activate()
    elif not devWindow.isMaximized:
        devWindow.maximize()
        devWindow.activate()
    else:
        devWindow.activate()

    print("Dev C++ is activated \n Creating new file please provide a name to file")
    pyautogui.hotkey('ctrl', 'n')
    pyautogui.hotkey('ctrl', 's')

    print("Checking for Save As window")
    saveWindow = gw.getWindowsWithTitle("Save As")[0]

    if saveWindow.isMinimized:
        saveWindow.maximize()
        saveWindow.activate()
    elif saveWindow.isMaximized:
        saveWindow.activate()

    pyautogui.typewrite(cff.create_file())
    pyautogui.press('enter')

    print("Executed Successfully")
