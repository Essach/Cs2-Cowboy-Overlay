import sys
from PyQt5.QtWidgets import QApplication
import os
from overlay import Overlay

if __name__ == "__main__":
    os.environ["QT_LOGGING_RULES"] = "qt.gui.imageio=false"

    app = QApplication(sys.argv)

    screen = app.primaryScreen()
    size = screen.size()

    window = Overlay(size)
    window.show()
    sys.exit(app.exec_())