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
        self.show_playlists()
        self.view.VT_PlaylistsCount.setText(str(count))

    def show_playlists(self):
        displayed_playlists = self.model.get_current_playlists_info()

        if not (displayed_playlists[0] is None):
            self.view.set_playlist1_info(displayed_playlists[0])
            if displayed_playlists[2] is displayed_playlists[0]:
                self.view.highlightItem(self.view.Playlist1_Icon, self.view.px_medium)
            else:
                self.view.unhighlightItem(self.view.Playlist1_Icon, self.view.px_medium)
            self.view.VTP_Playlist1_Container.setVisible(True)

        if not (displayed_playlists[1] is None):
            self.view.set_playlist2_info(displayed_playlists[1])
            if displayed_playlists[2]['id'] == displayed_playlists[1]['id']:
                self.view.highlightItem(self.view.Playlist2_Icon, self.view.px_medium)
            else:
                self.view.unhighlightItem(self.view.Playlist2_Icon, self.view.px_medium)
            self.view.VTP_Playlist2_Container.setVisible(True)
        else:
            self.view.VTP_Playlist2_Container.setVisible(False)


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