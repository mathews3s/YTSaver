from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication as AppQT
import sys

class Controller:
    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.setupUI()
        self.startUI()

    def setupUI(self):
        self.view.setupGraphicalEvents()
        self.setupUISignals()

    def startUI(self):
        self.view.showMainWindow(True)
        sys.exit(self.view.app.exec_())

    def setupUISignals(self):
        self.view.SettingsTabButton.clicked.connect(lambda: self.switchMainMenuTab(self.view.SettingsTab))
        self.view.FindTabButton.clicked.connect(lambda: self.switchMainMenuTab(self.view.FindTab))
        self.view.PlaylistsTabButton.clicked.connect(lambda: self.switchMainMenuTab(self.view.ViewingTab))

    def switchMainMenuTab(self, tab):
        self.view.MainMenu.setCurrentWidget(tab)




    # def hide(self):
    #     self.view.VTV_Video2_Container.setVisible(False)



