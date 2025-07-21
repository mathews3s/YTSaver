
from controller import Controller
from view import View
from model import Model
import sys



if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)

