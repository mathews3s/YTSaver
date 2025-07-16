from controller import Controller


# def setup_ui_events(window):
#     window.Playlist1_Icon.mousePressEvent = lambda event: hide(window.VTV_Video2_Container)
#     window.Playlist1_Icon.enterEvent = lambda event: led(window.Playlist1_Icon)
#
# def hide(group_box):
#     group_box.setVisible(False)
#
# def led(group_box):
#     group_box.setStyleSheet("border: 2px solid white;")


if __name__ == "__main__":
    controller = Controller()
    controller.initUi()
    controller.showUI()
    controller.startApp()

