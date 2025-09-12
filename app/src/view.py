from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication as AppQT,  QFileDialog
from player import VideoPlayer
import os

class View():

    def __init__(self):
        self.px_low = 2
        self.px_medium = 4
        self.player = None
        self.controller = None

        self.app = AppQT([])
        self.window = QtWidgets.QMainWindow()
        self.window.setObjectName("MainWindow")
        self.window.resize(800, 600)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.window.sizePolicy().hasHeightForWidth())
        self.window.setSizePolicy(self.sizePolicy)
        self.window.setMinimumSize(QtCore.QSize(800, 600))
        self.window.setMaximumSize(QtCore.QSize(800, 600))

        self.window.setStyleSheet("border-color: rgb(255, 16, 80);")
        self.WorkSpace = QtWidgets.QWidget(self.window)
        self.WorkSpace.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 85, 127);")
        self.WorkSpace.setObjectName("WorkSpace")
        self.AppMessagerBar = QtWidgets.QFrame(self.WorkSpace)
        self.AppMessagerBar.setGeometry(QtCore.QRect(0, 10, 801, 71))
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
        self.AppMessagerOutput.setGeometry(QtCore.QRect(110, 30, 585, 16))
        self.AppMessagerOutput.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.AppMessagerOutput.setObjectName("AppMessagerOutput")
        self.ControlButtonsBar = QtWidgets.QFrame(self.WorkSpace)
        self.ControlButtonsBar.setGeometry(QtCore.QRect(-10, 90, 811, 61))
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
        self.VideosTabButton = QtWidgets.QPushButton(self.ControlButtonsBar)
        self.VideosTabButton.setGeometry(QtCore.QRect(20, 10, 141, 41))
        self.VideosTabButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.VideosTabButton.setObjectName("VideosTabButton")
        self.DownloadTabButton = QtWidgets.QPushButton(self.ControlButtonsBar)
        self.DownloadTabButton.setGeometry(QtCore.QRect(180, 10, 141, 41))
        self.DownloadTabButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DownloadTabButton.setObjectName("DownloadTabButton")
        self.MainMenu = QtWidgets.QStackedWidget(self.WorkSpace)
        self.MainMenu.setGeometry(QtCore.QRect(10, 160, 791, 441))
        self.MainMenu.setObjectName("MainMenu")
        self.VideoTab = QtWidgets.QWidget()
        self.VideoTab.setObjectName("VideoTab")
        self.VID_Container = QtWidgets.QFrame(self.VideoTab)
        self.VID_Container.setGeometry(QtCore.QRect(0, 50, 781, 371))
        self.VID_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "border-radius: 20px;\n"
                                         "text-align: center;\n"
                                         "")
        self.VID_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VID_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VID_Container.setObjectName("VID_Container")
        self.VID_UpButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_UpButton.setGeometry(QtCore.QRect(20, 30, 31, 61))
        self.VID_UpButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px\n"
                                        "")
        self.VID_UpButton.setObjectName("VID_UpButton")
        self.VID_DownButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_DownButton.setGeometry(QtCore.QRect(20, 250, 31, 61))
        self.VID_DownButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 10px\n"
                                          "")
        self.VID_DownButton.setObjectName("VID_DownButton")
        self.VID1_Container = QtWidgets.QGroupBox(self.VID_Container)
        self.VID1_Container.setGeometry(QtCore.QRect(120, 20, 451, 141))
        self.VID1_Container.setObjectName("VID1_Container")
        self.VID1_Icon = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_Icon.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.VID1_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 20px;")
        self.VID1_Icon.setText("")
        self.VID1_Icon.setObjectName("VID1_Icon")
        self.VID1_NameLabel = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_NameLabel.setGeometry(QtCore.QRect(150, 20, 281, 16))
        self.VID1_NameLabel.setStyleSheet("\n"
                                          "color: rgb(255, 255, 255);")
        self.VID1_NameLabel.setObjectName("VID1_NameLabel")
        self.VID1_DateCreationLabel = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_DateCreationLabel.setGeometry(QtCore.QRect(150, 40, 141, 16))
        self.VID1_DateCreationLabel.setStyleSheet("\n"
                                                  "color: rgb(255, 255, 255);")
        self.VID1_DateCreationLabel.setObjectName("VID1_DateCreationLabel")
        self.VID1_DescriptionLabel = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_DescriptionLabel.setGeometry(QtCore.QRect(150, 60, 301, 16))
        self.VID1_DescriptionLabel.setStyleSheet("\n"
                                                 "color: rgb(255, 255, 255);")
        self.VID1_DescriptionLabel.setObjectName("VID1_DescriptionLabel")
        self.VID1_PathLabel = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_PathLabel.setGeometry(QtCore.QRect(150, 100, 301, 16))
        self.VID1_PathLabel.setStyleSheet("\n"
                                          "color: rgb(255, 255, 255);")
        self.VID1_PathLabel.setObjectName("VID1_PathLabel")
        self.VID2_Container = QtWidgets.QGroupBox(self.VID_Container)
        self.VID2_Container.setGeometry(QtCore.QRect(120, 190, 451, 141))
        self.VID2_Container.setObjectName("VID2_Container")
        self.VID2_Icon = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_Icon.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.VID2_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 20px;")
        self.VID2_Icon.setText("")
        self.VID2_Icon.setObjectName("VID2_Icon")
        self.VID2_NameLabel = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_NameLabel.setGeometry(QtCore.QRect(150, 20, 301, 16))
        self.VID2_NameLabel.setStyleSheet("\n"
                                          "color: rgb(255, 255, 255);")
        self.VID2_NameLabel.setObjectName("VID2_NameLabel")
        self.VID2_DateCreationLabel = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_DateCreationLabel.setGeometry(QtCore.QRect(150, 40, 141, 16))
        self.VID2_DateCreationLabel.setStyleSheet("\n"
                                                  "color: rgb(255, 255, 255);")
        self.VID2_DateCreationLabel.setObjectName("VID2_DateCreationLabel")
        self.VID2_DescriptionLabel = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_DescriptionLabel.setGeometry(QtCore.QRect(150, 60, 301, 16))
        self.VID2_DescriptionLabel.setStyleSheet("\n"
                                                 "color: rgb(255, 255, 255);")
        self.VID2_DescriptionLabel.setObjectName("VID2_DescriptionLabel")
        self.VID2_PathLabel = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_PathLabel.setGeometry(QtCore.QRect(150, 100, 301, 16))
        self.VID2_PathLabel.setStyleSheet("\n"
                                          "color: rgb(255, 255, 255);")
        self.VID2_PathLabel.setObjectName("VID2_PathLabel")
        self.VID_NothingLabel = QtWidgets.QLabel(self.VID_Container)
        self.VID_NothingLabel.setGeometry(QtCore.QRect(270, 170, 141, 16))
        self.VID_NothingLabel.setStyleSheet("\n"
                                            "color: rgb(255, 255, 255);")
        self.VID_NothingLabel.setObjectName("VID_NothingLabel")
        self.VID_WatchButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_WatchButton.setGeometry(QtCore.QRect(600, 90, 141, 31))
        self.VID_WatchButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 10px\n"
                                           "")
        self.VID_WatchButton.setObjectName("VID_WatchButton")
        self.VID_DeleteButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_DeleteButton.setGeometry(QtCore.QRect(600, 150, 141, 31))
        self.VID_DeleteButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 10px\n"
                                            "")
        self.VID_DeleteButton.setObjectName("VID_DeleteButton")
        self.VID_EditButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_EditButton.setGeometry(QtCore.QRect(600, 210, 141, 31))
        self.VID_EditButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 10px\n"
                                          "")
        self.VID_EditButton.setObjectName("VID_EditButton")
        self.VID1_NameLabel_2 = QtWidgets.QLabel(self.VID_Container)
        self.VID1_NameLabel_2.setGeometry(QtCore.QRect(640, 40, 81, 16))
        self.VID1_NameLabel_2.setStyleSheet("\n"
                                            "color: rgb(255, 255, 255);")
        self.VID1_NameLabel_2.setObjectName("VID1_NameLabel_2")
        self.VID_TabLabel = QtWidgets.QLabel(self.VideoTab)
        self.VID_TabLabel.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.VID_TabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.VID_TabLabel.setObjectName("VID_TabLabel")
        self.VID_CountValue = QtWidgets.QLabel(self.VideoTab)
        self.VID_CountValue.setGeometry(QtCore.QRect(170, 10, 55, 16))
        self.VID_CountValue.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);")
        self.VID_CountValue.setObjectName("VID_CountValue")
        self.MainMenu.addWidget(self.VideoTab)

        self.PreviewTab = QtWidgets.QWidget()
        self.PreviewTab.setObjectName("PreviewTab")
        self.PT_Container = QtWidgets.QFrame(self.PreviewTab)
        self.PT_Container.setGeometry(QtCore.QRect(0, 0, 781, 421))
        self.PT_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "border-radius: 20px;")
        self.PT_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PT_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PT_Container.setObjectName("PT_Container")
        self.PT_CancelButton = QtWidgets.QPushButton(self.PT_Container)
        self.PT_CancelButton.setGeometry(QtCore.QRect(30, 360, 141, 41))
        self.PT_CancelButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 20px;")
        self.PT_CancelButton.setObjectName("PT_CancelButton")
        self.PT_Video = QtWidgets.QLabel(self.PT_Container)
        self.PT_Video.setGeometry(QtCore.QRect(20, 20, 741, 321))
        self.PT_Video.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 20px;")
        self.PT_Video.setText("")
        self.PT_Video.setObjectName("PT_Video")
        self.PT_StopOrPlayButton = QtWidgets.QPushButton(self.PT_Container)
        self.PT_StopOrPlayButton.setGeometry(QtCore.QRect(190, 360, 141, 41))
        self.PT_StopOrPlayButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-radius: 20px;")
        self.PT_StopOrPlayButton.setObjectName("PT_StopOrPlayButton")
        self.PT_ShipForwardButton = QtWidgets.QPushButton(self.PT_Container)
        self.PT_ShipForwardButton.setGeometry(QtCore.QRect(590, 360, 141, 41))
        self.PT_ShipForwardButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "border-radius: 20px;")
        self.PT_ShipForwardButton.setObjectName("PT_ShipForwardButton")
        self.PT_SkipBackButton = QtWidgets.QPushButton(self.PT_Container)
        self.PT_SkipBackButton.setGeometry(QtCore.QRect(350, 360, 141, 41))
        self.PT_SkipBackButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius: 20px;")
        self.PT_SkipBackButton.setObjectName("PT_SkipBackButton")
        self.PT_TimeLabel = QtWidgets.QLabel(self.PT_Container)
        self.PT_TimeLabel.setGeometry(QtCore.QRect(510, 370, 81, 16))
        self.PT_TimeLabel.setStyleSheet("\n"
                                        "color: rgb(255, 255, 255);")
        self.PT_TimeLabel.setObjectName("PT_TimeLabel")
        self.MainMenu.addWidget(self.PreviewTab)

        self.DownloadTab = QtWidgets.QWidget()
        self.DownloadTab.setObjectName("DownloadTab")
        self.DOW_Container = QtWidgets.QFrame(self.DownloadTab)
        self.DOW_Container.setGeometry(QtCore.QRect(0, 50, 781, 371))
        self.DOW_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.DOW_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DOW_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DOW_Container.setObjectName("DOW_Container")
        self.DOW_FindButton = QtWidgets.QPushButton(self.DOW_Container)
        self.DOW_FindButton.setGeometry(QtCore.QRect(310, 160, 141, 41))
        self.DOW_FindButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DOW_FindButton.setObjectName("DOW_FindButton")
        self.DOW_LinkInput = QtWidgets.QLineEdit(self.DOW_Container)
        self.DOW_LinkInput.setGeometry(QtCore.QRect(70, 50, 581, 31))
        self.DOW_LinkInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.DOW_LinkInput.setObjectName("DOW_LinkInput")
        self.DOW_TabLabel = QtWidgets.QLabel(self.DownloadTab)
        self.DOW_TabLabel.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.DOW_TabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.DOW_TabLabel.setObjectName("DOW_TabLabel")
        self.MainMenu.addWidget(self.DownloadTab)

        self.DownloadDetailsTab = QtWidgets.QWidget()
        self.DownloadDetailsTab.setObjectName("DownloadDetailsTab")
        self.DDT_Container = QtWidgets.QFrame(self.DownloadDetailsTab)
        self.DDT_Container.setGeometry(QtCore.QRect(0, 50, 781, 371))
        self.DDT_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.DDT_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DDT_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DDT_Container.setObjectName("DDT_Container")
        self.DDT_VideoName = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_VideoName.setGeometry(QtCore.QRect(40, 10, 111, 41))
        self.DDT_VideoName.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_VideoName.setObjectName("DDT_VideoName")
        self.DDT_QualityLabel = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_QualityLabel.setGeometry(QtCore.QRect(220, 50, 141, 41))
        self.DDT_QualityLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_QualityLabel.setObjectName("DDT_QualityLabel")
        self.DDT_FormatLabel = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_FormatLabel.setGeometry(QtCore.QRect(440, 50, 141, 41))
        self.DDT_FormatLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_FormatLabel.setObjectName("DDT_FormatLabel")
        self.DDT_BitrateLabel = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_BitrateLabel.setGeometry(QtCore.QRect(630, 50, 141, 41))
        self.DDT_BitrateLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_BitrateLabel.setObjectName("DDT_BitrateLabel")
        self.DDT_QualityBox = QtWidgets.QComboBox(self.DDT_Container)
        self.DDT_QualityBox.setGeometry(QtCore.QRect(190, 110, 171, 22))
        self.DDT_QualityBox.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_QualityBox.setObjectName("DDT_QualityBox")
        self.DDT_FormatBox = QtWidgets.QComboBox(self.DDT_Container)
        self.DDT_FormatBox.setGeometry(QtCore.QRect(390, 110, 171, 22))
        self.DDT_FormatBox.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_FormatBox.setObjectName("DDT_FormatBox")
        self.DDT_BitrateBox = QtWidgets.QComboBox(self.DDT_Container)
        self.DDT_BitrateBox.setGeometry(QtCore.QRect(590, 110, 171, 22))
        self.DDT_BitrateBox.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_BitrateBox.setObjectName("DDT_BitrateBox")
        self.DDT_DownloadButton = QtWidgets.QPushButton(self.DDT_Container)
        self.DDT_DownloadButton.setGeometry(QtCore.QRect(420, 280, 141, 41))
        self.DDT_DownloadButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_DownloadButton.setObjectName("DDT_DownloadButton")
        self.DDT_CancelButton = QtWidgets.QPushButton(self.DDT_Container)
        self.DDT_CancelButton.setGeometry(QtCore.QRect(210, 280, 141, 41))
        self.DDT_CancelButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_CancelButton.setObjectName("DDT_CancelButton")
        self.DDT_VideoIcon = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_VideoIcon.setGeometry(QtCore.QRect(20, 100, 121, 121))
        self.DDT_VideoIcon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DDT_VideoIcon.setText("")
        self.DDT_VideoIcon.setObjectName("DDT_VideoIcon")
        self.DDT_PathInput = QtWidgets.QLineEdit(self.DDT_Container)
        self.DDT_PathInput.setGeometry(QtCore.QRect(190, 180, 571, 31))
        self.DDT_PathInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.DDT_PathInput.setObjectName("DDT_PathInput")
        self.DDT_PathLabel = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_PathLabel.setGeometry(QtCore.QRect(220, 140, 141, 41))
        self.DDT_PathLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DDT_PathLabel.setObjectName("DDT_PathLabel")
        self.DDT_LabLabel = QtWidgets.QLabel(self.DownloadDetailsTab)
        self.DDT_LabLabel.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.DDT_LabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.DDT_LabLabel.setObjectName("DDT_LabLabel")
        self.MainMenu.addWidget(self.DownloadDetailsTab)


        self.EditVideoTab = QtWidgets.QWidget()
        self.EditVideoTab.setObjectName("EditVideoTab")
        self.EDT_TabLabel = QtWidgets.QLabel(self.EditVideoTab)
        self.EDT_TabLabel.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.EDT_TabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.EDT_TabLabel.setObjectName("EDT_TabLabel")
        self.EDT_Container = QtWidgets.QFrame(self.EditVideoTab)
        self.EDT_Container.setGeometry(QtCore.QRect(0, 50, 781, 371))
        self.EDT_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.EDT_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EDT_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EDT_Container.setObjectName("EDT_Container")
        self.EDT_IconLabel = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_IconLabel.setGeometry(QtCore.QRect(60, 10, 121, 41))
        self.EDT_IconLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EDT_IconLabel.setObjectName("EDT_IconLabel")
        self.EDT_NameLabel = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_NameLabel.setGeometry(QtCore.QRect(200, 10, 91, 41))
        self.EDT_NameLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EDT_NameLabel.setObjectName("EDT_NameLabel")
        self.EDT_PathLabel = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_PathLabel.setGeometry(QtCore.QRect(200, 160, 121, 41))
        self.EDT_PathLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EDT_PathLabel.setObjectName("EDT_PathLabel")
        self.EDT_SaveButton = QtWidgets.QPushButton(self.EDT_Container)
        self.EDT_SaveButton.setGeometry(QtCore.QRect(430, 280, 141, 41))
        self.EDT_SaveButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EDT_SaveButton.setObjectName("EDT_SaveButton")
        self.EDT_ChangeButton = QtWidgets.QPushButton(self.EDT_Container)
        self.EDT_ChangeButton.setGeometry(QtCore.QRect(20, 180, 141, 41))
        self.EDT_ChangeButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EDT_ChangeButton.setObjectName("EDT_ChangeButton")
        self.EDT_DescriptionLabel = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_DescriptionLabel.setGeometry(QtCore.QRect(200, 90, 91, 31))
        self.EDT_DescriptionLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EDT_DescriptionLabel.setObjectName("EDT_DescriptionLabel")
        self.EDT_CancelButton = QtWidgets.QPushButton(self.EDT_Container)
        self.EDT_CancelButton.setGeometry(QtCore.QRect(210, 280, 141, 41))
        self.EDT_CancelButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EDT_CancelButton.setObjectName("EDT_CancelButton")
        self.EDT_NameInput = QtWidgets.QLineEdit(self.EDT_Container)
        self.EDT_NameInput.setGeometry(QtCore.QRect(200, 50, 411, 31))
        self.EDT_NameInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.EDT_NameInput.setObjectName("EDT_NameInput")
        self.EDT_DescriptionInput = QtWidgets.QLineEdit(self.EDT_Container)
        self.EDT_DescriptionInput.setGeometry(QtCore.QRect(200, 130, 411, 31))
        self.EDT_DescriptionInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.EDT_DescriptionInput.setObjectName("EDT_DescriptionInput")
        self.EDT_Icon = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_Icon.setGeometry(QtCore.QRect(30, 50, 121, 121))
        self.EDT_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.EDT_Icon.setText("")
        self.EDT_Icon.setObjectName("EDT_Icon")
        self.EDT_PathInput = QtWidgets.QLineEdit(self.EDT_Container)
        self.EDT_PathInput.setGeometry(QtCore.QRect(200, 200, 411, 31))
        self.EDT_PathInput.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(85, 85, 127);;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.EDT_PathInput.setObjectName("EDT_PathInput")
        self.MainMenu.addWidget(self.EditVideoTab)
        self.DialogTab = QtWidgets.QWidget()
        self.DialogTab.setObjectName("DialogTab")
        self.DLG_Container = QtWidgets.QFrame(self.DialogTab)
        self.DLG_Container.setGeometry(QtCore.QRect(0, 50, 781, 371))
        self.DLG_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.DLG_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DLG_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DLG_Container.setObjectName("DLG_Container")
        self.DLG_TextLabel = QtWidgets.QLabel(self.DLG_Container)
        self.DLG_TextLabel.setGeometry(QtCore.QRect(350, 110, 111, 41))
        self.DLG_TextLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DLG_TextLabel.setObjectName("DLG_TextLabel")
        self.DLG_AcceptButton = QtWidgets.QPushButton(self.DLG_Container)
        self.DLG_AcceptButton.setGeometry(QtCore.QRect(430, 200, 141, 41))
        self.DLG_AcceptButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DLG_AcceptButton.setObjectName("DLG_AcceptButton")
        self.DLG_CancelButton = QtWidgets.QPushButton(self.DLG_Container)
        self.DLG_CancelButton.setGeometry(QtCore.QRect(220, 200, 141, 41))
        self.DLG_CancelButton.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.DLG_CancelButton.setObjectName("DLG_CancelButton")
        self.DLG_DetailsLabel = QtWidgets.QLabel(self.DLG_Container)
        self.DLG_DetailsLabel.setGeometry(QtCore.QRect(370, 140, 111, 41))
        self.DLG_DetailsLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.DLG_DetailsLabel.setObjectName("DLG_DetailsLabel")
        self.DLG_TabLabel = QtWidgets.QLabel(self.DialogTab)
        self.DLG_TabLabel.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.DLG_TabLabel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.DLG_TabLabel.setObjectName("DLG_TabLabel")
        self.MainMenu.addWidget(self.DialogTab)


        self.enable_video_controls(False)
        self.enable_download_controls(False)
        self.EDT_PathLabel.setEnabled(False)
        self.download_details_reset()
        self.MainMenu.setCurrentIndex(0)


        self.window.setCentralWidget(self.WorkSpace)
        self.retranslate(self.window)
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def set_feedback(self, cntrl):
        self.controller = cntrl

    def setup_graphical_events(self):
        self.DownloadTabButton.clicked.connect(lambda: self.controller.user_switch_to_download_tab())
        self.VideosTabButton.clicked.connect(lambda: self.controller.user_switch_to_video_tab())

        self.VID_UpButton.clicked.connect(lambda: self.controller.user_click_scroll_up())
        self.VID_DownButton.clicked.connect(lambda: self.controller.user_click_scroll_down())

        self.VID1_Icon.mousePressEvent = lambda event: self.controller.user_click_video1_icon()

        self.DLG_AcceptButton.mousePressEvent = lambda event: self.controller.user_click_accept_delete()
        self.DLG_CancelButton.mousePressEvent = lambda event: self.controller.user_click_cancel()

        self.VID_DeleteButton.mousePressEvent = lambda event: self.controller.user_click_delete()
        self.VID_EditButton.clicked.connect(lambda: self.controller.user_click_edit())
        self.EDT_SaveButton.mousePressEvent = lambda event: self.controller.user_accept_edit_clicked()
        self.EDT_CancelButton.mousePressEvent = lambda event: self.controller.user_click_cancel()

        self.VID_WatchButton.clicked.connect(lambda: self.controller.user_click_watch())
        self.PT_CancelButton.clicked.connect(lambda: self.controller.video_close())

        self.VID2_Icon.mousePressEvent = lambda event: self.controller.user_click_video2_icon()

        self.DOW_FindButton.clicked.connect(lambda: self.controller.user_click_find())

        self.DDT_DownloadButton.clicked.connect(lambda: self.controller.user_clicked_download())
        self.DDT_QualityBox.currentIndexChanged.connect(lambda: self.controller.user_select_resolution())
        self.DDT_FormatBox.currentIndexChanged.connect(lambda: self.controller.user_select_format())
        self.DDT_BitrateBox.currentIndexChanged.connect(lambda: self.controller.user_select_fps())



        self.VideosTabButton.enterEvent = lambda event: self.highlight_item(self.VideosTabButton, self.px_low)
        self.VideosTabButton.leaveEvent = lambda event: self.unhighlight_item(self.VideosTabButton, self.px_low)
        self.DownloadTabButton.enterEvent = lambda event: self.highlight_item(self.DownloadTabButton, self.px_low)
        self.DownloadTabButton.leaveEvent = lambda event: self.unhighlight_item(self.DownloadTabButton, self.px_low)

        self.VID_UpButton.enterEvent = lambda event: self.highlight_item(self.VID_UpButton, self.px_low)
        self.VID_UpButton.leaveEvent = lambda event: self.unhighlight_item(self.VID_UpButton, self.px_low)
        self.VID_DownButton.enterEvent = lambda event: self.highlight_item(self.VID_DownButton, self.px_low)
        self.VID_DownButton.leaveEvent = lambda event: self.unhighlight_item(self.VID_DownButton, self.px_low)

        self.VID1_Icon.enterEvent = lambda event: self.highlight_item(self.VID1_Icon, self.px_low)
        self.VID1_Icon.leaveEvent = lambda event: self.unhighlight_item(self.VID1_Icon, self.px_low)
        self.VID_WatchButton.enterEvent = lambda event: self.highlight_item(self.VID_WatchButton, self.px_low)
        self.VID_WatchButton.leaveEvent = lambda event: self.unhighlight_item(self.VID_WatchButton, self.px_low)
        self.VID_EditButton.enterEvent = lambda event: self.highlight_item(self.VID_EditButton, self.px_low)
        self.VID_EditButton.leaveEvent = lambda event: self.unhighlight_item(self.VID_EditButton, self.px_low)
        self.VID_DeleteButton.enterEvent = lambda event: self.highlight_item(self.VID_DeleteButton, self.px_low)
        self.VID_DeleteButton.leaveEvent = lambda event: self.unhighlight_item(self.VID_DeleteButton, self.px_low)

        self.VID2_Icon.enterEvent = lambda event: self.highlight_item(self.VID2_Icon, self.px_low)
        self.VID2_Icon.leaveEvent = lambda event: self.unhighlight_item(self.VID2_Icon, self.px_low)


        self.DOW_FindButton.enterEvent = lambda event: self.highlight_item(self.DOW_FindButton, self.px_low)
        self.DOW_FindButton.leaveEvent = lambda event: self.unhighlight_item(self.DOW_FindButton, self.px_low)

        self.DLG_AcceptButton.enterEvent = lambda event: self.highlight_item(self.DLG_AcceptButton, self.px_low)
        self.DLG_AcceptButton.leaveEvent = lambda event: self.unhighlight_item(self.DLG_AcceptButton, self.px_low)
        self.DLG_CancelButton.enterEvent = lambda event: self.highlight_item(self.DLG_CancelButton, self.px_low)
        self.DLG_CancelButton.leaveEvent = lambda event: self.unhighlight_item(self.DLG_CancelButton, self.px_low)

        self.EDT_SaveButton.enterEvent = lambda event: self.highlight_item(self.EDT_SaveButton, self.px_low)
        self.EDT_SaveButton.leaveEvent = lambda event: self.unhighlight_item(self.EDT_SaveButton, self.px_low)
        self.EDT_CancelButton.enterEvent = lambda event: self.highlight_item(self.EDT_CancelButton, self.px_low)
        self.EDT_CancelButton.leaveEvent = lambda event: self.unhighlight_item(self.EDT_CancelButton, self.px_low)
        self.EDT_ChangeButton.enterEvent = lambda event: self.highlight_item(self.EDT_ChangeButton, self.px_low)
        self.EDT_ChangeButton.leaveEvent = lambda event: self.unhighlight_item(self.EDT_ChangeButton, self.px_low)

        self.PT_CancelButton.enterEvent = lambda event: self.highlight_item(self.PT_CancelButton, self.px_low)
        self.PT_CancelButton.leaveEvent = lambda event: self.unhighlight_item(self.PT_CancelButton, self.px_low)
        self.PT_StopOrPlayButton.enterEvent = lambda event: self.highlight_item(self.PT_StopOrPlayButton, self.px_low)
        self.PT_StopOrPlayButton.leaveEvent = lambda event: self.unhighlight_item(self.PT_StopOrPlayButton, self.px_low)
        self.PT_ShipForwardButton.enterEvent = lambda event: self.highlight_item(self.PT_ShipForwardButton, self.px_low)
        self.PT_ShipForwardButton.leaveEvent = lambda event: self.unhighlight_item(self.PT_ShipForwardButton, self.px_low)
        self.PT_SkipBackButton.enterEvent = lambda event: self.highlight_item(self.PT_SkipBackButton, self.px_low)
        self.PT_SkipBackButton.leaveEvent = lambda event: self.unhighlight_item(self.PT_SkipBackButton, self.px_low)

        self.EDT_PathInput.mousePressEvent = lambda event: self.edit_video_directory_discover()
        self.DDT_PathInput.mousePressEvent = lambda event: self.download_video_directory_discover()

        self.DDT_CancelButton.enterEvent = lambda event: self.highlight_item(self.DDT_CancelButton, self.px_low)
        self.DDT_CancelButton.leaveEvent = lambda event: self.unhighlight_item(self.DDT_CancelButton, self.px_low)
        self.DDT_DownloadButton.enterEvent = lambda event: self.highlight_item(self.DDT_DownloadButton, self.px_low)
        self.DDT_DownloadButton.leaveEvent = lambda event: self.unhighlight_item(self.DDT_DownloadButton, self.px_low)


    def retranslate(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "YTSaver"))
            self.AppMessagerOutput.setText(_translate("MainWindow", "SysMsg"))
            self.VideosTabButton.setText(_translate("MainWindow", "Videos"))
            self.DownloadTabButton.setText(_translate("MainWindow", "Download"))
            self.VID_UpButton.setText(_translate("MainWindow", "↑"))
            self.VID_DownButton.setText(_translate("MainWindow", "↓"))
            self.VID1_Container.setTitle(_translate("MainWindow", "GroupBox"))
            self.VID1_NameLabel.setText(_translate("MainWindow", "VideoName"))
            self.VID1_DateCreationLabel.setText(_translate("MainWindow", "10.01.2003"))
            self.VID1_DescriptionLabel.setText(_translate("MainWindow", "description"))
            self.VID1_PathLabel.setText(_translate("MainWindow", "C:/USERS/DOCUMENTS/"))
            self.VID2_Container.setTitle(_translate("MainWindow", "GroupBox"))
            self.VID2_NameLabel.setText(_translate("MainWindow", "VideoName"))
            self.VID2_DateCreationLabel.setText(_translate("MainWindow", "10.01.2003"))
            self.VID2_DescriptionLabel.setText(_translate("MainWindow", "description"))
            self.VID2_PathLabel.setText(_translate("MainWindow", "C:/USERS/DOCUMENTS/"))
            self.VID_NothingLabel.setText(_translate("MainWindow", "nothing found"))
            self.VID_WatchButton.setText(_translate("MainWindow", "O"))
            self.VID_DeleteButton.setText(_translate("MainWindow", "×"))
            self.VID_EditButton.setText(_translate("MainWindow", "E"))
            self.VID1_NameLabel_2.setText(_translate("MainWindow", "Controls"))
            self.VID_TabLabel.setText(_translate("MainWindow", "Downloaded videos count:"))
            self.VID_CountValue.setText(_translate("MainWindow", "0"))
            self.DOW_FindButton.setText(_translate("MainWindow", "Find"))
            self.DOW_LinkInput.setText(_translate("MainWindow", "url"))
            self.DOW_TabLabel.setText(_translate("MainWindow", "Find"))
            self.DDT_VideoName.setText(_translate("MainWindow", "Video name:"))
            self.DDT_QualityLabel.setText(_translate("MainWindow", "Сhoose quality:"))
            self.DDT_FormatLabel.setText(_translate("MainWindow", "Сhoose format:"))
            self.DDT_BitrateLabel.setText(_translate("MainWindow", "Сhoose bitrate:"))
            self.DDT_DownloadButton.setText(_translate("MainWindow", "download video"))
            self.DDT_CancelButton.setText(_translate("MainWindow", "cancel"))
            self.DDT_PathInput.setText(_translate("MainWindow", "..."))
            self.DDT_PathLabel.setText(_translate("MainWindow", "Enter path"))
            self.DDT_LabLabel.setText(_translate("MainWindow", "Download details:"))
            self.EDT_TabLabel.setText(_translate("MainWindow", "Edit Video Info"))
            self.EDT_IconLabel.setText(_translate("MainWindow", "Video icon:"))
            self.EDT_NameLabel.setText(_translate("MainWindow", "video name:"))
            self.EDT_PathLabel.setText(_translate("MainWindow", "path:"))
            self.EDT_SaveButton.setText(_translate("MainWindow", "save"))
            self.EDT_ChangeButton.setText(_translate("MainWindow", "change"))
            self.EDT_DescriptionLabel.setText(_translate("MainWindow", "video description:"))
            self.EDT_CancelButton.setText(_translate("MainWindow", "cancel"))
            self.EDT_NameInput.setText(_translate("MainWindow", "name"))
            self.EDT_DescriptionInput.setText(_translate("MainWindow", "desc"))
            self.EDT_PathInput.setText(_translate("MainWindow", "path"))
            self.DLG_TextLabel.setText(_translate("MainWindow", "Are you shure to"))
            self.DLG_AcceptButton.setText(_translate("MainWindow", "shure"))
            self.DLG_CancelButton.setText(_translate("MainWindow", "cancel"))
            self.DLG_DetailsLabel.setText(_translate("MainWindow", "details?"))
            self.DLG_TabLabel.setText(_translate("MainWindow", "Warning"))
            self.PT_CancelButton.setText(_translate("MainWindow", "BACK"))
            self.PT_StopOrPlayButton.setText(_translate("MainWindow", "STOP/PLAY"))
            self.PT_ShipForwardButton.setText(_translate("MainWindow", ">> 5"))
            self.PT_SkipBackButton.setText(_translate("MainWindow", "5<< "))
            self.PT_TimeLabel.setText(_translate("MainWindow", "time"))

    def edit_video_directory_discover(self):
        directory = QFileDialog.getExistingDirectory(self.window,  'Выберите директорию', '/')
        self.EDT_PathInput.setText(directory)

    def download_video_directory_discover(self):
        directory = QFileDialog.getExistingDirectory(self.window,  'Выберите директорию', '/')
        self.DDT_PathInput.setText(directory)

    def show_main_window(self, allow):
        if allow:
            self.window.show()
        else:
            self.window.hide()

    def highlight_item(self, item, px):
        current_style = item.styleSheet()
        new_style = current_style + f";border: {px}px solid white;"
        item.setStyleSheet(new_style)

    def unhighlight_item(self, item, px):
        current_style = item.styleSheet()
        new_style = current_style.replace(f"border: {px}px solid white;", "")
        item.setStyleSheet(new_style)

    def set_video1_info(self, video_info):
        self.VID1_NameLabel.setText(str(video_info['video_name']))
        self.VID1_DescriptionLabel.setText(str(video_info['video_desc']))
        self.VID1_PathLabel.setText(str(video_info['video_path']))
        self.VID1_DateCreationLabel.setText(str(video_info['video_date']))

    def set_video2_info(self, video_info):
        self.VID2_NameLabel.setText(str(video_info['video_name']))
        self.VID2_DescriptionLabel.setText(str(video_info['video_desc']))
        self.VID2_PathLabel.setText(str(video_info['video_path']))
        self.VID2_DateCreationLabel.setText(str(video_info['video_date']))

    def disable_videos_display(self):
        self.VID_NothingLabel.setVisible(True)
        self.VID1_Container.setVisible(False)
        self.VID2_Container.setVisible(False)

    def enable_videos_display(self):
        self.VID_NothingLabel.setVisible(False)

    def update_displayed_count_videos(self, count):
        self.VID_CountValue.setText(str(count))

    def display_first_video(self, data):
        self.set_video1_info(data)
        self.VID1_Container.setVisible(True)

    def hide_first_video(self):
        self.VID1_Container.setVisible(False)

    def display_second_video(self, data):
        self.set_video2_info(data)
        self.VID2_Container.setVisible(True)

    def hide_second_video(self):
        self.VID2_Container.setVisible(False)

    def mark_first_video_as_current(self, flag):
        if flag:
            self.highlight_item(self.VID1_Icon, self.px_medium)
            self.unhighlight_item(self.VID2_Icon, self.px_medium)
        else:
            self.unhighlight_item(self.VID1_Icon, self.px_medium)

    def mark_second_video_as_current(self, flag):
        if flag:
            self.highlight_item(self.VID2_Icon, self.px_medium)
            self.unhighlight_item(self.VID1_Icon, self.px_medium)
        else:
            self.unhighlight_item(self.VID2_Icon, self.px_medium)

    def set_disabled_style(self, element):
        current_style = element.styleSheet()
        new_style = current_style + f";background-color: lightgray; color: darkgray;"
        element.setStyleSheet(new_style)
        element.setEnabled(False)

    def set_enabled_style(self, element):
        current_style = element.styleSheet()
        new_style = current_style.replace(f";background-color: lightgray; color: darkgray;", "")
        element.setStyleSheet(new_style)
        element.setEnabled(True)

    def enable_video_controls(self, flag):
        if flag:
            self.set_enabled_style(self.VID_WatchButton)
            self.set_enabled_style(self.VID_EditButton)
            self.set_enabled_style(self.VID_DeleteButton)
            self.VID_WatchButton.setEnabled(True)
            self.VID_EditButton.setEnabled(True)
            self.VID_DeleteButton.setEnabled(True)
        else:
            self.set_disabled_style(self.VID_WatchButton)
            self.set_disabled_style(self.VID_EditButton)
            self.set_disabled_style(self.VID_DeleteButton)
            self.VID_WatchButton.setEnabled(False)
            self.VID_EditButton.setEnabled(False)
            self.VID_DeleteButton.setEnabled(False)



    def delete_video_dialog(self, video_name):
        self.MainMenu.setCurrentWidget(self.DialogTab)
        self.DLG_DetailsLabel.setText(f"to delete video {video_name}")


    def edit_video(self, video):
        self.MainMenu.setCurrentWidget(self.EditVideoTab)

        path = video['video_path']
        name = video['video_name']
        desc = video['video_desc']

        self.EDT_NameInput.setText(name)
        self.EDT_DescriptionInput.setText(desc)
        self.EDT_PathInput.setText(path)

    def get_data_from_edit_fields(self):
        info = {
            'video_name': self.EDT_NameInput.text(),
            'video_desc': self.EDT_DescriptionInput.text(),
            'video_path': self.EDT_PathInput.text(),
            'video_icon': self.EDT_Icon.text()
                }
        return info


    def display_video(self, path):
        self.MainMenu.setCurrentWidget(self.PreviewTab)
        self.player = VideoPlayer(
            path,
            self.PT_Video,
            self.PT_StopOrPlayButton,
            self.PT_SkipBackButton,
            self.PT_ShipForwardButton,
            self.PT_TimeLabel
        )

    def undisplay_video(self):
        self.MainMenu.setCurrentWidget(self.VideoTab)
        del self.player

    def get_data_search_bar(self):
        url = self.DOW_LinkInput.text()
        return url





    def show_available_resolutions(self, resolutions):

        self.DDT_QualityBox.blockSignals(True)


        self.set_disabled_style(self.DDT_FormatBox)
        self.set_disabled_style(self.DDT_BitrateBox)
        self.DDT_QualityBox.clear()
        self.set_enabled_style(self.DDT_QualityBox)
        self.DDT_QualityBox.addItem('-')
        for element in resolutions:
            self.DDT_QualityBox.addItem(element)

        self.DDT_QualityBox.blockSignals(False)

    def show_available_formats(self, formats):

        self.DDT_FormatBox.blockSignals(True)


        self.set_disabled_style(self.DDT_BitrateBox)
        self.DDT_FormatBox.clear()
        self.set_enabled_style(self.DDT_FormatBox)
        self.DDT_FormatBox.addItem('-')
        for element in formats:
            self.DDT_FormatBox.addItem(element)

        self.DDT_FormatBox.blockSignals(False)

    def show_available_fps(self, frames):

        self.DDT_BitrateBox.blockSignals(True)


        self.DDT_BitrateBox.clear()
        self.set_enabled_style(self.DDT_BitrateBox)
        self.DDT_BitrateBox.addItem('-')
        for element in frames:
                self.DDT_BitrateBox.addItem(str(element))

        self.DDT_BitrateBox.blockSignals(False)

    def download_details_reset(self):
        self.set_disabled_style(self.DDT_FormatBox)
        self.set_disabled_style(self.DDT_QualityBox)
        self.set_disabled_style(self.DDT_BitrateBox)

    def get_data_from_download_fields(self):
        info = {
            'resolution': self.DDT_QualityBox.currentText(),
            'format': self.DDT_FormatBox.currentText(),
            'fps': self.DDT_BitrateBox.currentText(),
            'path': self.DDT_PathInput.text()
        }
        return info

    def enable_download_controls(self, flag):
        if flag:
            self.set_enabled_style(self.DDT_DownloadButton)
            self.DDT_DownloadButton.setEnabled(True)
        else:
            self.set_disabled_style(self.DDT_DownloadButton)
            self.DDT_DownloadButton.setEnabled(False)

    def enable_nav_controls(self, flag):
        if flag:
                self.set_enabled_style(self.VideosTabButton)
                self.VideosTabButton.setEnabled(True)
                self.set_enabled_style(self.DownloadTabButton)
                self.DownloadTabButton.setEnabled(True)
        else:
                self.set_disabled_style(self.VideosTabButton)
                self.VideosTabButton.setEnabled(False)
                self.set_disabled_style(self.DownloadTabButton)
                self.DownloadTabButton.setEnabled(False)

    def switch_to_video_tab(self):
        self.MainMenu.setCurrentWidget(self.VideoTab)


    def switch_to_download_tab(self):
        self.MainMenu.setCurrentWidget(self.DownloadTab)

    def switch_to_download_details_tab(self, video_name):
        self.MainMenu.setCurrentWidget(self.DownloadDetailsTab)
        self.DDT_VideoName.setText(video_name)

    def switch_to_dialog_tab(self, msg):
        self.MainMenu.setCurrentWidget(self.DialogTab)
        self.DLG_DetailsLabel.setText(msg)

    def setup_app_message(self, msg):
        self.AppMessagerOutput.setText(msg)