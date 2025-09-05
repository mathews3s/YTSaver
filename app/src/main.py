
from controller import Controller
from view import View
from view2 import View2
from model import Model
import sys



if __name__ == "__main__":
    model = Model()
    view = View2()
    controller = Controller(model, view)

