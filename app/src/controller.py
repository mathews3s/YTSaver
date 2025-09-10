import sys


class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.setup_app()
        self.startup_app()

    def setup_app(self):
        self.view.setup_graphical_events()
        self.setup_ui_signals()
        self.view.show_main_window(True)
        self.model.update_storages()
        self.update_video_tab()
        self.switch_to_video_tab()

    def startup_app(self):
        sys.exit(self.view.app.exec_())

    def setup_ui_signals(self):
        self.view.DownloadTabButton.clicked.connect(lambda: self.switch_to_find_tab())
        self.view.VideosTabButton.clicked.connect(lambda: self.switch_to_video_tab())

        self.view.VID_UpButton.clicked.connect(lambda: self.videos_scroll_up())
        self.view.VID_DownButton.clicked.connect(lambda: self.videos_scroll_down())

        self.view.VID1_Icon.mousePressEvent = lambda event: self.video1_icon_clicked()


        self.view.DLG_AcceptButton.mousePressEvent = lambda event: self.accept_delete_clicked()
        self.view.DLG_CancelButton.mousePressEvent = lambda event: self.cancel_clicked()

        self.view.VID_DeleteButton.mousePressEvent = lambda event: self.video_delete_clicked()
        self.view.VID_EditButton.clicked.connect(lambda: self.video_edit_clicked())
        self.view.EDT_SaveButton.mousePressEvent = lambda event: self.accept_edit_clicked()
        self.view.EDT_CancelButton.mousePressEvent = lambda event: self.cancel_clicked()

        self.view.VID_WatchButton.clicked.connect(lambda: self.video_open())
        self.view.PT_CancelButton.clicked.connect(lambda: self.video_close())


        self.view.VID2_Icon.mousePressEvent = lambda event: self.video2_icon_clicked()




    def switch_to_video_tab(self):
        self.view.MainMenu.setCurrentWidget(self.view.VideoTab)

    def update_video_tab(self):
        count = self.model.get_videos_count()
        self.view.update_displayed_count_videos(count)
        match count:
            case 0:
                self.view.disable_videos_display()
            case _:
                self.view.enable_videos_display()
                self.model.switch_current_videos()
                self.update_displayed_videos()

    def update_displayed_videos(self):
        self.view.mark_first_video_as_current(False)
        self.view.mark_second_video_as_current(False)

        videos_data_for_show = self.model.get_videos_info()
        first_video_data = videos_data_for_show['first']
        second_video_data = videos_data_for_show['second']
        current_video_data = videos_data_for_show['current']

        if not (first_video_data is None):
            self.view.display_first_video(first_video_data)

        if not (second_video_data is None):
            self.view.display_second_video(second_video_data)
        else:
            self.view.hide_second_video()
        if current_video_data == None:
            self.view.enable_video_controls(False)
        elif current_video_data == second_video_data:
            self.view.mark_second_video_as_current(True)
            self.view.enable_video_controls(True)
        elif current_video_data == first_video_data:
            self.view.mark_first_video_as_current(True)
            self.view.enable_video_controls(True)
        else:
            self.view.mark_first_video_as_current(False)
            self.view.mark_second_video_as_current(False)

    def switch_to_find_tab(self):
        self.view.MainMenu.setCurrentWidget(self.view.DownloadTab)

    def videos_scroll_down(self):
        self.model.videos_offset_down()
        self.update_video_tab()

    def videos_scroll_up(self):
        self.model.videos_offset_up()
        self.update_video_tab()

    def video1_icon_clicked(self):
        self.model.set_video_as_current(self.model.video_1)
        self.view.mark_first_video_as_current(True)
        self.view.enable_video_controls(True)


    def video2_icon_clicked(self):
        self.model.set_video_as_current(self.model.video_2)
        self.view.mark_second_video_as_current(True)
        self.view.enable_video_controls(True)


    def video_delete_clicked(self):
        current_video_data = self.model.get_videos_info()['current']
        if current_video_data != None:
            self.view.delete_video_dialog(current_video_data['video_name'])

    def accept_delete_clicked(self):
        current_video = self.model.get_videos_info()['current']
        self.model.delete_video(current_video, True)
        self.model.update_storages()
        self.update_video_tab()
        self.switch_to_video_tab()


    def cancel_clicked(self):
        self.switch_to_video_tab()

    def video_edit_clicked(self):
        current_video = self.model.get_videos_info()['current']
        if current_video != None:
            self.view.edit_video(current_video)

    def accept_edit_clicked(self):
        current_video = self.model.get_videos_info()['current']
        new_video_data = self.view.get_data_from_edit_fields()
        is_good = self.model.check_video_data(new_video_data)
        if is_good:
            new_video_data['id'] = current_video['id']
            new_video_data['video_format'] = current_video['video_format']
            new_video_data['video_date'] = current_video['video_date']
            new_video_data['video_icon'] = current_video['video_icon']
            self.model.update_video_in_db(new_video_data)

            self.model.update_storages()
            self.update_video_tab()
            self.switch_to_video_tab()


    def video_open(self):
        data = self.model.get_videos_info()
        current_video = data['current']

        if current_video != None:
            path = data['current']['video_path']
            self.view.display_video(path)

    def video_close(self):
        self.view.undisplay_video()