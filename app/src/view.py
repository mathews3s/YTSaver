from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication as AppQT

class View():

    def __init__(self):
        self.px_low = 2
        self.px_medium = 4
        self.app = AppQT([])
        self.window = QtWidgets.QMainWindow()
        self.window.setObjectName("MainWindow") ###
        self.window.resize(1010, 730) ###
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.window.sizePolicy().hasHeightForWidth()) ###
        self.window.setSizePolicy(self.sizePolicy) ###
        self.window.setMinimumSize(QtCore.QSize(1010, 730)) ###
        self.window.setMaximumSize(QtCore.QSize(1010, 730)) ###

        self.window.setStyleSheet("border-color: rgb(255, 16, 80);") ###
        self.WorkSpace = QtWidgets.QWidget(self.window) ###
        self.WorkSpace.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 85, 127);")
        self.WorkSpace.setObjectName("WorkSpace")
        self.AppMessagerBar = QtWidgets.QFrame(self.WorkSpace)
        self.AppMessagerBar.setGeometry(QtCore.QRect(0, 10, 1021, 71))
        self.AppMessagerBar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 0px;")
        self.AppMessagerBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AppMessagerBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AppMessagerBar.setObjectName("AppMessagerBar")
        self.AppMessagerIcon = QtWidgets.QLabel(self.AppMessagerBar)
        self.AppMessagerIcon.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.AppMessagerIcon.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.AppMessagerIcon.setText("")
        self.AppMessagerIcon.setObjectName("AppMessagerIcon")
        self.AppMessagerOutput = QtWidgets.QLabel(self.AppMessagerBar)
        self.AppMessagerOutput.setGeometry(QtCore.QRect(110, 30, 55, 16))
        self.AppMessagerOutput.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.AppMessagerOutput.setObjectName("AppMessagerOutput")
        self.ControlButtonsBar = QtWidgets.QFrame(self.WorkSpace)
        self.ControlButtonsBar.setGeometry(QtCore.QRect(-10, 90, 1021, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ControlButtonsBar.sizePolicy().hasHeightForWidth())
        self.ControlButtonsBar.setSizePolicy(sizePolicy)
        self.ControlButtonsBar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 0px;")
        self.ControlButtonsBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ControlButtonsBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ControlButtonsBar.setObjectName("ControlButtonsBar")
        self.PlaylistsTabButton = QtWidgets.QPushButton(self.ControlButtonsBar)
        self.PlaylistsTabButton.setGeometry(QtCore.QRect(20, 10, 141, 41))
        self.PlaylistsTabButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.PlaylistsTabButton.setObjectName("PlaylistsTabButton")
        self.FindTabButton = QtWidgets.QPushButton(self.ControlButtonsBar)
        self.FindTabButton.setGeometry(QtCore.QRect(180, 10, 141, 41))
        self.FindTabButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.FindTabButton.setObjectName("FindTabButton")
#         self.SettingsTabButton = QtWidgets.QPushButton(self.ControlButtonsBar)
#         self.SettingsTabButton.setGeometry(QtCore.QRect(340, 10, 141, 41))
#         self.SettingsTabButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius: 20px;")
#         self.SettingsTabButton.setObjectName("SettingsTabButton")
        self.MainMenu = QtWidgets.QStackedWidget(self.WorkSpace)
        self.MainMenu.setGeometry(QtCore.QRect(10, 160, 991, 561))
        self.MainMenu.setObjectName("MainMenu")
        self.ViewingTab = QtWidgets.QWidget()
        self.ViewingTab.setObjectName("ViewingTab")
        self.VT_PlaylistsContainer = QtWidgets.QFrame(self.ViewingTab)
        self.VT_PlaylistsContainer.setGeometry(QtCore.QRect(0, 50, 341, 491))
        self.VT_PlaylistsContainer.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"text-align: center;\n"
"")
        self.VT_PlaylistsContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VT_PlaylistsContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VT_PlaylistsContainer.setObjectName("VT_PlaylistsContainer")
        self.VTP_UpButton = QtWidgets.QPushButton(self.VT_PlaylistsContainer)
        self.VTP_UpButton.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.VTP_UpButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.VTP_UpButton.setObjectName("VTP_UpButton")
        self.VTP_DownButton = QtWidgets.QPushButton(self.VT_PlaylistsContainer)
        self.VTP_DownButton.setGeometry(QtCore.QRect(20, 430, 31, 31))
        self.VTP_DownButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.VTP_DownButton.setObjectName("VTP_DownButton")
        self.VTP_SearchInput = QtWidgets.QLineEdit(self.VT_PlaylistsContainer)
        self.VTP_SearchInput.setGeometry(QtCore.QRect(70, 20, 231, 31))
        self.VTP_SearchInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.VTP_SearchInput.setObjectName("VTP_SearchInput")
        self.VTP_AddButton = QtWidgets.QPushButton(self.VT_PlaylistsContainer)
        self.VTP_AddButton.setGeometry(QtCore.QRect(70, 430, 211, 31))
        self.VTP_AddButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.VTP_AddButton.setObjectName("VTP_AddButton")
        self.VTP_Playlist1_Container = QtWidgets.QGroupBox(self.VT_PlaylistsContainer)
        self.VTP_Playlist1_Container.setGeometry(QtCore.QRect(20, 80, 301, 141))
        self.VTP_Playlist1_Container.setObjectName("VTP_Playlist1_Container")
        self.Playlist1_Icon = QtWidgets.QLabel(self.VTP_Playlist1_Container)
        self.Playlist1_Icon.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.Playlist1_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Playlist1_Icon.setText("")
        self.Playlist1_Icon.setObjectName("Playlist1_Icon")
        self.Playlist1_NameLabel = QtWidgets.QLabel(self.VTP_Playlist1_Container)
        self.Playlist1_NameLabel.setGeometry(QtCore.QRect(150, 20, 81, 16))
        self.Playlist1_NameLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Playlist1_NameLabel.setObjectName("Playlist1_NameLabel")
        self.Playlist1_DateCreationLabel = QtWidgets.QLabel(self.VTP_Playlist1_Container)
        self.Playlist1_DateCreationLabel.setGeometry(QtCore.QRect(150, 40, 141, 16))
        self.Playlist1_DateCreationLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Playlist1_DateCreationLabel.setObjectName("Playlist1_DateCreationLabel")
        self.Playlist1_CountVideosLabel = QtWidgets.QLabel(self.VTP_Playlist1_Container)
        self.Playlist1_CountVideosLabel.setGeometry(QtCore.QRect(150, 60, 141, 16))
        self.Playlist1_CountVideosLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Playlist1_CountVideosLabel.setObjectName("Playlist1_CountVideosLabel")
        self.Playlist1_PathLabel = QtWidgets.QLabel(self.VTP_Playlist1_Container)
        self.Playlist1_PathLabel.setGeometry(QtCore.QRect(150, 100, 141, 16))
        self.Playlist1_PathLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Playlist1_PathLabel.setObjectName("Playlist1_PathLabel")
        self.Playlist1_DeleteButton = QtWidgets.QPushButton(self.VTP_Playlist1_Container)
        self.Playlist1_DeleteButton.setGeometry(QtCore.QRect(250, 20, 31, 31))
        self.Playlist1_DeleteButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.Playlist1_DeleteButton.setObjectName("Playlist1_DeleteButton")
        self.Playlist1_EditButton = QtWidgets.QPushButton(self.VTP_Playlist1_Container)
        self.Playlist1_EditButton.setGeometry(QtCore.QRect(250, 60, 31, 31))
        self.Playlist1_EditButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.Playlist1_EditButton.setObjectName("Playlist1_EditButton")
        self.VTP_Playlist1_Container.setVisible(False)

        self.VTP_Playlist2_Container = QtWidgets.QGroupBox(self.VT_PlaylistsContainer)
        self.VTP_Playlist2_Container.setGeometry(QtCore.QRect(20, 250, 301, 141))
        self.VTP_Playlist2_Container.setObjectName("VTP_Playlist2_Container")
        self.Playlist2_Icon = QtWidgets.QLabel(self.VTP_Playlist2_Container)
        self.Playlist2_Icon.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.Playlist2_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Playlist2_Icon.setText("")
        self.Playlist2_Icon.setObjectName("Playlist2_Icon")
        self.Playlist2_NameLabel = QtWidgets.QLabel(self.VTP_Playlist2_Container)
        self.Playlist2_NameLabel.setGeometry(QtCore.QRect(150, 20, 81, 16))
        self.Playlist2_NameLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Playlist2_NameLabel.setObjectName("Playlist2_NameLabel")
        self.Playlist2_DateCreationLabel = QtWidgets.QLabel(self.VTP_Playlist2_Container)
        self.Playlist2_DateCreationLabel.setGeometry(QtCore.QRect(150, 40, 141, 16))
        self.Playlist2_DateCreationLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Playlist2_DateCreationLabel.setObjectName("Playlist2_DateCreationLabel")
        self.Playlist2_CountVideosLabel = QtWidgets.QLabel(self.VTP_Playlist2_Container)
        self.Playlist2_CountVideosLabel.setGeometry(QtCore.QRect(150, 60, 141, 16))
        self.Playlist2_CountVideosLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Playlist2_CountVideosLabel.setObjectName("Playlist2_CountVideosLabel")
        self.Playlist2_PathLabel = QtWidgets.QLabel(self.VTP_Playlist2_Container)
        self.Playlist2_PathLabel.setGeometry(QtCore.QRect(150, 100, 141, 16))
        self.Playlist2_PathLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Playlist2_PathLabel.setObjectName("Playlist2_PathLabel")
        self.Playlist2_DeleteButton = QtWidgets.QPushButton(self.VTP_Playlist2_Container)
        self.Playlist2_DeleteButton.setGeometry(QtCore.QRect(250, 20, 31, 31))
        self.Playlist2_DeleteButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.Playlist2_DeleteButton.setObjectName("Playlist2_DeleteButton")
        self.Playlist2_EditButton = QtWidgets.QPushButton(self.VTP_Playlist2_Container)
        self.Playlist2_EditButton.setGeometry(QtCore.QRect(250, 60, 31, 31))
        self.Playlist2_EditButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.Playlist2_EditButton.setObjectName("Playlist2_EditButton")
        self.VTP_Playlist2_Container.setVisible(False)

        self.VTP_NothingLabel = QtWidgets.QLabel(self.VT_PlaylistsContainer)
        self.VTP_NothingLabel.setGeometry(QtCore.QRect(100, 230, 141, 16))
        self.VTP_NothingLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.VTP_NothingLabel.setObjectName("VTP_NothingLabel")
        self.VT_VideosContainer = QtWidgets.QFrame(self.ViewingTab)
        self.VT_VideosContainer.setGeometry(QtCore.QRect(370, 50, 621, 491))
        self.VT_VideosContainer.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.VT_VideosContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VT_VideosContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VT_VideosContainer.setObjectName("VT_VideosContainer")
        self.VTV_UpButton = QtWidgets.QPushButton(self.VT_VideosContainer)
        self.VTV_UpButton.setGeometry(QtCore.QRect(570, 20, 31, 31))
        self.VTV_UpButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.VTV_UpButton.setObjectName("VTV_UpButton")
        self.VTV_DownButton = QtWidgets.QPushButton(self.VT_VideosContainer)
        self.VTV_DownButton.setGeometry(QtCore.QRect(570, 430, 31, 31))
        self.VTV_DownButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.VTV_DownButton.setObjectName("VTV_DownButton")
        self.VTV_SearchInput = QtWidgets.QLineEdit(self.VT_VideosContainer)
        self.VTV_SearchInput.setGeometry(QtCore.QRect(330, 20, 231, 31))
        self.VTV_SearchInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.VTV_SearchInput.setObjectName("VTV_SearchInput")
        self.VTV_AddButton = QtWidgets.QPushButton(self.VT_VideosContainer)
        self.VTV_AddButton.setGeometry(QtCore.QRect(340, 430, 211, 31))
        self.VTV_AddButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.VTV_AddButton.setObjectName("VTV_AddVideoButton")
        self.VTV_Video1_Container = QtWidgets.QGroupBox(self.VT_VideosContainer)
        self.VTV_Video1_Container.setGeometry(QtCore.QRect(50, 70, 561, 141))
        self.VTV_Video1_Container.setObjectName("VTV_Video1_Container")
        self.Video1_Icon = QtWidgets.QLabel(self.VTV_Video1_Container)
        self.Video1_Icon.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.Video1_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Video1_Icon.setText("")
        self.Video1_Icon.setObjectName("Video1_Icon")
        self.Video1_NameLabel = QtWidgets.QLabel(self.VTV_Video1_Container)
        self.Video1_NameLabel.setGeometry(QtCore.QRect(150, 20, 81, 16))
        self.Video1_NameLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Video1_NameLabel.setObjectName("Video1_NameLabel")
        self.Video1_FormatLabel = QtWidgets.QLabel(self.VTV_Video1_Container)
        self.Video1_FormatLabel.setGeometry(QtCore.QRect(150, 50, 141, 16))
        self.Video1_FormatLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Video1_FormatLabel.setObjectName("Video1_FormatLabel")
        self.Video1_DateUploadLabel = QtWidgets.QLabel(self.VTV_Video1_Container)
        self.Video1_DateUploadLabel.setGeometry(QtCore.QRect(150, 80, 351, 16))
        self.Video1_DateUploadLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Video1_DateUploadLabel.setObjectName("Video1_DateUploadLabel")
        self.Video1_DeleteButton = QtWidgets.QPushButton(self.VTV_Video1_Container)
        self.Video1_DeleteButton.setGeometry(QtCore.QRect(430, 10, 31, 31))
        self.Video1_DeleteButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.Video1_DeleteButton.setObjectName("Video1_DeleteButton")
        self.Video1_EditButton = QtWidgets.QPushButton(self.VTV_Video1_Container)
        self.Video1_EditButton.setGeometry(QtCore.QRect(470, 10, 31, 31))
        self.Video1_EditButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.Video1_EditButton.setObjectName("Video1_EditButton")
        self.Video1_DescriptionLabel = QtWidgets.QLabel(self.VTV_Video1_Container)
        self.Video1_DescriptionLabel.setGeometry(QtCore.QRect(150, 110, 351, 16))
        self.Video1_DescriptionLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Video1_DescriptionLabel.setObjectName("Video1_DescriptionLabel")
        self.VTV_Video2_Container = QtWidgets.QGroupBox(self.VT_VideosContainer)
        self.VTV_Video2_Container.setGeometry(QtCore.QRect(50, 260, 561, 141))
        self.VTV_Video2_Container.setObjectName("VTV_Video2_Container")
        self.Video2_Icon = QtWidgets.QLabel(self.VTV_Video2_Container)
        self.Video2_Icon.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.Video2_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Video2_Icon.setText("")
        self.Video2_Icon.setObjectName("Video2_Icon")
        self.Video2_NameLabel = QtWidgets.QLabel(self.VTV_Video2_Container)
        self.Video2_NameLabel.setGeometry(QtCore.QRect(150, 20, 81, 16))
        self.Video2_NameLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Video2_NameLabel.setObjectName("Video2_NameLabel")
        self.Video2_FormatLabel = QtWidgets.QLabel(self.VTV_Video2_Container)
        self.Video2_FormatLabel.setGeometry(QtCore.QRect(150, 50, 141, 16))
        self.Video2_FormatLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Video2_FormatLabel.setObjectName("Video2_FormatLabel")
        self.Video2_DateUploadLabel = QtWidgets.QLabel(self.VTV_Video2_Container)
        self.Video2_DateUploadLabel.setGeometry(QtCore.QRect(150, 80, 351, 16))
        self.Video2_DateUploadLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Video2_DateUploadLabel.setObjectName("Video2_DateUploadLabel")
        self.Video2_DeleteButton = QtWidgets.QPushButton(self.VTV_Video2_Container)
        self.Video2_DeleteButton.setGeometry(QtCore.QRect(430, 10, 31, 31))
        self.Video2_DeleteButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.Video2_DeleteButton.setObjectName("Video2_DeleteButton")
        self.Video2_EditButton = QtWidgets.QPushButton(self.VTV_Video2_Container)
        self.Video2_EditButton.setGeometry(QtCore.QRect(470, 10, 31, 31))
        self.Video2_EditButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.Video2_EditButton.setObjectName("Video2_EditButton")
        self.Video2_DescriptionLabel = QtWidgets.QLabel(self.VTV_Video2_Container)
        self.Video2_DescriptionLabel.setGeometry(QtCore.QRect(150, 110, 351, 16))
        self.Video2_DescriptionLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Video2_DescriptionLabel.setObjectName("Video2_DescriptionLabel")
        self.VTV_NothingLabel = QtWidgets.QLabel(self.VT_VideosContainer)
        self.VTV_NothingLabel.setGeometry(QtCore.QRect(340, 240, 141, 16))
        self.VTV_NothingLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.VTV_NothingLabel.setObjectName("Playlist1_PathLabel_3")
        self.VT_PlaylistsLabel = QtWidgets.QLabel(self.ViewingTab)
        self.VT_PlaylistsLabel.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.VT_PlaylistsLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.VT_PlaylistsLabel.setObjectName("VT_PlaylistsLabel")
        self.VT_VideosLabel = QtWidgets.QLabel(self.ViewingTab)
        self.VT_VideosLabel.setGeometry(QtCore.QRect(370, 10, 55, 16))
        self.VT_VideosLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.VT_VideosLabel.setObjectName("VT_VideosLabel")
        self.VT_PlaylistsCount = QtWidgets.QLabel(self.ViewingTab)
        self.VT_PlaylistsCount.setGeometry(QtCore.QRect(100, 10, 55, 16))
        self.VT_PlaylistsCount.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.VT_PlaylistsCount.setObjectName("VT_PlaylistsCount")
        self.MainMenu.addWidget(self.ViewingTab)
        self.FindTab = QtWidgets.QWidget()
        self.FindTab.setObjectName("FindTab")
        self.FindTabContainer = QtWidgets.QFrame(self.FindTab)
        self.FindTabContainer.setGeometry(QtCore.QRect(0, 50, 991, 491))
        self.FindTabContainer.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.FindTabContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FindTabContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FindTabContainer.setObjectName("FindTabContainer")
        self.FT_FindButton = QtWidgets.QPushButton(self.FindTabContainer)
        self.FT_FindButton.setGeometry(QtCore.QRect(420, 270, 141, 41))
        self.FT_FindButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.FT_FindButton.setObjectName("FT_FindButton")
        self.FT_URLInput = QtWidgets.QLineEdit(self.FindTabContainer)
        self.FT_URLInput.setGeometry(QtCore.QRect(190, 150, 581, 31))
        self.FT_URLInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.FT_URLInput.setObjectName("FT_URLInput")
        self.FindTabLabel = QtWidgets.QLabel(self.FindTab)
        self.FindTabLabel.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.FindTabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.FindTabLabel.setObjectName("FindTabLabel")
        self.MainMenu.addWidget(self.FindTab)
#         self.SettingsTab = QtWidgets.QWidget()
#         self.SettingsTab.setObjectName("SettingsTab")
#         self.SettingsTabContainer = QtWidgets.QFrame(self.SettingsTab)
#         self.SettingsTabContainer.setGeometry(QtCore.QRect(0, 50, 991, 491))
#         self.SettingsTabContainer.setStyleSheet("background-color: rgb(0, 0, 0);\n"
# "border-radius: 20px;")
#         self.SettingsTabContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.SettingsTabContainer.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.SettingsTabContainer.setObjectName("SettingsTabContainer")
#         self.ST_LanguagesLabel = QtWidgets.QLabel(self.SettingsTabContainer)
#         self.ST_LanguagesLabel.setGeometry(QtCore.QRect(60, 60, 121, 41))
#         self.ST_LanguagesLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
# "color: rgb(255, 255, 255);")
#         self.ST_LanguagesLabel.setObjectName("ST_LanguagesLabel")
#         self.ST_LanguagesBox = QtWidgets.QComboBox(self.SettingsTabContainer)
#         self.ST_LanguagesBox.setGeometry(QtCore.QRect(230, 70, 171, 22))
#         self.ST_LanguagesBox.setStyleSheet("background-color: rgb(85, 85, 127);\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius: 20px;")
#         self.ST_LanguagesBox.setObjectName("ST_LanguagesBox")
#         self.ST_StreamsDASHLabel = QtWidgets.QLabel(self.SettingsTabContainer)
#         self.ST_StreamsDASHLabel.setGeometry(QtCore.QRect(60, 140, 141, 41))
#         self.ST_StreamsDASHLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
# "color: rgb(255, 255, 255);")
#         self.ST_StreamsDASHLabel.setObjectName("ST_StreamsDASHLabel")
#         self.ST_DefaultPlaylistLabel = QtWidgets.QLabel(self.SettingsTabContainer)
#         self.ST_DefaultPlaylistLabel.setGeometry(QtCore.QRect(60, 220, 141, 41))
#         self.ST_DefaultPlaylistLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
# "color: rgb(255, 255, 255);")
#         self.ST_DefaultPlaylistLabel.setObjectName("ST_DefaultPlaylistLabel")
#         self.ST_StreamsDASHButtons = QtWidgets.QGroupBox(self.SettingsTabContainer)
#         self.ST_StreamsDASHButtons.setGeometry(QtCore.QRect(220, 120, 101, 91))
#         self.ST_StreamsDASHButtons.setObjectName("ST_StreamsDASHButtons")
#         self.ST_ActivateDASHButton = QtWidgets.QRadioButton(self.ST_StreamsDASHButtons)
#         self.ST_ActivateDASHButton.setGeometry(QtCore.QRect(10, 20, 158, 13))
#         self.ST_ActivateDASHButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius: 10px;")
#         self.ST_ActivateDASHButton.setObjectName("ST_ActivateDASHButton")
#         self.ST_DeactivateDASHButton = QtWidgets.QRadioButton(self.ST_StreamsDASHButtons)
#         self.ST_DeactivateDASHButton.setGeometry(QtCore.QRect(10, 50, 158, 13))
#         self.ST_DeactivateDASHButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius: 10px;")
#         self.ST_DeactivateDASHButton.setObjectName("ST_DeactivateDASHButton")
#         self.ST_DefaultPlaylistPathInput = QtWidgets.QLineEdit(self.SettingsTabContainer)
#         self.ST_DefaultPlaylistPathInput.setGeometry(QtCore.QRect(230, 220, 411, 31))
#         self.ST_DefaultPlaylistPathInput.setStyleSheet("padding-left: 10px;\n"
# "background-color: rgb(255, 255, 255);\n"
# "border: 3px solid rgb(85, 85, 127);;\n"
# "border-radius: 10px;\n"
# "\n"
# "")
#         self.ST_DefaultPlaylistPathInput.setObjectName("ST_DefaultPlaylistPathInput")
#         self.ST_SaveButton = QtWidgets.QPushButton(self.SettingsTabContainer)
#         self.ST_SaveButton.setGeometry(QtCore.QRect(50, 390, 141, 41))
#         self.ST_SaveButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius: 20px;")
#         self.ST_SaveButton.setObjectName("ST_SaveButton")
#         self.SettingsTabLabel = QtWidgets.QLabel(self.SettingsTab)
#         self.SettingsTabLabel.setGeometry(QtCore.QRect(10, 10, 55, 16))
#         self.SettingsTabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
# "color: rgb(255, 255, 255);")
#         self.SettingsTabLabel.setObjectName("SettingsTabLabel")
#         self.MainMenu.addWidget(self.SettingsTab)
        self.DownloadTab = QtWidgets.QWidget()
        self.DownloadTab.setObjectName("DownloadTab")
        self.DownloadTabContainer = QtWidgets.QFrame(self.DownloadTab)
        self.DownloadTabContainer.setGeometry(QtCore.QRect(0, 50, 991, 491))
        self.DownloadTabContainer.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.DownloadTabContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DownloadTabContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DownloadTabContainer.setObjectName("DownloadTabContainer")
        self.DDT_PlaylistsBox = QtWidgets.QComboBox(self.DownloadTabContainer)
        self.DDT_PlaylistsBox.setGeometry(QtCore.QRect(190, 230, 171, 22))
        self.DDT_PlaylistsBox.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_PlaylistsBox.setObjectName("DDT_PlaylistsBox")
        self.DDT_NameLabel = QtWidgets.QLabel(self.DownloadTabContainer)
        self.DDT_NameLabel.setGeometry(QtCore.QRect(180, 40, 111, 41))
        self.DDT_NameLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_NameLabel.setObjectName("DDT_NameLabel")
        self.DDT_PlaylistsLabel = QtWidgets.QLabel(self.DownloadTabContainer)
        self.DDT_PlaylistsLabel.setGeometry(QtCore.QRect(60, 220, 121, 41))
        self.DDT_PlaylistsLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_PlaylistsLabel.setObjectName("DDT_PlaylistsLabel")
        self.DDT_QualityLabel = QtWidgets.QLabel(self.DownloadTabContainer)
        self.DDT_QualityLabel.setGeometry(QtCore.QRect(60, 270, 141, 41))
        self.DDT_QualityLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_QualityLabel.setObjectName("DDT_QualityLabel")
        self.DDT_FormatLabel = QtWidgets.QLabel(self.DownloadTabContainer)
        self.DDT_FormatLabel.setGeometry(QtCore.QRect(60, 320, 141, 41))
        self.DDT_FormatLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_FormatLabel.setObjectName("DDT_FormatLabel")
        self.DDT_BitrateLabel = QtWidgets.QLabel(self.DownloadTabContainer)
        self.DDT_BitrateLabel.setGeometry(QtCore.QRect(60, 370, 141, 41))
        self.DDT_BitrateLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_BitrateLabel.setObjectName("DDT_BitrateLabel")
        self.DDT_QualityBox = QtWidgets.QComboBox(self.DownloadTabContainer)
        self.DDT_QualityBox.setGeometry(QtCore.QRect(190, 280, 171, 22))
        self.DDT_QualityBox.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_QualityBox.setObjectName("DDT_QualityBox")
        self.DDT_FormatBox = QtWidgets.QComboBox(self.DownloadTabContainer)
        self.DDT_FormatBox.setGeometry(QtCore.QRect(190, 330, 171, 22))
        self.DDT_FormatBox.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_FormatBox.setObjectName("DDT_FormatBox")
        self.DDT_BitrateBox = QtWidgets.QComboBox(self.DownloadTabContainer)
        self.DDT_BitrateBox.setGeometry(QtCore.QRect(190, 380, 171, 22))
        self.DDT_BitrateBox.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_BitrateBox.setObjectName("DDT_BitrateBox")
        self.DDT_DownloadButton = QtWidgets.QPushButton(self.DownloadTabContainer)
        self.DDT_DownloadButton.setGeometry(QtCore.QRect(620, 360, 141, 41))
        self.DDT_DownloadButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_DownloadButton.setObjectName("DDT_DownloadButton")
        self.DDT_NameInput = QtWidgets.QLineEdit(self.DownloadTabContainer)
        self.DDT_NameInput.setGeometry(QtCore.QRect(170, 90, 411, 31))
        self.DDT_NameInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.DDT_NameInput.setObjectName("DDT_NameInput")
        self.DDT_CancelButton = QtWidgets.QPushButton(self.DownloadTabContainer)
        self.DDT_CancelButton.setGeometry(QtCore.QRect(450, 360, 141, 41))
        self.DDT_CancelButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_CancelButton.setObjectName("DDT_CancelButton")
        self.DDT_Icon = QtWidgets.QLabel(self.DownloadTabContainer)
        self.DDT_Icon.setGeometry(QtCore.QRect(30, 50, 121, 121))
        self.DDT_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_Icon.setText("")
        self.DDT_Icon.setObjectName("DDT_Icon")
        self.DownloadTabLabel = QtWidgets.QLabel(self.DownloadTab)
        self.DownloadTabLabel.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.DownloadTabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.DownloadTabLabel.setObjectName("DownloadTabLabel")
        self.MainMenu.addWidget(self.DownloadTab)
        self.EditPlaylistTab = QtWidgets.QWidget()
        self.EditPlaylistTab.setObjectName("EditPlaylistTab")
        self.EditPlaylistTabContainer = QtWidgets.QFrame(self.EditPlaylistTab)
        self.EditPlaylistTabContainer.setGeometry(QtCore.QRect(0, 50, 991, 491))
        self.EditPlaylistTabContainer.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.EditPlaylistTabContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EditPlaylistTabContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EditPlaylistTabContainer.setObjectName("EditPlaylistTabContainer")
        self.EP_IconLabel = QtWidgets.QLabel(self.EditPlaylistTabContainer)
        self.EP_IconLabel.setGeometry(QtCore.QRect(60, 10, 121, 41))
        self.EP_IconLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EP_IconLabel.setObjectName("EP_IconLabel")
        self.EP_NameLabel = QtWidgets.QLabel(self.EditPlaylistTabContainer)
        self.EP_NameLabel.setGeometry(QtCore.QRect(200, 10, 91, 41))
        self.EP_NameLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EP_NameLabel.setObjectName("EP_NameLabel")
        self.EP_ChangeButton = QtWidgets.QPushButton(self.EditPlaylistTabContainer)
        self.EP_ChangeButton.setGeometry(QtCore.QRect(20, 180, 141, 41))
        self.EP_ChangeButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EP_ChangeButton.setObjectName("EP_ChangeButton")
        self.EP_PathLabel = QtWidgets.QLabel(self.EditPlaylistTabContainer)
        self.EP_PathLabel.setGeometry(QtCore.QRect(200, 100, 91, 41))
        self.EP_PathLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EP_PathLabel.setObjectName("EP_PathLabel")
        self.EP_CancelButton = QtWidgets.QPushButton(self.EditPlaylistTabContainer)
        self.EP_CancelButton.setGeometry(QtCore.QRect(190, 230, 141, 41))
        self.EP_CancelButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EP_CancelButton.setObjectName("EP_CancelButton")
        self.EP_SaveButton = QtWidgets.QPushButton(self.EditPlaylistTabContainer)
        self.EP_SaveButton.setGeometry(QtCore.QRect(370, 230, 141, 41))
        self.EP_SaveButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EP_SaveButton.setObjectName("EP_SaveButton")
        self.EP_NameInput = QtWidgets.QLineEdit(self.EditPlaylistTabContainer)
        self.EP_NameInput.setGeometry(QtCore.QRect(190, 50, 411, 31))
        self.EP_NameInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.EP_NameInput.setObjectName("EP_NameInput")
        self.EP_PathInput = QtWidgets.QLineEdit(self.EditPlaylistTabContainer)
        self.EP_PathInput.setGeometry(QtCore.QRect(190, 150, 411, 31))
        self.EP_PathInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.EP_PathInput.setObjectName("EP_PathInput")
        self.EP_Icon = QtWidgets.QLabel(self.EditPlaylistTabContainer)
        self.EP_Icon.setGeometry(QtCore.QRect(30, 50, 121, 121))
        self.EP_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EP_Icon.setText("")
        self.EP_Icon.setObjectName("EP_Icon")
        self.EditPlaylistTabLabel = QtWidgets.QLabel(self.EditPlaylistTab)
        self.EditPlaylistTabLabel.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.EditPlaylistTabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.EditPlaylistTabLabel.setObjectName("EditPlaylistTabLabel")
        self.MainMenu.addWidget(self.EditPlaylistTab)
        self.EditVideoTab = QtWidgets.QWidget()
        self.EditVideoTab.setObjectName("EditVideoTab")
        self.EditVideoTabLabel = QtWidgets.QLabel(self.EditVideoTab)
        self.EditVideoTabLabel.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.EditVideoTabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.EditVideoTabLabel.setObjectName("EditVideoTabLabel")
        self.EditVideoTabContainer = QtWidgets.QFrame(self.EditVideoTab)
        self.EditVideoTabContainer.setGeometry(QtCore.QRect(0, 50, 991, 491))
        self.EditVideoTabContainer.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.EditVideoTabContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EditVideoTabContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EditVideoTabContainer.setObjectName("EditVideoTabContainer")
        self.EV_IconLabel = QtWidgets.QLabel(self.EditVideoTabContainer)
        self.EV_IconLabel.setGeometry(QtCore.QRect(60, 10, 121, 41))
        self.EV_IconLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EV_IconLabel.setObjectName("EV_IconLabel")
        self.EV_PlaylistsBox = QtWidgets.QComboBox(self.EditVideoTabContainer)
        self.EV_PlaylistsBox.setGeometry(QtCore.QRect(340, 190, 171, 22))
        self.EV_PlaylistsBox.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EV_PlaylistsBox.setObjectName("EV_PlaylistsBox")
        self.EV_NameLabel = QtWidgets.QLabel(self.EditVideoTabContainer)
        self.EV_NameLabel.setGeometry(QtCore.QRect(200, 10, 91, 41))
        self.EV_NameLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EV_NameLabel.setObjectName("EV_NameLabel")
        self.EV_PlaylistsLabel = QtWidgets.QLabel(self.EditVideoTabContainer)
        self.EV_PlaylistsLabel.setGeometry(QtCore.QRect(200, 180, 121, 41))
        self.EV_PlaylistsLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EV_PlaylistsLabel.setObjectName("EV_PlaylistsLabel")
        self.EV_SaveButton = QtWidgets.QPushButton(self.EditVideoTabContainer)
        self.EV_SaveButton.setGeometry(QtCore.QRect(370, 290, 141, 41))
        self.EV_SaveButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EV_SaveButton.setObjectName("EV_SaveButton")
        self.EV_ChangeButton = QtWidgets.QPushButton(self.EditVideoTabContainer)
        self.EV_ChangeButton.setGeometry(QtCore.QRect(20, 180, 141, 41))
        self.EV_ChangeButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EV_ChangeButton.setObjectName("EV_ChangeButton")
        self.EV_DescriptionLabel = QtWidgets.QLabel(self.EditVideoTabContainer)
        self.EV_DescriptionLabel.setGeometry(QtCore.QRect(200, 90, 91, 31))
        self.EV_DescriptionLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EV_DescriptionLabel.setObjectName("EV_DescriptionLabel")
        self.EV_CancelButton = QtWidgets.QPushButton(self.EditVideoTabContainer)
        self.EV_CancelButton.setGeometry(QtCore.QRect(190, 290, 141, 41))
        self.EV_CancelButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EV_CancelButton.setObjectName("EV_CancelButton")
        self.EV_NameInput = QtWidgets.QLineEdit(self.EditVideoTabContainer)
        self.EV_NameInput.setGeometry(QtCore.QRect(200, 50, 411, 31))
        self.EV_NameInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.EV_NameInput.setObjectName("EV_NameInput")
        self.EV_DescriptionInput = QtWidgets.QLineEdit(self.EditVideoTabContainer)
        self.EV_DescriptionInput.setGeometry(QtCore.QRect(200, 130, 411, 31))
        self.EV_DescriptionInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.EV_DescriptionInput.setObjectName("EV_DescriptionInput")
        self.EV_Icon = QtWidgets.QLabel(self.EditVideoTabContainer)
        self.EV_Icon.setGeometry(QtCore.QRect(30, 50, 121, 121))
        self.EV_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EV_Icon.setText("")
        self.EV_Icon.setObjectName("EV_Icon")
        self.MainMenu.addWidget(self.EditVideoTab)
        self.DialogTab = QtWidgets.QWidget()
        self.DialogTab.setObjectName("DialogTab")
        self.DialogTabContainer = QtWidgets.QFrame(self.DialogTab)
        self.DialogTabContainer.setGeometry(QtCore.QRect(0, 50, 991, 491))
        self.DialogTabContainer.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.DialogTabContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DialogTabContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DialogTabContainer.setObjectName("DialogTabContainer")
        self.DT_TextLabel = QtWidgets.QLabel(self.DialogTabContainer)
        self.DT_TextLabel.setGeometry(QtCore.QRect(350, 190, 111, 41))
        self.DT_TextLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DT_TextLabel.setObjectName("DT_TextLabel")
        self.DT_AcceptButton = QtWidgets.QPushButton(self.DialogTabContainer)
        self.DT_AcceptButton.setGeometry(QtCore.QRect(430, 360, 141, 41))
        self.DT_AcceptButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DT_AcceptButton.setObjectName("DT_AcceptButton")
        self.DT_CancelButton = QtWidgets.QPushButton(self.DialogTabContainer)
        self.DT_CancelButton.setGeometry(QtCore.QRect(250, 360, 141, 41))
        self.DT_CancelButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DT_CancelButton.setObjectName("DT_CancelButton")
        self.DT_DetailsLabel = QtWidgets.QLabel(self.DialogTabContainer)
        self.DT_DetailsLabel.setGeometry(QtCore.QRect(370, 220, 111, 41))
        self.DT_DetailsLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DT_DetailsLabel.setObjectName("DT_DetailsLabel")
        self.DialogTabLabel = QtWidgets.QLabel(self.DialogTab)
        self.DialogTabLabel.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.DialogTabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.DialogTabLabel.setObjectName("DialogTabLabel")
        self.MainMenu.addWidget(self.DialogTab)
        self.window.setCentralWidget(self.WorkSpace)

        self.retranslate(self.window)
        self.MainMenu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.window)

        self.VTV_Video1_Container.setVisible(False)
        self.VTV_Video2_Container.setVisible(False)
        self.VTP_SearchInput.setVisible(False)
        self.VTV_SearchInput.setVisible(False)

    def setupGraphicalEvents(self):
        # self.Playlist1_Icon.mousePressEvent = lambda event: self.hide()
        self.PlaylistsTabButton.enterEvent = lambda event: self.highlightItem(self.PlaylistsTabButton, self.px_low)
        self.PlaylistsTabButton.leaveEvent = lambda event: self.unhighlightItem(self.PlaylistsTabButton, self.px_low)
        self.FindTabButton.enterEvent = lambda event: self.highlightItem(self.FindTabButton, self.px_low)
        self.FindTabButton.leaveEvent = lambda event: self.unhighlightItem(self.FindTabButton, self.px_low)
        # self.SettingsTabButton.enterEvent = lambda event: self.highlightItem(self.SettingsTabButton)
        # self.SettingsTabButton.leaveEvent = lambda event: self.unhighlightItem(self.SettingsTabButton)

        self.VTP_AddButton.enterEvent = lambda event: self.highlightItem(self.VTP_AddButton, self.px_low)
        self.VTP_AddButton.leaveEvent = lambda event: self.unhighlightItem(self.VTP_AddButton, self.px_low)
        self.VTP_UpButton.enterEvent = lambda event: self.highlightItem(self.VTP_UpButton, self.px_low)
        self.VTP_UpButton.leaveEvent = lambda event: self.unhighlightItem(self.VTP_UpButton, self.px_low)
        self.VTP_DownButton.enterEvent = lambda event: self.highlightItem(self.VTP_DownButton, self.px_low)
        self.VTP_DownButton.leaveEvent = lambda event: self.unhighlightItem(self.VTP_DownButton, self.px_low)

        self.Playlist1_Icon.enterEvent = lambda event: self.highlightItem(self.Playlist1_Icon, self.px_low)
        self.Playlist1_Icon.leaveEvent = lambda event: self.unhighlightItem(self.Playlist1_Icon, self.px_low)
        self.Playlist1_EditButton.enterEvent = lambda event: self.highlightItem(self.Playlist1_EditButton, self.px_low)
        self.Playlist1_EditButton.leaveEvent = lambda event: self.unhighlightItem(self.Playlist1_EditButton, self.px_low)
        self.Playlist1_DeleteButton.enterEvent = lambda event: self.highlightItem(self.Playlist1_DeleteButton, self.px_low)
        self.Playlist1_DeleteButton.leaveEvent = lambda event: self.unhighlightItem(self.Playlist1_DeleteButton, self.px_low)

        self.Playlist2_Icon.enterEvent = lambda event: self.highlightItem(self.Playlist2_Icon, self.px_low)
        self.Playlist2_Icon.leaveEvent = lambda event: self.unhighlightItem(self.Playlist2_Icon, self.px_low)
        self.Playlist2_EditButton.enterEvent = lambda event: self.highlightItem(self.Playlist2_EditButton, self.px_low)
        self.Playlist2_EditButton.leaveEvent = lambda event: self.unhighlightItem(self.Playlist2_EditButton, self.px_low)
        self.Playlist2_DeleteButton.enterEvent = lambda event: self.highlightItem(self.Playlist2_DeleteButton, self.px_low)
        self.Playlist2_DeleteButton.leaveEvent = lambda event: self.unhighlightItem(self.Playlist2_DeleteButton, self.px_low)

        self.VTV_AddButton.enterEvent = lambda event: self.highlightItem(self.VTV_AddButton, self.px_low)
        self.VTV_AddButton.leaveEvent = lambda event: self.unhighlightItem(self.VTV_AddButton, self.px_low)
        self.VTV_UpButton.enterEvent = lambda event: self.highlightItem(self.VTV_UpButton, self.px_low)
        self.VTV_UpButton.leaveEvent = lambda event: self.unhighlightItem(self.VTV_UpButton, self.px_low)
        self.VTV_DownButton.enterEvent = lambda event: self.highlightItem(self.VTV_DownButton, self.px_low)
        self.VTV_DownButton.leaveEvent = lambda event: self.unhighlightItem(self.VTV_DownButton, self.px_low)

        self.Video1_Icon.enterEvent = lambda event: self.highlightItem(self.Video1_Icon, self.px_low)
        self.Video1_Icon.leaveEvent = lambda event: self.unhighlightItem(self.Video1_Icon, self.px_low)
        self.Video1_EditButton.enterEvent = lambda event: self.highlightItem(self.Video1_EditButton, self.px_low)
        self.Video1_EditButton.leaveEvent = lambda event: self.unhighlightItem(self.Video1_EditButton, self.px_low)
        self.Video1_DeleteButton.enterEvent = lambda event: self.highlightItem(self.Video1_DeleteButton, self.px_low)
        self.Video1_DeleteButton.leaveEvent = lambda event: self.unhighlightItem(self.Video1_DeleteButton, self.px_low)

        self.Video2_Icon.enterEvent = lambda event: self.highlightItem(self.Video2_Icon, self.px_low)
        self.Video2_Icon.leaveEvent = lambda event: self.unhighlightItem(self.Video2_Icon, self.px_low)
        self.Video2_EditButton.enterEvent = lambda event: self.highlightItem(self.Video2_EditButton, self.px_low)
        self.Video2_EditButton.leaveEvent = lambda event: self.unhighlightItem(self.Video2_EditButton, self.px_low)
        self.Video2_DeleteButton.enterEvent = lambda event: self.highlightItem(self.Video2_DeleteButton, self.px_low)
        self.Video2_DeleteButton.leaveEvent = lambda event: self.unhighlightItem(self.Video2_DeleteButton, self.px_low)

        self.FT_FindButton.enterEvent = lambda event: self.highlightItem(self.FT_FindButton, self.px_low)
        self.FT_FindButton.leaveEvent = lambda event: self.unhighlightItem(self.FT_FindButton, self.px_low)


        # self.ST_LanguagesBox.enterEvent = lambda event: self.highlightItem(self.ST_LanguagesBox)
        # self.ST_LanguagesBox.leaveEvent = lambda event: self.unhighlightItem(self.ST_LanguagesBox)
        # self.ST_SaveButton.enterEvent = lambda event: self.highlightItem(self.ST_SaveButton)
        # self.ST_SaveButton.leaveEvent = lambda event: self.unhighlightItem(self.ST_SaveButton)

    def retranslate(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YTSaver"))
        self.AppMessagerOutput.setText(_translate("MainWindow", "SysMsg"))
        self.PlaylistsTabButton.setText(_translate("MainWindow", "Playlists"))
        self.FindTabButton.setText(_translate("MainWindow", "Download"))
        # self.SettingsTabButton.setText(_translate("MainWindow", "Settings"))
        self.VTP_UpButton.setText(_translate("MainWindow", "↑"))
        self.VTP_DownButton.setText(_translate("MainWindow", "↓"))
        self.VTP_SearchInput.setText(_translate("MainWindow", "Default"))
        self.VTP_AddButton.setText(_translate("MainWindow", "Add"))
        self.VTP_Playlist1_Container.setTitle(_translate("MainWindow", "GroupBox"))
        self.Playlist1_NameLabel.setText(_translate("MainWindow", "PlaylistName"))
        self.Playlist1_DateCreationLabel.setText(_translate("MainWindow", "10.01.2003"))
        self.Playlist1_CountVideosLabel.setText(_translate("MainWindow", "59 videos"))
        self.Playlist1_PathLabel.setText(_translate("MainWindow", "C:/USERS/DOCUMENTS/"))
        self.Playlist1_DeleteButton.setText(_translate("MainWindow", "×"))
        self.Playlist1_EditButton.setText(_translate("MainWindow", "ed"))
        self.VTP_Playlist2_Container.setTitle(_translate("MainWindow", "GroupBox"))
        self.Playlist2_NameLabel.setText(_translate("MainWindow", "PlaylistName"))
        self.Playlist2_DateCreationLabel.setText(_translate("MainWindow", "10.01.2003"))
        self.Playlist2_CountVideosLabel.setText(_translate("MainWindow", "59 videos"))
        self.Playlist2_PathLabel.setText(_translate("MainWindow", "C:/USERS/DOCUMENTS/"))
        self.Playlist2_DeleteButton.setText(_translate("MainWindow", "×"))
        self.Playlist2_EditButton.setText(_translate("MainWindow", "ed"))
        self.VTP_NothingLabel.setText(_translate("MainWindow", "nothing found"))
        self.VTV_UpButton.setText(_translate("MainWindow", "↑"))
        self.VTV_DownButton.setText(_translate("MainWindow", "↓"))
        self.VTV_SearchInput.setText(_translate("MainWindow", "Default"))
        self.VTV_AddButton.setText(_translate("MainWindow", "Add"))
        self.VTV_Video1_Container.setTitle(_translate("MainWindow", "GroupBox"))
        self.Video1_NameLabel.setText(_translate("MainWindow", "VideoName"))
        self.Video1_FormatLabel.setText(_translate("MainWindow", "mp4"))
        self.Video1_DateUploadLabel.setText(_translate("MainWindow", "10.01.2003"))
        self.Video1_DeleteButton.setText(_translate("MainWindow", "×"))
        self.Video1_EditButton.setText(_translate("MainWindow", "ed"))
        self.Video1_DescriptionLabel.setText(_translate("MainWindow", "Video description: dsssssssssssssssssf fffffffffffffffff"))
        self.VTV_Video2_Container.setTitle(_translate("MainWindow", "GroupBox"))
        self.Video2_NameLabel.setText(_translate("MainWindow", "VideoName"))
        self.Video2_FormatLabel.setText(_translate("MainWindow", "mp4"))
        self.Video2_DateUploadLabel.setText(_translate("MainWindow", "10.01.2003"))
        self.Video2_DeleteButton.setText(_translate("MainWindow", "×"))
        self.Video2_EditButton.setText(_translate("MainWindow", "ed"))
        self.Video2_DescriptionLabel.setText(_translate("MainWindow", "Video description: dsssssssssssssssssf fffffffffffffffff"))
        self.VTV_NothingLabel.setText(_translate("MainWindow", "nothing found"))
        self.VT_PlaylistsLabel.setText(_translate("MainWindow", "Playlists Count:"))
        self.VT_VideosLabel.setText(_translate("MainWindow", "Videos:"))
        self.VT_PlaylistsCount.setText(_translate("MainWindow", "2"))
        self.FT_FindButton.setText(_translate("MainWindow", "Find"))
        self.FT_URLInput.setText(_translate("MainWindow", "url"))
        self.FindTabLabel.setText(_translate("MainWindow", "Find"))
        # self.ST_LanguagesLabel.setText(_translate("MainWindow", "Language"))
        # self.ST_StreamsDASHLabel.setText(_translate("MainWindow", "Allow DASH streams catch:"))
        # self.ST_DefaultPlaylistLabel.setText(_translate("MainWindow", "Default playlist"))
        # self.ST_StreamsDASHButtons.setTitle(_translate("MainWindow", "GroupBox"))
        # self.ST_ActivateDASHButton.setText(_translate("MainWindow", "Yes"))
        # self.ST_DeactivateDASHButton.setText(_translate("MainWindow", "No"))
        # self.ST_DefaultPlaylistPathInput.setText(_translate("MainWindow", "path"))
        # self.ST_SaveButton.setText(_translate("MainWindow", "save"))
        # self.SettingsTabLabel.setText(_translate("MainWindow", "Settings"))
        self.DDT_NameLabel.setText(_translate("MainWindow", "Video name:"))
        self.DDT_PlaylistsLabel.setText(_translate("MainWindow", "Сhoose playlist:"))
        self.DDT_QualityLabel.setText(_translate("MainWindow", "Сhoose quality:"))
        self.DDT_FormatLabel.setText(_translate("MainWindow", "Сhoose format:"))
        self.DDT_BitrateLabel.setText(_translate("MainWindow", "Сhoose bitrate:"))
        self.DDT_DownloadButton.setText(_translate("MainWindow", "download video"))
        self.DDT_NameInput.setText(_translate("MainWindow", "path"))
        self.DDT_CancelButton.setText(_translate("MainWindow", "cancel"))
        self.DownloadTabLabel.setText(_translate("MainWindow", "DownloadProperties"))
        self.EP_IconLabel.setText(_translate("MainWindow", "playlist icon:"))
        self.EP_NameLabel.setText(_translate("MainWindow", "playlist name:"))
        self.EP_ChangeButton.setText(_translate("MainWindow", "change"))
        self.EP_PathLabel.setText(_translate("MainWindow", "playlist path:"))
        self.EP_CancelButton.setText(_translate("MainWindow", "cancel"))
        self.EP_SaveButton.setText(_translate("MainWindow", "save"))
        self.EP_NameInput.setText(_translate("MainWindow", "path"))
        self.EP_PathInput.setText(_translate("MainWindow", "path"))
        self.EditPlaylistTabLabel.setText(_translate("MainWindow", "Edit playlist"))
        self.EditVideoTabLabel.setText(_translate("MainWindow", "Edit Video Info"))
        self.EV_IconLabel.setText(_translate("MainWindow", "Video icon:"))
        self.EV_NameLabel.setText(_translate("MainWindow", "video name:"))
        self.EV_PlaylistsLabel.setText(_translate("MainWindow", "Сhoose playlist:"))
        self.EV_SaveButton.setText(_translate("MainWindow", "save"))
        self.EV_ChangeButton.setText(_translate("MainWindow", "change"))
        self.EV_DescriptionLabel.setText(_translate("MainWindow", "video description:"))
        self.EV_CancelButton.setText(_translate("MainWindow", "cancel"))
        self.EV_NameInput.setText(_translate("MainWindow", "name"))
        self.EV_DescriptionInput.setText(_translate("MainWindow", "desc"))
        self.DT_TextLabel.setText(_translate("MainWindow", "Are you shure to"))
        self.DT_AcceptButton.setText(_translate("MainWindow", "shure"))
        self.DT_CancelButton.setText(_translate("MainWindow", "cancel"))
        self.DT_DetailsLabel.setText(_translate("MainWindow", "details?"))
        self.DialogTabLabel.setText(_translate("MainWindow", "Warning"))

    def showMainWindow(self, allow):
        if allow:
            self.window.show()
        else:
            self.window.hide()

    def highlightItem(self, item, px):
        current_style = item.styleSheet()
        new_style = current_style + f";border: {px}px solid white;"
        item.setStyleSheet(new_style)

    def unhighlightItem(self, item, px):
        current_style = item.styleSheet()
        new_style = current_style.replace(f"border: {px}px solid white;", "")
        item.setStyleSheet(new_style)



    def set_playlist1_info(self, playlist_info):
        self.Playlist1_NameLabel.setText(str(playlist_info[1]))
        self.Playlist1_CountVideosLabel.setText(str(playlist_info[2]))
        self.Playlist1_PathLabel.setText(str(playlist_info[3]))
        self.Playlist1_DateCreationLabel.setText(str(playlist_info[5]))

    def set_playlist2_info(self, playlist_info):
        self.Playlist2_NameLabel.setText(str(playlist_info[1]))
        self.Playlist2_CountVideosLabel.setText(str(playlist_info[2]))
        self.Playlist2_PathLabel.setText(str(playlist_info[3]))
        self.Playlist2_DateCreationLabel.setText(str(playlist_info[5]))

