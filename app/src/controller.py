from view import View, QtWidgets
from model import Model
import sys

class Controller:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.view = View()
        self.model = Model()

    def startApp(self):
        sys.exit(self.app.exec_())

    def initUi(self):
        self.view.setupMainWindow()

    def showUI(self):
        self.view.showMainWindow(True)


