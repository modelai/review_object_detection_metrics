# Execute this script with the command below to open the GUI
# python run.py

import sys

from PyQt5 import QtWidgets
from object_detection_metrics.ui.run_ui import Main_Dialog
from object_detection_metrics.ui.splash import Splash_Dialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = Main_Dialog()
    ui.show()

    splash = Splash_Dialog()
    splash.show()

    sys.exit(app.exec_())
