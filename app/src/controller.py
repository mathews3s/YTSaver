import sys


class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.setup_ui()
        self.start_ui()

    def setup_ui(self):
        self.view.setupGraphicalEvents()
        self.setup_ui_signals()
        self.view.showMainWindow(True)
        self.update_view_tab()
        self.switch_to_view_tab()

    def start_ui(self):
        sys.exit(self.view.app.exec_())

    def setup_ui_signals(self):
        # self.view.SettingsTabButton.clicked.connect(lambda: self.switchToSettingsTab())
        self.view.FindTabButton.clicked.connect(lambda: self.switch_to_find_tab())
        self.view.PlaylistsTabButton.clicked.connect(lambda: self.switch_to_view_tab())

        self.view.VTP_UpButton.clicked.connect(lambda: self.playlists_scroll_up())
        self.view.VTP_DownButton.clicked.connect(lambda: self.playlists_scroll_down())
        self.view.VTV_UpButton.clicked.connect(lambda: self.videos_scroll_up())
        self.view.VTV_DownButton.clicked.connect(lambda: self.videos_scroll_down())

        self.view.Playlist1_Icon.mousePressEvent = lambda event: self.playlist1_icon_clicked()
        self.view.Playlist2_Icon.mousePressEvent = lambda event: self.playlist2_icon_clicked()

    def switch_to_view_tab(self):
        self.view.MainMenu.setCurrentWidget(self.view.ViewingTab)

    def update_view_tab(self):
        count = self.model.get_playlists_count()
        self.model.setup_current_playlists()

        if count == 0:
            self.view.VTP_NothingLabel.setVisible(True)
        else:
            self.view.VTP_NothingLabel.setVisible(False)

            playlists_info = self.model.get_current_playlists_info()

            if not playlists_info[0] is None:
                self.view.set_playlist1_info(playlists_info[0])
                if playlists_info[2] == playlists_info[0]:
                    self.view.highlightItem(self.view.Playlist1_Icon, self.view.px_medium)
                else:
                    self.view.unhighlightItem(self.view.Playlist1_Icon, self.view.px_medium)
                self.view.VTP_Playlist1_Container.setVisible(True)

            if not playlists_info[1] is None:
                self.view.set_playlist2_info(playlists_info[1])
                if playlists_info[2] == playlists_info[1]:
                    self.view.highlightItem(self.view.Playlist2_Icon, self.view.px_medium)
                else:
                    self.view.unhighlightItem(self.view.Playlist2_Icon, self.view.px_medium)
                self.view.VTP_Playlist2_Container.setVisible(True)
            else:
                self.view.VTP_Playlist2_Container.setVisible(False)

        self.view.VT_PlaylistsCount.setText(str(count))

    def switch_to_find_tab(self):
        self.view.MainMenu.setCurrentWidget(self.view.FindTab)



    def playlists_scroll_down(self):
        self.model.playlists_offset_down()
        self.update_view_tab()

    def playlists_scroll_up(self):
        self.model.playlists_offset_up()
        self.update_view_tab()

    def playlist1_icon_clicked(self):
        self.model.set_playlist1_as_current()
        self.view.highlightItem(self.view.Playlist1_Icon, self.view.px_medium)
        self.view.unhighlightItem(self.view.Playlist2_Icon, self.view.px_medium)

    def playlist2_icon_clicked(self):
        self.model.set_playlist2_as_current()
        self.view.highlightItem(self.view.Playlist2_Icon, self.view.px_medium)
        self.view.unhighlightItem(self.view.Playlist1_Icon, self.view.px_medium)



    def videos_scroll_down(self):
        self.model.videos_offset_down()
        self.update_view_tab()

    def videos_scroll_up(self):
        self.model.videos_offset_up()
        self.update_view_tab()

    def video1_icon_clicked(self):
        self.model.set_video1_as_current()
        self.view.highlightItem(self.view.Video1_Icon, self.view.px_medium)
        self.view.unhighlightItem(self.view.Video2_Icon, self.view.px_medium)

    def video2_icon_clicked(self):
        self.model.set_video2_as_current()
        self.view.highlightItem(self.view.Video2_Icon, self.view.px_medium)
        self.view.unhighlightItem(self.view.Video1_Icon, self.view.px_medium)