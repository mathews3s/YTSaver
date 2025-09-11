import sys

class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.setup_app()
        self.startup_app()

    ''' --------- APP INITIALIZATION ------------- '''

    def setup_app(self):
        self.model.set_feedback(self)
        self.view.set_feedback(self)
        self.view.setup_graphical_events()
        self.view.show_main_window(True)
        self.model.update_storages()
        self.update_video_tab()
        self.user_switch_to_video_tab()

    def startup_app(self):
        sys.exit(self.view.app.exec_())

    ''' --------- СONTROLLER/MODEL/VIEW INTERACTIONS ------------- '''

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

    def video_close(self):
        self.view.undisplay_video()

    def download_going(self):
        pass

    ''' --------- USER NAV BAR INTERACTION ------------- '''

    def user_switch_to_video_tab(self):
        self.view.switch_to_video_tab()

    def user_switch_to_download_tab(self):
        self.view.switch_to_download_tab()

    ''' --------- USER VIDEO TAB INTERACTION ------------- '''

    def user_click_scroll_down(self):
        self.model.videos_offset_down()
        self.update_video_tab()

    def user_click_scroll_up(self):
        self.model.videos_offset_up()
        self.update_video_tab()

    def user_click_video1_icon(self):
        self.model.set_video_as_current(self.model.video_1)
        self.view.mark_first_video_as_current(True)
        self.view.enable_video_controls(True)

    def user_click_video2_icon(self):
        self.model.set_video_as_current(self.model.video_2)
        self.view.mark_second_video_as_current(True)
        self.view.enable_video_controls(True)

    def user_click_delete(self):
        current_video_data = self.model.get_videos_info()['current']
        if current_video_data != None:
            self.view.switch_to_dialog_tab(msg=f"TO DELETE {current_video_data['video_name']}")

    def user_click_edit(self):
        current_video = self.model.get_videos_info()['current']
        if current_video != None:
            self.view.edit_video(current_video)

    def user_click_watch(self):
        data = self.model.get_videos_info()
        current_video = data['current']

        if current_video != None:
            path = data['current']['video_path']
            self.view.display_video(path)

    ''' --------- USER DIALOG TAB INTERACTION ------------- '''

    def user_click_accept_delete(self):
        current_video = self.model.get_videos_info()['current']
        self.model.delete_video(current_video, True)
        self.model.update_storages()
        self.update_video_tab()
        self.user_switch_to_video_tab()

    ''' --------- USER UNIVERSAL INTERACTION ------------- '''

    def user_click_cancel(self):
        self.user_switch_to_video_tab()

    ''' --------- USER EDIT TAB INTERACTION ------------- '''

    def user_accept_edit_clicked(self):
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
            self.user_switch_to_video_tab()

    ''' --------- USER DOWNLOAD TAB INTERACTION ------------- '''

    def user_click_find(self):
        link = self.view.get_data_search_bar()
        if self.model.try_to_find(link):
            info = self.model.get_suitable_streams_information()
            self.view.switch_to_download_details_tab(info['video_name'])
            self.view.show_available_resolutions(info['resolutions'])
            print("++")
        else:
            print("___")

    ''' --------- USER DOWNLOAD DETAILS TAB INTERACTION ------------- '''

    def user_select_resolution(self):
        data_from_view = self.view.get_data_from_download_fields()
        self.model.update_streams_by_filter(res=data_from_view['resolution'])
        data_from_model = self.model.get_suitable_streams_information()
        self.view.show_available_formats(data_from_model['formats'])

    def user_select_format(self):
        data_from_view = self.view.get_data_from_download_fields()
        self.model.update_streams_by_filter(res=data_from_view['resolution'],
                                            fmt=data_from_view['format'])
        data_from_model = self.model.get_suitable_streams_information()
        self.view.show_available_fps(data_from_model['fps'])
        print("+++")

    def user_select_fps(self):
        data_from_view = self.view.get_data_from_download_fields()
        self.model.update_streams_by_filter(res=data_from_view['resolution'],
                                            fmt=data_from_view['format'],
                                            fps=data_from_view['fps'])
        self.view.enable_download_controls(True)

    def user_clicked_download(self):
        data_from_view = self.view.get_data_from_download_fields()

        if self.model.check_download_video_data(data_from_view):
            self.model.start_download()
            self.user_switch_to_video_tab()
        else:
            self.user_select_fps()



