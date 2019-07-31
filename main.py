from PyQt5.QtWidgets import *
import sys
from SoftwareTool import Ui_MainWindow
from winregeditor import winregeditor
from UninstallSoftware import ShowWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ShowWindow()
    ui.show()
    sys.exit(app.exec_())
   