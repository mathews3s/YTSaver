from PyQt5.QtWidgets import QApplication as AppQT
from controller import Controller
from view import View
from model import Model
import sys



if __name__ == "__main__":
    app = AppQT([])
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.initUi()
    controller.showUI()
    sys.exit(app.exec_())

