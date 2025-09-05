import sys


class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.setup_ui()
        self.startup_ui()

    def setup_ui(self):
        self.view.setupGraphicalEvents()
        self.setup_ui_signals()
        self.view.showMainWindow(True)
        self.update_view_tab()
        self.switch_to_video_tab()

    def startup_ui(self):
        sys.exit(self.view.app.exec_())

    def setup_ui_signals(self):
        self.view.DownloadTabButton.clicked.connect(lambda: self.switch_to_find_tab())
        self.view.VideosTabButton.clicked.connect(lambda: self.switch_to_video_tab())

        self.view.VID_UpButton.clicked.connect(lambda: self.videos_scroll_up())
        self.view.VID_DownButton.clicked.connect(lambda: self.videos_scroll_down())

        self.view.VID1_Icon.mousePressEvent = lambda event: self.video1_icon_clicked()
        self.view.VID2_Icon.mousePressEvent = lambda event: self.video2_icon_clicked()

    def switch_to_video_tab(self):
        self.view.MainMenu.setCurrentWidget(self.view.VideoTab)

    def update_view_tab(self):
        count = self.model.get_videos_count()
        self.model.setup_current_videos()
        self.show_videos(count)
        self.view.VID_CountValue.setText(str(count))

    def show_videos(self, count):
        # if count == 0:
        #     self.view.videos_empty()
        #     return
        self.view.videos_exists()
        displayed_videos = self.model.get_videos_info()
        first = displayed_videos['first']
        second = displayed_videos['second']
        current = displayed_videos['current']

        if not (first is None):
            self.view.set_video1_info(first)
            if current == first:
                self.view.highlightItem(self.view.VID1_Icon, self.view.px_medium)
            else:
                self.view.unhighlightItem(self.view.VID1_Icon, self.view.px_medium)
            self.view.VID1_Container.setVisible(True)

        if not (second is None):
            self.view.set_video2_info(second)
            if current == second:
                self.view.highlightItem(self.view.VID2_Icon, self.view.px_medium)
            else:
                self.view.unhighlightItem(self.view.VID2_Icon, self.view.px_medium)
            self.view.VID2_Container.setVisible(True)
        else:
            self.view.VID2_Container.setVisible(False)


    def switch_to_find_tab(self):
        self.view.MainMenu.setCurrentWidget(self.view.FindTab)



    def videos_scroll_down(self):
        self.model.videos_offset_down()
        self.update_view_tab()

    def videos_scroll_up(self):
        self.model.videos_offset_up()
        self.update_view_tab()

    def video1_icon_clicked(self):
        self.model.set_video_as_current(self.model.video_1)
        self.view.highlightItem(self.view.VID1_Icon, self.view.px_medium)
        self.view.unhighlightItem(self.view.VID2_Icon, self.view.px_medium)

    def video2_icon_clicked(self):
        self.model.set_video_as_current(self.model.video_2)
        self.view.highlightItem(self.view.VID2_Icon, self.view.px_medium)
        self.view.unhighlightItem(self.view.VID1_Icon, self.view.px_medium)