import sys


class Controller:

    def __init__(self, model, view, paths):
        self.view = view
        self.model = model
        self.model.prepare_paths_for_resources(paths)
        self.setup_app()
        self.startup_app()

    # Input/Output points of the app

    def setup_app(self):
        self.model.model_set_feedback(controller=self)
        self.view.view_set_feedback(controller=self)
        self.model.model_check_resources()
        self.view.setup_graphical_events()
        self.view.main_window_open(True)
        self.model.model_update_video_collection()
        self.controller_update_video_tab()
        self.user_switch_to_video_tab_handler()

    def startup_app(self):
        sys.exit(self.view.app.exec_())

    def close_app(self):
        sys.exit()

    # Handlers for model processing app events

    def controller_notify_user(self, msg):
        self.view.set_text_app_messenger(msg)

    def controller_update_video_tab(self):
        count = self.model.get_videos_count()
        self.view.set_videos_count_text(count)

        match count:
            case 0:
                self.view.videos_containers_empty()
            case _:
                self.view.videos_containers_not_empty()
                self.model.model_change_videos_page()
                self.controller_update_displayed_videos()

    def controller_update_displayed_videos(self):
        self.view.mark_first_video_as_selected(False)
        self.view.mark_second_video_as_selected(False)

        first_video_data = self.model.get_first_video_data()
        second_video_data = self.model.get_second_video_data()
        current_video_data = self.model.get_current_video_data()

        if not (first_video_data is None):
            self.view.display_first_video_container(first_video_data)
        if not (second_video_data is None):
            self.view.display_second_video__container(second_video_data)
        else:
            self.view.hide_second_video_container()

        if current_video_data == None:
            self.view.enable_video_controls_buttons(False)
        elif current_video_data == second_video_data:
            self.view.mark_second_video_as_selected(True)
            self.view.enable_video_controls_buttons(True)
        elif current_video_data == first_video_data:
            self.view.mark_first_video_as_selected(True)
            self.view.enable_video_controls_buttons(True)
        else:
            self.view.mark_first_video_as_selected(False)
            self.view.mark_second_video_as_selected(False)

    def user_close_video_preview_handler(self):
        self.view.clode_video_preview_tab()
        self.user_click_cancel_handler()

    def model_downloading_stream_handler(self, downloading_message):
        self.controller_notify_user(msg=downloading_message)

    def model_downloaded_youtube_video_info_handler(self):
        self.model.update_video_streams_by_filter()
        data = self.model.get_download_video_data()
        if data is not None:
            self.controller_notify_user("Выберите параметры для загрузки видео")
            self.view.switch_to_download_details_tab(data)
            self.view.enable_download_tab_download_controls(False)
        else:
            self.controller_notify_user("Ошибка во время получения сведений о видео. Попробуйте еще раз!")

    def model_successfully_downloaded_video_handler(self, msg):
        self.controller_notify_user(msg)
        self.model.model_update_video_collection()
        self.controller_update_video_tab()
        self.user_switch_to_video_tab_handler()
        self.view.enable_controls_while_downloading(flag=True)

    # Handler for user interaction in navigation bar

    def user_switch_to_video_tab_handler(self):
        self.controller_notify_user("Ваша история")
        self.view.switch_to_video_tab()

    def user_switch_to_download_tab_handler(self):
        self.controller_notify_user("Введите ваш поисковой запрос")
        self.view.switch_to_download_tab()

    # Handler for user interaction in video tab

    def user_click_scroll_down_page_handler(self):
        self.model.model_prev_videos_page()
        self.controller_update_video_tab()

    def user_click_scroll_up_page_handler(self):
        self.model.model_next_videos_page()
        self.controller_update_video_tab()

    def user_select_first_video_handler(self):
        if self.model.set_video_as_current(self.model.first_video):
            self.view.mark_first_video_as_selected(True)
            self.view.enable_video_controls_buttons(True)

    def user_select_second_video_handler(self):
        if self.model.set_video_as_current(self.model.second_video):
            self.view.mark_second_video_as_selected(True)
            self.view.enable_video_controls_buttons(True)

    def user_click_delete_selected_video_handler(self):
        current_video_data = self.model.get_current_video_data()

        if current_video_data != None:
            self.controller_notify_user("Подтвердите удаление видео")
            self.view.switch_to_delete_tab(msg=f"Удаление видеофайла: |{current_video_data['video_name']}|")

    def user_click_edit_selected_video_handler(self):
        current_video = self.model.get_current_video_data()

        if current_video != None:
            self.controller_notify_user("Отредактируйте необходимую информацию")
            self.view.open_edit_video_tab(current_video)

    def user_click_watch_selected_video_handler(self):
        current_video = self.model.get_current_video_data()

        if current_video != None:
            self.controller_notify_user("Просмотр превью загруженного видео")
            self.view.open_video_preview_tab(current_video)

    # Handler for user interaction in delete tab

    def user_click_accept_delete_handler(self):
        current_video = self.model.get_current_video_data()
        if current_video != None:
            if self.model.delete_video_model(video=current_video, full_delete=True):
                self.model.model_update_video_collection()
                self.controller_update_video_tab()
                self.user_switch_to_video_tab_handler()

    # Handler for user canceling in download/find/edit/delete tabs

    def user_click_cancel_handler(self):
        self.model.reset_model_pytube()
        self.user_switch_to_video_tab_handler()

    # Handlers for user interaction in edit video tab

    def user_click_accept_edit_handler(self):
        new_video_data = self.view.get_data_from_edit_video_tab()
        data_correct = self.model.model_check_data_for_editing(new_video_data)
        if data_correct:
            self.model.edit_video_model(new_video_data)
            self.model.model_update_video_collection()
            self.controller_update_video_tab()
            self.view.switch_to_video_tab()

    # Handlers for user interaction in find tab

    def user_click_find_youtube_video_handler(self):
        link = self.view.get_data_from_find_tab()
        if self.model.model_search_video(link):
            self.controller_notify_user("Видео найдено. Подождите ...")
            self.model.model_download_youtube_video()
        else:
            self.controller_notify_user("Видео не найдено. Попробуйте еще раз")

    # Handlers for user interaction in download details tab

    def user_select_resolution_handler(self):
        data_from_view = self.view.get_data_from_download_tab()
        self.model.update_video_streams_by_filter(res=data_from_view['resolution'])
        data_from_model = self.model.get_download_video_data()
        self.view.display_available_formats(data_from_model['formats'])
        self.view.enable_download_tab_download_controls(False)

    def user_select_format_handler(self):
        data_from_view = self.view.get_data_from_download_tab()
        self.model.update_video_streams_by_filter(res=data_from_view['resolution'],
                                                  fmt=data_from_view['format'])
        data_from_model = self.model.get_download_video_data()
        self.view.display_available_fps(data_from_model['fps'])
        self.view.enable_download_tab_download_controls(False)

    def user_select_fps(self):
        data_from_view = self.view.get_data_from_download_tab()
        self.model.update_video_streams_by_filter(res=data_from_view['resolution'],
                                                  fmt=data_from_view['format'],
                                                  fps=data_from_view['fps'])
        self.view.enable_download_tab_download_controls(True)

    def user_clicked_download_youtube_video_handler(self):
        data_from_view = self.view.get_data_from_download_tab()
        correct = self.model.model_prepare_before_downloading(data_from_view)
        if correct:
            self.view.enable_controls_while_downloading(flag=False)
            self.model.select_suit_stream()
            self.model.start_download_video()
        else:
            self.user_select_fps()
            self.controller_notify_user("Проверьте правильность пути!")

    # Handlers for app errors

    def model_downloading_youtube_video_info_error(self, name_err: str = ""):
        self.controller_notify_user("Ошибка во время загрузки сведений: " + name_err)
        self.view.switch_to_download_tab()

    def model_downloading_youtube_video_error(self, name_err: str = ""):
        self.user_switch_to_download_tab_handler()
        self.view.enable_controls_while_downloading(flag=True)
        self.controller_notify_user("Ошибка во время загрузки видео: " + name_err)

    def model_edit_video_error(self, name_err: str = ""):
        self.controller_notify_user("Ошибка во время редактирования видео: " + name_err)

    def model_delete_video_error(self, name_err: str = ""):
        self.controller_notify_user("Ошибка во время удаления видео: " + name_err)

    def model_critical_error(self, error_code):
        self.view.show_critical_error_window(f"Произошла критическая ошибка, код: {error_code}")
        self.close_app()