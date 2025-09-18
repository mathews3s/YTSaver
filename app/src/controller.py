import sys

class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.setup_app()
        self.startup_app()

    ''' --------- APP INITIALIZATION ------------- '''

    def setup_app(self):
        self.model.set_feedback(instance=self)
        self.view.set_feedback(instance=self)
        self.view.setup_graphical_events()
        self.view.show_main_window(True)
        self.model.synchronize_app_videos_data_with_db()
        self.update_video_tab()
        self.user_switch_to_video_tab()

    def startup_app(self):
        sys.exit(self.view.app.exec_())

    def close_app(self):
        sys.exit()

    ''' --------- СONTROLLER/MODEL/VIEW INTERACTIONS ------------- '''


    def model_critical_error(self, code):
        self.view.end_by_error(code)
        self.close_app()

    def model_process_error(self, msg):
        self.view.setup_app_message(msg)

    def update_video_tab(self):

        count = self.model.get_videos_count()
        self.view.update_displayed_count_videos(count)
        match count:
            case 0:
                self.view.disable_videos_display()
            case _:
                self.view.enable_videos_display()
                self.model.move_in_videos_collection()
                self.update_displayed_videos()

    def update_displayed_videos(self):
        self.view.mark_first_video_as_current(False)
        self.view.mark_second_video_as_current(False)

        first_video_data = self.model.get_first_video_data()
        second_video_data = self.model.get_second_video_data()
        current_video_data = self.model.get_current_video_data()

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
        self.user_click_cancel()

    def download_going(self, msg):
        self.notify_user(msg)

    def download_end(self, msg):
        self.notify_user(msg)
        self.model.synchronize_app_videos_data_with_db()
        self.update_video_tab()
        self.user_switch_to_video_tab()
        self.view.enable_nav_controls(True)

    def notification_for_user(self, code):
        self.view.setup_app_message(code)

    def notify_user(self, msg):
        self.view.setup_app_message(msg)

    ''' --------- USER NAV BAR INTERACTION ------------- '''

    def user_switch_to_video_tab(self):
        self.notify_user("Ваша история")
        self.view.switch_to_video_tab()

    def user_switch_to_download_tab(self):
        self.notify_user("Введите ваш поисковой запрос")
        self.view.switch_to_download_tab()

    ''' --------- USER VIDEO TAB INTERACTION ------------- '''

    def user_click_scroll_down(self):
        self.model.videos_offset_down()
        self.update_video_tab()

    def user_click_scroll_up(self):
        self.model.videos_offset_up()
        self.update_video_tab()

    def user_click_video1_icon(self):
        self.model.set_video_as_current(self.model.first_video)
        self.view.mark_first_video_as_current(True)
        self.view.enable_video_controls(True)

    def user_click_video2_icon(self):
        self.model.set_video_as_current(self.model.second_video)
        self.view.mark_second_video_as_current(True)
        self.view.enable_video_controls(True)

    def user_click_delete(self):
        current_video_data = self.model.get_current_video_data()
        if current_video_data != None:
            self.notify_user("Удалите видео")
            self.view.switch_to_dialog_tab(msg=f"TO DELETE {current_video_data['video_name']}")

    def user_click_edit(self):
        current_video = self.model.get_current_video_data()
        if current_video != None:
            self.notify_user("Отредактируйте информацию")
            self.view.edit_video(current_video)

    def user_click_watch(self):
        current_video = self.model.get_current_video_data()

        if current_video != None:
            self.notify_user("Просмотр превью")
            path = current_video['video_path']
            self.view.display_video(path)

    ''' --------- USER DIALOG TAB INTERACTION ------------- '''

    def user_click_accept_delete(self):
        current_video = self.model.get_current_video_data()
        self.model.delete_video_model(current_video, full_delete=True)
        self.model.synchronize_app_videos_data_with_db()
        self.update_video_tab()
        self.view.switch_to_video_tab()

    ''' --------- USER UNIVERSAL INTERACTION ------------- '''

    def user_click_cancel(self):
        self.user_switch_to_video_tab()

    ''' --------- USER EDIT TAB INTERACTION ------------- '''

    def user_accept_edit_clicked(self):
        new_video_data = self.view.get_data_from_edit_fields()
        data_correct = self.model.check_new_data_for_video(new_video_data)
        if data_correct:
            self.model.edit_video(new_video_data)
            self.model.synchronize_app_videos_data_with_db()
            self.update_video_tab()
            self.view.switch_to_video_tab()

    ''' --------- USER DOWNLOAD TAB INTERACTION ------------- '''

    def find_youtube_video(self):
        link = self.view.get_data_search_bar()
        if self.model.try_to_find(link):
            self.notify_user("Видео найдено. Подождите ...")
            self.model.start_download_common_data()
        else:
            self.notify_user("Видео не найдено. Попробуйте еще раз")

    def common_data_downloaded(self):
        data = self.model.get_download_video_data()
        if data is not None:
            self.notify_user("Сведения о видео получены! Выберите параметры загрузки:")
            self.view.switch_to_download_details_tab(data)
        else:
            self.notify_user("Ошибка во время получения сведений о видео. Попробуйте еще раз!")






    ''' --------- USER DOWNLOAD DETAILS TAB INTERACTION ------------- '''

    def user_select_resolution(self):
        data_from_view = self.view.get_data_from_download_fields()
        self.model.update_video_streams_by_filter(res=data_from_view['resolution'])
        data_from_model = self.model.get_download_video_data()
        self.view.show_available_formats(data_from_model['formats'])

    def user_select_format(self):
        data_from_view = self.view.get_data_from_download_fields()
        self.model.update_video_streams_by_filter(res=data_from_view['resolution'],
                                                  fmt=data_from_view['format'])
        data_from_model = self.model.get_download_video_data()
        self.view.show_available_fps(data_from_model['fps'])

    def user_select_fps(self):
        data_from_view = self.view.get_data_from_download_fields()
        self.model.update_video_streams_by_filter(res=data_from_view['resolution'],
                                                  fmt=data_from_view['format'],
                                                  fps=data_from_view['fps'])
        self.view.enable_download_controls(True)

    def user_clicked_download(self):
        data_from_view = self.view.get_data_from_download_fields()
        correct = self.model.prepare_data_for_downloading_video(data_from_view)
        if correct:
            self.view.enable_nav_controls(False)
            self.model.select_suit_stream()
            self.model.start_download_video()
        else:
            self.user_select_fps()
            self.notify_user("Проверьте правильность введенных данных")



    def common_data_download_error(self, name_err: str = ""):
        self.notify_user("Ошибка во время загрузки сведений: " + name_err)

    def download_error(self, name_err: str = ""):
        self.user_switch_to_download_tab()
        self.view.enable_nav_controls(True)
        self.notify_user("Ошибка во время загрузки видео: " + name_err)

    def edit_error(self, name_err: str = ""):
        self.notify_user("Ошибка во время редактирования видео: " + name_err)

    def delete_error(self, name_err: str = ""):
        self.notify_user("Ошибка во время редактирования видео: " + name_err)