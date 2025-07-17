from PyQt5 import QtWidgets

import sys

class Controller:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def initUi(self):
        self.view.setupMainWindow()
        self.view.setupGraphicalEvents()

    def showUI(self):
        self.view.showMainWindow(True)



    # def hide(self):
    #     self.view.VTV_Video2_Container.setVisible(False)



