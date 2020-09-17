from pywinauto import application, win32defines
from pywinauto.win32functions import ShowWindow
import psutil
import win32process
import win32gui

# Select random app from the pull of apps
def display_bdo():
    # Init App object
    app = application.Application().connect(title_re=".*%s.*" % 'BLACK DESERT')
    w = app.top_window()

    w.set_focus()


def bdo_active() -> bool:
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        if psutil.Process(pid[-1]).name() == "BlackDesert64.exe":
            return True

        return False

    except:
        pass
