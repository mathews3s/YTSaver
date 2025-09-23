from PyQt5.QtWidgets import QApplication as AppQT, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore, QtWidgets
import os
from app.utils.player import VideoPlayer


class View:

    def __init__(self):
        # attributes for installing lines width
        self.px_low = 2
        self.px_medium = 4
        # attributes for class aggregation/composision
        self.player = None
        self.controller = None
        self.app = AppQT([])

        # QT elements constructing
        self.window = QtWidgets.QMainWindow()
        self.window.setObjectName("MainWindow")
        self.window.resize(1200, 800)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.window.sizePolicy().hasHeightForWidth())
        self.window.setSizePolicy(self.sizePolicy)
        self.window.setMinimumSize(QtCore.QSize(1200, 800))
        self.window.setMaximumSize(QtCore.QSize(1200, 800))
        self.window.setStyleSheet("border-color: rgb(255, 16, 80);")

        self.WorkSpace = QtWidgets.QWidget(self.window)
        self.WorkSpace.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(85, 85, 127);")
        self.WorkSpace.setObjectName("WorkSpace")
        self.AppMessengerBar = QtWidgets.QFrame(self.WorkSpace)
        self.AppMessengerBar.setGeometry(QtCore.QRect(0, 10, 1201, 71))
        self.AppMessengerBar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                           "border-radius: 0px;")
        self.AppMessengerBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AppMessengerBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AppMessengerBar.setObjectName("AppMessagerBar")
        self.AppMessengerIcon = QtWidgets.QLabel(self.AppMessengerBar)
        self.AppMessengerIcon.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.AppMessengerIcon.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(0, 0, 0);\n"
                                            "border: 2px solid;\n"
                                            "border-color: rgb(255, 255, 255);\n"
                                            "border-radius: 25px;")
        self.AppMessengerIcon.setText("")
        self.AppMessengerIcon.setObjectName("AppMessagerIcon")
        self.AppMessengerOutput = QtWidgets.QLabel(self.AppMessengerBar)
        self.AppMessengerOutput.setGeometry(QtCore.QRect(110, 15, 1061, 41))
        self.AppMessengerOutput.setStyleSheet("font: 63 13pt \"Yu Gothic UI Semibold\";\n"
                                              "background-color: rgb(0, 0, 0);\n"
                                              "color: rgb(255, 255, 255);")
        self.AppMessengerOutput.setText("")
        self.AppMessengerOutput.setObjectName("AppMessagerOutput")
        self.ControlButtonsBar = QtWidgets.QFrame(self.WorkSpace)
        self.ControlButtonsBar.setGeometry(QtCore.QRect(-10, 90, 1211, 71))
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
        self.VideosTabButton.setGeometry(QtCore.QRect(760, 10, 321, 51))
        self.VideosTabButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                           "background-color: rgb(85, 85, 127);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 20px;")
        self.VideosTabButton.setObjectName("VideosTabButton")
        self.DownloadTabButton = QtWidgets.QPushButton(self.ControlButtonsBar)
        self.DownloadTabButton.setGeometry(QtCore.QRect(110, 10, 321, 51))
        self.DownloadTabButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                             "background-color: rgb(85, 85, 127);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius: 20px;")
        self.DownloadTabButton.setObjectName("DownloadTabButton")
        self.MainMenu = QtWidgets.QStackedWidget(self.WorkSpace)
        self.MainMenu.setGeometry(QtCore.QRect(10, 160, 1171, 631))
        self.MainMenu.setObjectName("MainMenu")
        self.VideoTab = QtWidgets.QWidget()
        self.VideoTab.setObjectName("VideoTab")
        self.VID_Container = QtWidgets.QFrame(self.VideoTab)
        self.VID_Container.setGeometry(QtCore.QRect(0, 50, 1171, 571))
        self.VID_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "border-radius: 20px;\n"
                                         "text-align: center;\n"
                                         "")
        self.VID_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VID_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VID_Container.setObjectName("VID_Container")
        self.VID_UpButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_UpButton.setGeometry(QtCore.QRect(30, 90, 51, 81))
        self.VID_UpButton.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                        "background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px\n"
                                        "")
        self.VID_UpButton.setObjectName("VID_UpButton")
        self.VID_DownButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_DownButton.setGeometry(QtCore.QRect(30, 380, 51, 81))
        self.VID_DownButton.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                          "background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 10px\n"
                                          "")
        self.VID_DownButton.setObjectName("VID_DownButton")
        self.VID1_Container = QtWidgets.QGroupBox(self.VID_Container)
        self.VID1_Container.setGeometry(QtCore.QRect(100, 40, 731, 211))
        self.VID1_Container.setObjectName("VID1_Container")
        self.VID1_Icon = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_Icon.setGeometry(QtCore.QRect(10, 10, 171, 161))
        self.VID1_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 20px;")
        self.VID1_Icon.setText("")
        self.VID1_Icon.setObjectName("VID1_Icon")
        self.VID1_NameLabel = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_NameLabel.setGeometry(QtCore.QRect(200, 20, 531, 21))
        self.VID1_NameLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                          "color: rgb(255, 255, 255);")
        self.VID1_NameLabel.setText("")
        self.VID1_NameLabel.setObjectName("VID1_NameLabel")
        self.VID1_DateCreationLabel = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_DateCreationLabel.setGeometry(QtCore.QRect(200, 60, 141, 21))
        self.VID1_DateCreationLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                                  "color: rgb(255, 255, 255);")
        self.VID1_DateCreationLabel.setText("")
        self.VID1_DateCreationLabel.setObjectName("VID1_DateCreationLabel")
        self.VID1_DescriptionLabel = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_DescriptionLabel.setGeometry(QtCore.QRect(200, 100, 531, 31))
        self.VID1_DescriptionLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                                 "color: rgb(255, 255, 255);")
        self.VID1_DescriptionLabel.setText("")
        self.VID1_DescriptionLabel.setObjectName("VID1_DescriptionLabel")
        self.VID1_PathLabel = QtWidgets.QLabel(self.VID1_Container)
        self.VID1_PathLabel.setGeometry(QtCore.QRect(200, 150, 531, 20))
        self.VID1_PathLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                          "color: rgb(255, 255, 255);")
        self.VID1_PathLabel.setText("")
        self.VID1_PathLabel.setObjectName("VID1_PathLabel")
        self.VID2_Container = QtWidgets.QGroupBox(self.VID_Container)
        self.VID2_Container.setGeometry(QtCore.QRect(100, 310, 741, 241))
        self.VID2_Container.setObjectName("VID2_Container")
        self.VID2_Icon = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_Icon.setGeometry(QtCore.QRect(10, 20, 171, 171))
        self.VID2_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 20px;")
        self.VID2_Icon.setText("")
        self.VID2_Icon.setObjectName("VID2_Icon")
        self.VID2_NameLabel = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_NameLabel.setGeometry(QtCore.QRect(200, 30, 551, 31))
        self.VID2_NameLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                          "color: rgb(255, 255, 255);")
        self.VID2_NameLabel.setText("")
        self.VID2_NameLabel.setObjectName("VID2_NameLabel")
        self.VID2_DateCreationLabel = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_DateCreationLabel.setGeometry(QtCore.QRect(200, 70, 321, 31))
        self.VID2_DateCreationLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                                  "color: rgb(255, 255, 255);")
        self.VID2_DateCreationLabel.setText("")
        self.VID2_DateCreationLabel.setObjectName("VID2_DateCreationLabel")
        self.VID2_DescriptionLabel = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_DescriptionLabel.setGeometry(QtCore.QRect(200, 110, 541, 41))
        self.VID2_DescriptionLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                                 "color: rgb(255, 255, 255);")
        self.VID2_DescriptionLabel.setText("")
        self.VID2_DescriptionLabel.setObjectName("VID2_DescriptionLabel")
        self.VID2_PathLabel = QtWidgets.QLabel(self.VID2_Container)
        self.VID2_PathLabel.setGeometry(QtCore.QRect(200, 170, 541, 21))
        self.VID2_PathLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                          "color: rgb(255, 255, 255);")
        self.VID2_PathLabel.setText("")
        self.VID2_PathLabel.setObjectName("VID2_PathLabel")
        self.VID_NothingLabel = QtWidgets.QLabel(self.VID_Container)
        self.VID_NothingLabel.setGeometry(QtCore.QRect(410, 250, 261, 41))
        self.VID_NothingLabel.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                            "color: rgb(255, 255, 255);")
        self.VID_NothingLabel.setObjectName("VID_NothingLabel")
        self.VID_WatchButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_WatchButton.setGeometry(QtCore.QRect(910, 180, 211, 41))
        self.VID_WatchButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                           "background-color: rgb(85, 85, 127);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 10px\n"
                                           "")
        self.VID_WatchButton.setObjectName("VID_WatchButton")
        self.VID_DeleteButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_DeleteButton.setGeometry(QtCore.QRect(910, 270, 211, 41))
        self.VID_DeleteButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                            "background-color: rgb(85, 85, 127);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 10px\n"
                                            "")
        self.VID_DeleteButton.setObjectName("VID_DeleteButton")
        self.VID_EditButton = QtWidgets.QPushButton(self.VID_Container)
        self.VID_EditButton.setGeometry(QtCore.QRect(910, 360, 211, 41))
        self.VID_EditButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                          "background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 10px\n"
                                          "")
        self.VID_EditButton.setObjectName("VID_EditButton")
        self.VID_ControlsLabel = QtWidgets.QLabel(self.VID_Container)
        self.VID_ControlsLabel.setGeometry(QtCore.QRect(890, 80, 241, 81))
        self.VID_ControlsLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                             "color: rgb(255, 255, 255);")
        self.VID_ControlsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VID_ControlsLabel.setObjectName("VID_ControlsLabel")
        self.VID_TabLabel = QtWidgets.QLabel(self.VideoTab)
        self.VID_TabLabel.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.VID_TabLabel.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                        "background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.VID_TabLabel.setObjectName("VID_TabLabel")
        self.VID_CountValue = QtWidgets.QLabel(self.VideoTab)
        self.VID_CountValue.setGeometry(QtCore.QRect(190, 10, 55, 31))
        self.VID_CountValue.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                          "background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);")
        self.VID_CountValue.setObjectName("VID_CountValue")
        self.MainMenu.addWidget(self.VideoTab)
        self.DownloadTab = QtWidgets.QWidget()
        self.DownloadTab.setObjectName("DownloadTab")
        self.DOW_Container = QtWidgets.QFrame(self.DownloadTab)
        self.DOW_Container.setGeometry(QtCore.QRect(0, 50, 1171, 571))
        self.DOW_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "border-radius: 20px;")
        self.DOW_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DOW_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DOW_Container.setObjectName("DOW_Container")
        self.DOW_FindButton = QtWidgets.QPushButton(self.DOW_Container)
        self.DOW_FindButton.setGeometry(QtCore.QRect(450, 340, 271, 51))
        self.DOW_FindButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                          "background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 20px;")
        self.DOW_FindButton.setObjectName("DOW_FindButton")
        self.DOW_LinkInput = QtWidgets.QLineEdit(self.DOW_Container)
        self.DOW_LinkInput.setGeometry(QtCore.QRect(130, 220, 901, 41))
        self.DOW_LinkInput.setStyleSheet("padding-left: 10px;\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border: 3px solid rgb(85, 85, 127);;\n"
                                         "border-radius: 10px;\n"
                                         "\n"
                                         "")
        self.DOW_LinkInput.setObjectName("DOW_LinkInput")
        self.DOW_TabLabel = QtWidgets.QLabel(self.DownloadTab)
        self.DOW_TabLabel.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.DOW_TabLabel.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                        "background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.DOW_TabLabel.setObjectName("DOW_TabLabel")
        self.MainMenu.addWidget(self.DownloadTab)
        self.PreviewTab = QtWidgets.QWidget()
        self.PreviewTab.setObjectName("PreviewTab")
        self.PT_Container = QtWidgets.QFrame(self.PreviewTab)
        self.PT_Container.setGeometry(QtCore.QRect(0, 10, 1211, 611))
        self.PT_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "border-radius: 20px;")
        self.PT_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PT_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PT_Container.setObjectName("PT_Container")
        self.PT_CancelButton = QtWidgets.QPushButton(self.PT_Container)
        self.PT_CancelButton.setGeometry(QtCore.QRect(40, 540, 221, 61))
        self.PT_CancelButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                           "background-color: rgb(85, 85, 127);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 20px;")
        self.PT_CancelButton.setObjectName("PT_CancelButton")
        self.PT_Video = QtWidgets.QLabel(self.PT_Container)
        self.PT_Video.setGeometry(QtCore.QRect(20, 40, 1131, 481))
        self.PT_Video.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(56, 40, 110, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 20px;")
        self.PT_Video.setText("")
        self.PT_Video.setObjectName("PT_Video")
        self.PT_StopOrPlayButton = QtWidgets.QPushButton(self.PT_Container)
        self.PT_StopOrPlayButton.setGeometry(QtCore.QRect(370, 540, 231, 61))
        self.PT_StopOrPlayButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                               "background-color: rgb(85, 85, 127);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-radius: 20px;")
        self.PT_StopOrPlayButton.setObjectName("PT_StopOrPlayButton")
        self.PT_ShipForwardButton = QtWidgets.QPushButton(self.PT_Container)
        self.PT_ShipForwardButton.setGeometry(QtCore.QRect(1030, 540, 91, 61))
        self.PT_ShipForwardButton.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                                "background-color: rgb(85, 85, 127);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "border-radius: 20px;")
        self.PT_ShipForwardButton.setObjectName("PT_ShipForwardButton")
        self.PT_SkipBackButton = QtWidgets.QPushButton(self.PT_Container)
        self.PT_SkipBackButton.setGeometry(QtCore.QRect(720, 540, 91, 61))
        self.PT_SkipBackButton.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                             "background-color: rgb(85, 85, 127);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius: 20px;")
        self.PT_SkipBackButton.setObjectName("PT_SkipBackButton")
        self.PT_TimeLabel = QtWidgets.QLabel(self.PT_Container)
        self.PT_TimeLabel.setGeometry(QtCore.QRect(870, 550, 111, 41))
        self.PT_TimeLabel.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                        "color: rgb(255, 255, 255);")
        self.PT_TimeLabel.setText("")
        self.PT_TimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PT_TimeLabel.setObjectName("PT_TimeLabel")
        self.MainMenu.addWidget(self.PreviewTab)
        self.DownloadDetailsTab = QtWidgets.QWidget()
        self.DownloadDetailsTab.setObjectName("DownloadDetailsTab")
        self.DDT_Container = QtWidgets.QFrame(self.DownloadDetailsTab)
        self.DDT_Container.setGeometry(QtCore.QRect(0, 50, 1181, 571))
        self.DDT_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "border-radius: 20px;")
        self.DDT_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DDT_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DDT_Container.setObjectName("DDT_Container")
        self.DDT_VideoName = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_VideoName.setGeometry(QtCore.QRect(40, 40, 1111, 41))
        self.DDT_VideoName.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                         "background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.DDT_VideoName.setText("")
        self.DDT_VideoName.setObjectName("DDT_VideoName")
        self.DDT_QualityLabel = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_QualityLabel.setGeometry(QtCore.QRect(320, 130, 231, 41))
        self.DDT_QualityLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                            "background-color: rgb(0, 0, 0);\n"
                                            "color: rgb(255, 255, 255);")
        self.DDT_QualityLabel.setObjectName("DDT_QualityLabel")
        self.DDT_FormatLabel = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_FormatLabel.setGeometry(QtCore.QRect(590, 130, 251, 41))
        self.DDT_FormatLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                           "background-color: rgb(0, 0, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.DDT_FormatLabel.setObjectName("DDT_FormatLabel")
        self.DDT_BitrateLabel = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_BitrateLabel.setGeometry(QtCore.QRect(810, 120, 321, 61))
        self.DDT_BitrateLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                            "background-color: rgb(0, 0, 0);\n"
                                            "color: rgb(255, 255, 255);")
        self.DDT_BitrateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DDT_BitrateLabel.setObjectName("DDT_BitrateLabel")
        self.DDT_QualityBox = QtWidgets.QComboBox(self.DDT_Container)
        self.DDT_QualityBox.setGeometry(QtCore.QRect(290, 200, 231, 31))
        self.DDT_QualityBox.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                          "background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 20px;")
        self.DDT_QualityBox.setObjectName("DDT_QualityBox")
        self.DDT_FormatBox = QtWidgets.QComboBox(self.DDT_Container)
        self.DDT_FormatBox.setGeometry(QtCore.QRect(570, 200, 231, 31))
        self.DDT_FormatBox.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                         "background-color: rgb(85, 85, 127);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 20px;")
        self.DDT_FormatBox.setObjectName("DDT_FormatBox")
        self.DDT_BitrateBox = QtWidgets.QComboBox(self.DDT_Container)
        self.DDT_BitrateBox.setGeometry(QtCore.QRect(860, 200, 231, 31))
        self.DDT_BitrateBox.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                          "background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 20px;")
        self.DDT_BitrateBox.setObjectName("DDT_BitrateBox")
        self.DDT_DownloadButton = QtWidgets.QPushButton(self.DDT_Container)
        self.DDT_DownloadButton.setGeometry(QtCore.QRect(860, 480, 241, 41))
        self.DDT_DownloadButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                              "background-color: rgb(85, 85, 127);\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "border-radius: 20px;")
        self.DDT_DownloadButton.setObjectName("DDT_DownloadButton")
        self.DDT_CancelButton = QtWidgets.QPushButton(self.DDT_Container)
        self.DDT_CancelButton.setGeometry(QtCore.QRect(60, 480, 141, 41))
        self.DDT_CancelButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                            "background-color: rgb(85, 85, 127);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 20px;")
        self.DDT_CancelButton.setObjectName("DDT_CancelButton")
        self.DDT_VideoIcon = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_VideoIcon.setGeometry(QtCore.QRect(40, 190, 181, 181))
        self.DDT_VideoIcon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 20px;")
        self.DDT_VideoIcon.setText("")
        self.DDT_VideoIcon.setObjectName("DDT_VideoIcon")
        self.DDT_PathInput = QtWidgets.QLineEdit(self.DDT_Container)
        self.DDT_PathInput.setGeometry(QtCore.QRect(280, 340, 821, 41))
        self.DDT_PathInput.setStyleSheet("padding-left: 10px;\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border: 3px solid rgb(85, 85, 127);;\n"
                                         "border-radius: 10px;\n"
                                         "\n"
                                         "")
        self.DDT_PathInput.setText("default")
        self.DDT_PathInput.setObjectName("DDT_PathInput")
        self.DDT_PathLabel = QtWidgets.QLabel(self.DDT_Container)
        self.DDT_PathLabel.setGeometry(QtCore.QRect(300, 270, 851, 41))
        self.DDT_PathLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                         "background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.DDT_PathLabel.setObjectName("DDT_PathLabel")
        self.DDT_LabLabel = QtWidgets.QLabel(self.DownloadDetailsTab)
        self.DDT_LabLabel.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.DDT_LabLabel.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                        "background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.DDT_LabLabel.setObjectName("DDT_LabLabel")
        self.MainMenu.addWidget(self.DownloadDetailsTab)

        self.EditVideoTab = QtWidgets.QWidget()
        self.EditVideoTab.setObjectName("EditVideoTab")
        self.EDT_Icon_Path = None
        self.EDT_TabLabel = QtWidgets.QLabel(self.EditVideoTab)
        self.EDT_TabLabel.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.EDT_TabLabel.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                        "background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.EDT_TabLabel.setObjectName("EDT_TabLabel")
        self.EDT_Container = QtWidgets.QFrame(self.EditVideoTab)
        self.EDT_Container.setGeometry(QtCore.QRect(0, 50, 1181, 571))
        self.EDT_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "border-radius: 20px;")
        self.EDT_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EDT_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EDT_Container.setObjectName("EDT_Container")
        self.EDT_IconLabel = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_IconLabel.setGeometry(QtCore.QRect(60, 20, 261, 41))
        self.EDT_IconLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                         "background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.EDT_IconLabel.setObjectName("EDT_IconLabel")
        self.EDT_NameLabel = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_NameLabel.setGeometry(QtCore.QRect(380, 20, 351, 41))
        self.EDT_NameLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                         "background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.EDT_NameLabel.setObjectName("EDT_NameLabel")
        self.EDT_PathLabel = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_PathLabel.setGeometry(QtCore.QRect(380, 260, 431, 41))
        self.EDT_PathLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                         "background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.EDT_PathLabel.setObjectName("EDT_PathLabel")
        self.EDT_SaveButton = QtWidgets.QPushButton(self.EDT_Container)
        self.EDT_SaveButton.setGeometry(QtCore.QRect(720, 470, 391, 51))
        self.EDT_SaveButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                          "background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 20px;")
        self.EDT_SaveButton.setObjectName("EDT_SaveButton")
        self.EDT_ChangeButton = QtWidgets.QPushButton(self.EDT_Container)
        self.EDT_ChangeButton.setGeometry(QtCore.QRect(70, 310, 221, 51))
        self.EDT_ChangeButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                            "background-color: rgb(85, 85, 127);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 20px;")
        self.EDT_ChangeButton.setObjectName("EDT_ChangeButton")
        self.EDT_DescriptionLabel = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_DescriptionLabel.setGeometry(QtCore.QRect(380, 140, 491, 31))
        self.EDT_DescriptionLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                                "background-color: rgb(0, 0, 0);\n"
                                                "color: rgb(255, 255, 255);")
        self.EDT_DescriptionLabel.setObjectName("EDT_DescriptionLabel")
        self.EDT_CancelButton = QtWidgets.QPushButton(self.EDT_Container)
        self.EDT_CancelButton.setGeometry(QtCore.QRect(70, 460, 211, 51))
        self.EDT_CancelButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                            "background-color: rgb(85, 85, 127);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 20px;")
        self.EDT_CancelButton.setObjectName("EDT_CancelButton")
        self.EDT_NameInput = QtWidgets.QLineEdit(self.EDT_Container)
        self.EDT_NameInput.setGeometry(QtCore.QRect(370, 80, 751, 41))
        self.EDT_NameInput.setStyleSheet("padding-left: 10px;\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border: 3px solid rgb(85, 85, 127);;\n"
                                         "border-radius: 10px;\n"
                                         "\n"
                                         "")
        self.EDT_NameInput.setText("")
        self.EDT_NameInput.setObjectName("EDT_NameInput")
        self.EDT_DescriptionInput = QtWidgets.QLineEdit(self.EDT_Container)
        self.EDT_DescriptionInput.setGeometry(QtCore.QRect(370, 200, 751, 41))
        self.EDT_DescriptionInput.setStyleSheet("padding-left: 10px;\n"
                                                "background-color: rgb(255, 255, 255);\n"
                                                "border: 3px solid rgb(85, 85, 127);;\n"
                                                "border-radius: 10px;\n"
                                                "\n"
                                                "")
        self.EDT_DescriptionInput.setText("")
        self.EDT_DescriptionInput.setObjectName("EDT_DescriptionInput")
        self.EDT_Icon = QtWidgets.QLabel(self.EDT_Container)
        self.EDT_Icon.setGeometry(QtCore.QRect(70, 80, 221, 201))
        self.EDT_Icon.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border: 3px solid rgb(85, 85, 127);\n"
                                    "border-radius: 20px;")
        self.EDT_Icon.setText("")
        self.EDT_Icon.setObjectName("EDT_Icon")
        self.EDT_PathInput = QtWidgets.QLineEdit(self.EDT_Container)
        self.EDT_PathInput.setGeometry(QtCore.QRect(370, 320, 751, 41))
        self.EDT_PathInput.setStyleSheet("padding-left: 10px;\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border: 3px solid rgb(85, 85, 127);;\n"
                                         "border-radius: 10px;\n"
                                         "\n"
                                         "")
        self.EDT_PathInput.setText("")
        self.EDT_PathInput.setObjectName("EDT_PathInput")
        self.MainMenu.addWidget(self.EditVideoTab)
        self.DialogTab = QtWidgets.QWidget()
        self.DialogTab.setObjectName("DialogTab")
        self.DLG_Container = QtWidgets.QFrame(self.DialogTab)
        self.DLG_Container.setGeometry(QtCore.QRect(0, 50, 1181, 551))
        self.DLG_Container.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "border-radius: 20px;")
        self.DLG_Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DLG_Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DLG_Container.setObjectName("DLG_Container")
        self.DLG_TextLabel = QtWidgets.QLabel(self.DLG_Container)
        self.DLG_TextLabel.setGeometry(QtCore.QRect(420, 110, 341, 41))
        self.DLG_TextLabel.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                         "background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.DLG_TextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DLG_TextLabel.setObjectName("DLG_TextLabel")
        self.DLG_AcceptButton = QtWidgets.QPushButton(self.DLG_Container)
        self.DLG_AcceptButton.setGeometry(QtCore.QRect(620, 280, 221, 51))
        self.DLG_AcceptButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                            "background-color: rgb(85, 85, 127);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 20px;")
        self.DLG_AcceptButton.setObjectName("DLG_AcceptButton")
        self.DLG_CancelButton = QtWidgets.QPushButton(self.DLG_Container)
        self.DLG_CancelButton.setGeometry(QtCore.QRect(340, 280, 221, 51))
        self.DLG_CancelButton.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                            "background-color: rgb(85, 85, 127);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 20px;")
        self.DLG_CancelButton.setObjectName("DLG_CancelButton")
        self.DLG_DetailsLabel = QtWidgets.QLabel(self.DLG_Container)
        self.DLG_DetailsLabel.setGeometry(QtCore.QRect(40, 170, 1081, 41))
        self.DLG_DetailsLabel.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                            "background-color: rgb(0, 0, 0);\n"
                                            "color: rgb(255, 255, 255);")
        self.DLG_DetailsLabel.setText("")
        self.DLG_DetailsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DLG_DetailsLabel.setObjectName("DLG_DetailsLabel")
        self.DLG_TabLabel = QtWidgets.QLabel(self.DialogTab)
        self.DLG_TabLabel.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.DLG_TabLabel.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                        "background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.DLG_TabLabel.setObjectName("DLG_TabLabel")
        self.MainMenu.addWidget(self.DialogTab)

        # disabling some controls, at start of executing app
        self.enable_video_controls_buttons(False)
        self.enable_download_tab_downloading_controls(False)
        self.EDT_PathLabel.setEnabled(False)
        self.set_disabled_download_combo_boxes()
        self.MainMenu.setCurrentIndex(0)

        self.window.setCentralWidget(self.WorkSpace)
        self.set_text_for_elements(self.window)
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def main_window_icon_install(self, path_to_ico: str):
        """
            Set the icon for application window and at the panel view.

            Parameters:
            - path_to_ico (str): The path to the .ico file to be used as the window icon.

            Returns:
            - None
        """
        self.app.setWindowIcon(QIcon(path_to_ico))
        self.window.setWindowIcon(QIcon(path_to_ico))

    def view_set_feedback(self, controller):
        """
            Set the controller for the view.

            Parameters:
            - controller: The controller object to be associated with this view.

            Returns:
            - None
        """
        self.controller = controller

    def setup_graphical_events(self):
        """
            Set up QT signals of UI objects to controller handlers (slots).

            Returns:
            - None
        """

        # connecting signals of ui objects to controller handlers in video tab

        self.VideosTabButton.clicked.connect(lambda: self.controller.user_switch_to_video_tab_handler())
        self.VideosTabButton.enterEvent = lambda event: self.highlight_item_border(self.VideosTabButton, self.px_low)
        self.VideosTabButton.leaveEvent = lambda event: self.unhighlight_item_border(self.VideosTabButton, self.px_low)
        self.VID_UpButton.clicked.connect(lambda: self.controller.user_click_scroll_up_page_handler())
        self.VID_DownButton.clicked.connect(lambda: self.controller.user_click_scroll_down_page_handler())
        self.VID_DeleteButton.clicked.connect(lambda: self.controller.user_click_delete_selected_video_handler())
        self.VID_EditButton.clicked.connect(lambda: self.controller.user_click_edit_selected_video_handler())
        self.VID_WatchButton.clicked.connect(lambda: self.controller.user_click_watch_selected_video_handler())
        self.VID_DownButton.enterEvent = lambda event: self.highlight_item_border(self.VID_DownButton, self.px_low)
        self.VID_DownButton.leaveEvent = lambda event: self.unhighlight_item_border(self.VID_DownButton, self.px_low)
        self.VID1_Icon.mousePressEvent = lambda event: self.controller.user_select_first_video_handler()
        self.VID2_Icon.mousePressEvent = lambda event: self.controller.user_select_second_video_handler()
        self.VID_UpButton.enterEvent = lambda event: self.highlight_item_border(self.VID_UpButton, self.px_low)
        self.VID_UpButton.leaveEvent = lambda event: self.unhighlight_item_border(self.VID_UpButton, self.px_low)
        self.VID1_Icon.enterEvent = lambda event: self.highlight_item_border(self.VID1_Icon, self.px_low)
        self.VID1_Icon.leaveEvent = lambda event: self.unhighlight_item_border(self.VID1_Icon, self.px_low)
        self.VID2_Icon.enterEvent = lambda event: self.highlight_item_border(self.VID2_Icon, self.px_low)
        self.VID2_Icon.leaveEvent = lambda event: self.unhighlight_item_border(self.VID2_Icon, self.px_low)
        self.VID_WatchButton.enterEvent = lambda event: self.highlight_item_border(self.VID_WatchButton, self.px_low)
        self.VID_WatchButton.leaveEvent = lambda event: self.unhighlight_item_border(self.VID_WatchButton, self.px_low)
        self.VID_EditButton.enterEvent = lambda event: self.highlight_item_border(self.VID_EditButton, self.px_low)
        self.VID_EditButton.leaveEvent = lambda event: self.unhighlight_item_border(self.VID_EditButton, self.px_low)
        self.VID_DeleteButton.enterEvent = lambda event: self.highlight_item_border(self.VID_DeleteButton, self.px_low)
        self.VID_DeleteButton.leaveEvent = lambda event: self.unhighlight_item_border(self.VID_DeleteButton,
                                                                                      self.px_low)

        # connecting signals of ui objects to controller handlers in dialog tab (only for delete video menu now)

        self.DLG_AcceptButton.mousePressEvent = lambda event: self.controller.user_click_accept_delete_handler()
        self.DLG_CancelButton.mousePressEvent = lambda event: self.controller.user_click_cancel_handler()

        # connecting signals of ui objects to controller handlers in edit video tab

        self.EDT_SaveButton.mousePressEvent = lambda event: self.controller.user_click_accept_edit_handler()
        self.EDT_CancelButton.mousePressEvent = lambda event: self.controller.user_click_cancel_handler()
        self.EDT_ChangeButton.clicked.connect(lambda: self.edit_video_tab_icon_file_discovery())
        self.DDT_CancelButton.clicked.connect(lambda: self.controller.user_click_cancel_handler())
        self.EDT_PathInput.mousePressEvent = lambda event: self.edit_video_tab_new_directory_discover()
        self.EDT_SaveButton.enterEvent = lambda event: self.highlight_item_border(self.EDT_SaveButton, self.px_low)
        self.EDT_SaveButton.leaveEvent = lambda event: self.unhighlight_item_border(self.EDT_SaveButton, self.px_low)
        self.EDT_CancelButton.enterEvent = lambda event: self.highlight_item_border(self.EDT_CancelButton, self.px_low)
        self.EDT_CancelButton.leaveEvent = lambda event: self.unhighlight_item_border(self.EDT_CancelButton,
                                                                                      self.px_low)
        self.EDT_ChangeButton.enterEvent = lambda event: self.highlight_item_border(self.EDT_ChangeButton, self.px_low)
        self.EDT_ChangeButton.leaveEvent = lambda event: self.unhighlight_item_border(self.EDT_ChangeButton,
                                                                                      self.px_low)

        # connecting signals of ui objects to controller handlers in download and find video tabs

        self.DownloadTabButton.clicked.connect(lambda: self.controller.user_switch_to_download_tab_handler())
        self.DOW_FindButton.clicked.connect(lambda: self.controller.user_click_find_youtube_video_handler())
        self.DDT_DownloadButton.clicked.connect(lambda: self.controller.user_clicked_download_youtube_video_handler())
        self.DDT_QualityBox.currentIndexChanged.connect(lambda: self.controller.user_select_resolution_handler())
        self.DDT_FormatBox.currentIndexChanged.connect(lambda: self.controller.user_select_format_handler())
        self.DDT_BitrateBox.currentIndexChanged.connect(lambda: self.controller.user_select_fps())
        self.DDT_PathInput.mousePressEvent = lambda event: self.download_video_tab_save_directory_discover()
        self.DDT_CancelButton.enterEvent = lambda event: self.highlight_item_border(self.DDT_CancelButton, self.px_low)
        self.DDT_CancelButton.leaveEvent = lambda event: self.unhighlight_item_border(self.DDT_CancelButton,
                                                                                      self.px_low)
        self.DDT_DownloadButton.enterEvent = lambda event: self.highlight_item_border(self.DDT_DownloadButton,
                                                                                      self.px_low)
        self.DDT_DownloadButton.leaveEvent = lambda event: self.unhighlight_item_border(self.DDT_DownloadButton,
                                                                                        self.px_low)
        self.DownloadTabButton.enterEvent = lambda event: self.highlight_item_border(self.DownloadTabButton,
                                                                                     self.px_low)
        self.DownloadTabButton.leaveEvent = lambda event: self.unhighlight_item_border(self.DownloadTabButton,
                                                                                       self.px_low)
        self.DOW_FindButton.enterEvent = lambda event: self.highlight_item_border(self.DOW_FindButton, self.px_low)
        self.DOW_FindButton.leaveEvent = lambda event: self.unhighlight_item_border(self.DOW_FindButton, self.px_low)

        self.DLG_AcceptButton.enterEvent = lambda event: self.highlight_item_border(self.DLG_AcceptButton, self.px_low)
        self.DLG_AcceptButton.leaveEvent = lambda event: self.unhighlight_item_border(self.DLG_AcceptButton,
                                                                                      self.px_low)
        self.DLG_CancelButton.enterEvent = lambda event: self.highlight_item_border(self.DLG_CancelButton, self.px_low)
        self.DLG_CancelButton.leaveEvent = lambda event: self.unhighlight_item_border(self.DLG_CancelButton,
                                                                                      self.px_low)

        # connecting signals of ui objects to controller and view handlers in preview show tab

        self.PT_CancelButton.clicked.connect(lambda: self.controller.user_close_video_preview_handler())
        self.PT_CancelButton.enterEvent = lambda event: self.highlight_item_border(self.PT_CancelButton, self.px_low)
        self.PT_CancelButton.leaveEvent = lambda event: self.unhighlight_item_border(self.PT_CancelButton, self.px_low)
        self.PT_StopOrPlayButton.enterEvent = lambda event: self.highlight_item_border(self.PT_StopOrPlayButton,
                                                                                       self.px_low)
        self.PT_StopOrPlayButton.leaveEvent = lambda event: self.unhighlight_item_border(self.PT_StopOrPlayButton,
                                                                                         self.px_low)
        self.PT_ShipForwardButton.enterEvent = lambda event: self.highlight_item_border(self.PT_ShipForwardButton,
                                                                                        self.px_low)
        self.PT_ShipForwardButton.leaveEvent = lambda event: self.unhighlight_item_border(self.PT_ShipForwardButton,
                                                                                          self.px_low)
        self.PT_SkipBackButton.enterEvent = lambda event: self.highlight_item_border(self.PT_SkipBackButton,
                                                                                     self.px_low)
        self.PT_SkipBackButton.leaveEvent = lambda event: self.unhighlight_item_border(self.PT_SkipBackButton,
                                                                                       self.px_low)

    def set_text_for_elements(self, main_window):
        """
           Set text for UI elements in the main window.

           Parameters:
           - main_window: The main window object to set text for.

           Returns:
           - None
        """

        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "YTSaver"))
        self.VideosTabButton.setText(_translate("MainWindow", "История загрузки"))
        self.DownloadTabButton.setText(_translate("MainWindow", "Найти и загрузить"))
        self.VID_UpButton.setText(_translate("MainWindow", "↑"))
        self.VID_DownButton.setText(_translate("MainWindow", "↓"))
        self.VID1_Container.setTitle(_translate("MainWindow", "GroupBox"))
        self.VID2_Container.setTitle(_translate("MainWindow", "GroupBox"))
        self.VID_NothingLabel.setText(_translate("MainWindow", "Ничего не найдено :("))
        self.VID_WatchButton.setText(_translate("MainWindow", "Открыть превью"))
        self.VID_DeleteButton.setText(_translate("MainWindow", "Удалить"))
        self.VID_EditButton.setText(_translate("MainWindow", "Редактирование"))
        self.VID_ControlsLabel.setText(_translate("MainWindow", "Управление выбранным \n"
                                                                "видео:"))
        self.VID_TabLabel.setText(_translate("MainWindow", "Найдено видео:"))
        self.VID_CountValue.setText(_translate("MainWindow", "0"))
        self.DOW_FindButton.setText(_translate("MainWindow", "Найти виде в YouTube!"))
        self.DOW_LinkInput.setText(_translate("MainWindow", "Вставьте вашу ссылку сюда"))
        self.DOW_TabLabel.setText(_translate("MainWindow", "Поиск видео"))
        self.PT_CancelButton.setText(_translate("MainWindow", "Назад"))
        self.PT_StopOrPlayButton.setText(_translate("MainWindow", "Воспроизвести / Стоп"))
        self.PT_ShipForwardButton.setText(_translate("MainWindow", ">> 5"))
        self.PT_SkipBackButton.setText(_translate("MainWindow", "5 << "))
        self.DDT_QualityLabel.setText(_translate("MainWindow", "Выберите качество:"))
        self.DDT_FormatLabel.setText(_translate("MainWindow", "Выберите видеоформат:"))
        self.DDT_BitrateLabel.setText(_translate("MainWindow", "Выберите FPS:"))
        self.DDT_DownloadButton.setText(_translate("MainWindow", "Загрузить!"))
        self.DDT_CancelButton.setText(_translate("MainWindow", "Назад"))
        self.DDT_PathLabel.setText(_translate("MainWindow",
                                              "Выберите путь для загрузки:                       (default - сохранить в папку приложения)"))
        self.DDT_LabLabel.setText(_translate("MainWindow", "Детали загрузки"))
        self.EDT_TabLabel.setText(_translate("MainWindow", "Редактирование информации"))
        self.EDT_IconLabel.setText(_translate("MainWindow", "Выберите новую иконку:"))
        self.EDT_NameLabel.setText(_translate("MainWindow", "Придумайте новое имя файла:"))
        self.EDT_PathLabel.setText(_translate("MainWindow", "Выберите новое расположение видео:"))
        self.EDT_SaveButton.setText(_translate("MainWindow", "Сохранить изменения"))
        self.EDT_ChangeButton.setText(_translate("MainWindow", "Выбрать"))
        self.EDT_DescriptionLabel.setText(_translate("MainWindow", "Дайте новое короткое описание видео:"))
        self.EDT_CancelButton.setText(_translate("MainWindow", "Назад"))
        self.DLG_TextLabel.setText(_translate("MainWindow", "Подвердите действие:"))
        self.DLG_AcceptButton.setText(_translate("MainWindow", "Подвердить"))
        self.DLG_CancelButton.setText(_translate("MainWindow", "Отмена"))
        self.DLG_TabLabel.setText(_translate("MainWindow", "Опасная операция"))

    def edit_video_tab_icon_file_discovery(self):
        """
            Open a file dialog to discover an image file in the edit video tab and set selected file
            as the icon for video (only in edit video tab).

            Returns:
            - None
        """
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")

        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()
            self.EDT_Icon_Path = selected_file[0]
            self.install_image_in_icon(self.EDT_Icon, self.EDT_Icon_Path)

    def edit_video_tab_new_directory_discover(self):
        """
            Open a file dialog to discover a new directory for the video in edit tab and
            set selected directory path in path input field.

            Returns:
            - None
        """
        directory = QFileDialog.getExistingDirectory(self.window, 'Выберите директорию', '/')
        self.EDT_PathInput.setText(directory)

    def download_video_tab_save_directory_discover(self):
        """
            Open a file dialog to discover a save directory for the video in download tab and
            set selected directory path in path input field.

            Returns:
            - None
        """
        directory = QFileDialog.getExistingDirectory(self.window, 'Выберите директорию', '/')
        self.DDT_PathInput.setText(directory)

    def install_image_in_icon(self, icon_label, image: str):
        """
            Install an image in the specified icon_label.

            Parameters:
            - icon_label: The QLabel object where the image will be installed.
            - image (str): The path to the image file.

            Returns:
            - None
        """
        pixmap = QPixmap(image)
        scaled_pixmap = pixmap.scaledToHeight(icon_label.height())
        icon_label.setPixmap(scaled_pixmap)
        icon_label.setScaledContents(True)

    def main_window_open(self, allow_open: bool):
        """
            Show or hide the main window based on the allow flag.

            Parameters:
            - allow_open (bool): A flag indicating whether to show or hide the main window.

            Returns:
            - None
        """
        if allow_open:
            self.window.show()
        else:
            self.window.hide()

    def highlight_item_border(self, item, border_px: int):
        """
            Highlight the border of the specified item by adding a white solid border with the specified width.

            Parameters:
            - item: The qt object to highlight.
            - border_px (int): The width of the border in pixels.

            Returns:
            - None
        """
        current_style = item.styleSheet()
        new_style = current_style + f";border: {border_px}px solid white;"
        item.setStyleSheet(new_style)

    def unhighlight_item_border(self, item, border_px: int):
        """
            Unhighlight the border of the specified item by removing a white solid border with the specified width.

            Parameters:
            - item: The qt object to unhighlight.
            - border_px (int): The width of the border in pixels.

            Returns:
            - None
        """
        current_style = item.styleSheet()
        new_style = current_style.replace(f"border: {border_px}px solid white;", "")
        item.setStyleSheet(new_style)

    def set_disabled_style_for_element(self, element):
        """
            Set a disabled style for the specified element by changing its stylesheet
            and disabling the element.

            Parameters:
            - element: The qt object to apply the disabled style to.

            Returns:
            - None
        """
        current_style = element.styleSheet()
        new_style = current_style + f";background-color: lightgray; color: darkgray;"
        element.setStyleSheet(new_style)
        element.setEnabled(False)

    def set_enabled_style_for_element(self, element):
        """
            Set enabled style for the specified element by changing its stylesheet
            and enabling the element.

            Parameters:
            - element: The qt object to apply the disabled style to.

            Returns:
            - None
        """
        current_style = element.styleSheet()
        new_style = current_style.replace(f";background-color: lightgray; color: darkgray;", "")
        element.setStyleSheet(new_style)
        element.setEnabled(True)

    def set_first_video_container_info(self, video_info: dict):
        """
            Set the information for the first video container using the provided video_info dictionary.

            Parameters:
            - video_info (dict): A dictionary containing information about the video, including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_date': The creation date of the video.

            Returns:
            - None
        """
        self.VID1_NameLabel.setText(str(video_info['video_name']))
        self.VID1_DescriptionLabel.setText(str(video_info['video_desc']))
        self.VID1_PathLabel.setText(str(video_info['video_path']))
        self.VID1_DateCreationLabel.setText(str(video_info['video_date']))

    def set_second_video_container_info(self, video_info: dict):
        """
            Set the information for the second video container using the provided video_info dictionary.

            Parameters:
            - video_info (dict): A dictionary containing information about the video, including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_date': The creation date of the video.

            Returns:
            - None
        """
        self.VID2_NameLabel.setText(str(video_info['video_name']))
        self.VID2_DescriptionLabel.setText(str(video_info['video_desc']))
        self.VID2_PathLabel.setText(str(video_info['video_path']))
        self.VID2_DateCreationLabel.setText(str(video_info['video_date']))

    def videos_containers_empty(self):
        """
            Hide both video containers and show a label indicating that there are no videos.

            Returns:
            - None
        """
        self.VID_NothingLabel.setVisible(True)
        self.VID1_Container.setVisible(False)
        self.VID2_Container.setVisible(False)

    def videos_containers_not_empty(self):
        """
            Hide a label indicating that there are no videos.

            Returns:
            - None
        """
        self.VID_NothingLabel.setVisible(False)

    def set_videos_count_text(self, count: int):
        """
            Set the text of the video count label to the specified count.

            Parameters:
            - count (int): The count of videos.

            Returns:
            - None
        """
        self.VID_CountValue.setText(str(count))

    def display_first_video_container(self, data: dict):
        """
            Display the first video container with the provided data.

            Parameters:
            - data (dict): A dictionary containing information about the video, including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_date': The creation date of the video.
                - 'video_icon': The icon image for the video.

            Returns:
            - None
        """
        self.set_first_video_container_info(data)
        self.VID1_Container.setVisible(True)
        self.install_image_in_icon(self.VID1_Icon, data['video_icon'])

    def hide_first_video_container(self):
        """
            Hide the first video container.

            Returns:
            - None
        """
        self.VID1_Container.setVisible(False)

    def display_second_video__container(self, data: dict):
        """
            Display the second video container with the provided data.

            Parameters:
            - data (dict): A dictionary containing information about the video, including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_date': The creation date of the video.
                - 'video_icon': The icon image for the video.

            Returns:
            - None
        """
        self.set_second_video_container_info(data)
        self.VID2_Container.setVisible(True)
        self.install_image_in_icon(self.VID2_Icon, data['video_icon'])

    def hide_second_video_container(self):
        """
            Hide the first video container.

            Returns:
            - None
        """
        self.VID2_Container.setVisible(False)

    def mark_first_video_as_selected(self, flag: bool):
        """
            Mark the first video icon as selected or unselected based on the flag value.

            Parameters:
            - flag (bool): A boolean flag indicating whether the first video should be selected.

            Returns:
            - None
        """
        if flag:
            self.highlight_item_border(self.VID1_Icon, self.px_medium)
            self.unhighlight_item_border(self.VID2_Icon, self.px_medium)
        else:
            self.unhighlight_item_border(self.VID1_Icon, self.px_medium)

    def mark_second_video_as_selected(self, flag: bool):
        """
            Mark the second video icon as selected or unselected based on the flag value.

            Parameters:
            - flag (bool): A boolean flag indicating whether the first video should be selected.

            Returns:
            - None
        """
        if flag:
            self.highlight_item_border(self.VID2_Icon, self.px_medium)
            self.unhighlight_item_border(self.VID1_Icon, self.px_medium)
        else:
            self.unhighlight_item_border(self.VID2_Icon, self.px_medium)

    def enable_video_controls_buttons(self, flag: bool):
        """
            Enable or disable video control buttons based on the flag value.

            Parameters:
            - flag (bool): A boolean flag indicating whether to enable or disable the video control buttons.

            Returns:
            - None
        """
        if flag:
            self.set_enabled_style_for_element(self.VID_WatchButton)
            self.set_enabled_style_for_element(self.VID_EditButton)
            self.set_enabled_style_for_element(self.VID_DeleteButton)
            self.VID_WatchButton.setEnabled(True)
            self.VID_EditButton.setEnabled(True)
            self.VID_DeleteButton.setEnabled(True)
        else:
            self.set_disabled_style_for_element(self.VID_WatchButton)
            self.set_disabled_style_for_element(self.VID_EditButton)
            self.set_disabled_style_for_element(self.VID_DeleteButton)
            self.VID_WatchButton.setEnabled(False)
            self.VID_EditButton.setEnabled(False)
            self.VID_DeleteButton.setEnabled(False)

    def open_edit_video_tab(self, video: dict):
        """
            Open the edit video tab and fill it with the details of the provided video.

            Parameters:
            - video (dict): A dictionary containing information about the video, including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_icon': The icon image for the video.

            Returns:
            - None
        """

        self.MainMenu.setCurrentWidget(self.EditVideoTab)

        path, _ = os.path.split(video['video_path'])
        name = video['video_name']
        desc = video['video_desc']
        icon = video['video_icon']

        self.EDT_NameInput.setText(name)
        self.EDT_DescriptionInput.setText(desc)
        self.EDT_PathInput.setText(path)
        self.EDT_Icon_Path = icon
        self.install_image_in_icon(self.EDT_Icon, icon)

    def open_video_preview_tab(self, data: dict):
        """
            Open the video preview tab and initialize the video player with the provided data.

            Parameters:
            - data (dict): A dictionary containing information about the video, including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_icon': The icon image for the video.

            Returns:
            - None
        """
        self.MainMenu.setCurrentWidget(self.PreviewTab)
        self.player = VideoPlayer(
            video_path=data['video_path'],
            output_widget=self.PT_Video,
            pause_widget=self.PT_StopOrPlayButton,
            back_widget=self.PT_SkipBackButton,
            forward_widget=self.PT_ShipForwardButton,
            time_widget=self.PT_TimeLabel)

    def clode_video_preview_tab(self):
        """
            Close the video preview tab and delete the video player object.

            Returns:
            - None
        """
        self.MainMenu.setCurrentWidget(self.VideoTab)
        del self.player

    def get_data_from_edit_video_tab(self):
        """
            Retrieve data from the edit video tab inputs and return it as a dictionary.

            Returns:
            - dict: A dictionary containing the video information including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_icon': The icon path of the video.
        """

        info = {
            'video_name': self.EDT_NameInput.text(),
            'video_desc': self.EDT_DescriptionInput.text(),
            'video_path': self.EDT_PathInput.text(),
            'video_icon': self.EDT_Icon_Path
        }
        return info

    def get_data_from_find_tab(self):
        """
            Retrieve the URL input from the find tab.

            Returns:
            - str: The URL input from the find tab.
        """

        url = self.DOW_LinkInput.text()
        return url

    def get_data_from_download_tab(self):
        """
            Retrieve data from the download tab inputs and return it as a dictionary.

            Returns:
            - dict: A dictionary containing the download information including:
                - 'resolution': The selected resolution.
                - 'format': The selected format.
                - 'fps': The selected frames per second.
                - 'path': The download path input.
        """

        info = {
            'resolution': self.DDT_QualityBox.currentText(),
            'format': self.DDT_FormatBox.currentText(),
            'fps': self.DDT_BitrateBox.currentText(),
            'path': self.DDT_PathInput.text()
        }
        return info

    def display_available_resolutions(self, resolutions: list):
        """
            Fill items of the available resolutions in the download tab QualityBox (QComboBox).

            Parameters:
            - resolutions (list): A list of available resolutions.

            Returns:
            - None
        """

        self.DDT_QualityBox.blockSignals(True)

        self.set_disabled_style_for_element(self.DDT_FormatBox)
        self.set_disabled_style_for_element(self.DDT_BitrateBox)
        self.DDT_QualityBox.clear()
        self.set_enabled_style_for_element(self.DDT_QualityBox)
        self.DDT_QualityBox.addItem('-')
        for element in resolutions:
            self.DDT_QualityBox.addItem(element)

        self.DDT_QualityBox.blockSignals(False)

    def display_available_formats(self, formats: list):
        """
            Fill items of the available formats in the download tab FormatBox (QComboBox).

            Parameters:
            - formats (list): A list of available formats.

            Returns:
            - None
        """

        self.DDT_FormatBox.blockSignals(True)

        self.set_disabled_style_for_element(self.DDT_BitrateBox)
        self.DDT_FormatBox.clear()
        self.set_enabled_style_for_element(self.DDT_FormatBox)
        self.DDT_FormatBox.addItem('-')
        for element in formats:
            self.DDT_FormatBox.addItem(element)

        self.DDT_FormatBox.blockSignals(False)

    def display_available_fps(self, frames: list):
        """
            Fill items of the available fps in the download tab BitrateBox (QComboBox).

            Parameters:
            - fps (list): A list of available fps.

            Returns:
            - None
        """

        self.DDT_BitrateBox.blockSignals(True)

        self.DDT_BitrateBox.clear()
        self.set_enabled_style_for_element(self.DDT_BitrateBox)
        self.DDT_BitrateBox.addItem('-')
        for element in frames:
            self.DDT_BitrateBox.addItem(str(element))

        self.DDT_BitrateBox.blockSignals(False)

    def set_disabled_download_combo_boxes(self):
        """
            Set the download tab combo boxes to a disabled style.

            Returns:
            - None
        """

        self.set_disabled_style_for_element(self.DDT_FormatBox)
        self.set_disabled_style_for_element(self.DDT_QualityBox)
        self.set_disabled_style_for_element(self.DDT_BitrateBox)

    def enable_download_tab_downloading_controls(self, flag: bool):
        """
            Enable or disable the download tab downloading controls based on the provided flag.

            Parameters:
            - flag (bool): Flag to enable or disable the controls.

            Returns:
            - None
        """
        if flag:
            self.set_enabled_style_for_element(self.DDT_DownloadButton)
            self.DDT_DownloadButton.setEnabled(True)
        else:
            self.set_disabled_style_for_element(self.DDT_DownloadButton)
            self.DDT_DownloadButton.setEnabled(False)

    def enable_download_tab_cancel_controls(self, flag: bool):
        """
            Enable or disable the download tab cancel controls based on the provided flag.

            Parameters:
            - flag (bool): Flag to enable or disable the controls.

            Returns:
            - None
        """
        if flag:
            self.set_enabled_style_for_element(self.DDT_CancelButton)
            self.DDT_CancelButton.setEnabled(True)
        else:
            self.set_disabled_style_for_element(self.DDT_CancelButton)
            self.DDT_CancelButton.setEnabled(False)

    def enable_controls_while_downloading(self, flag: bool):
        """
            Enable or disable the nav bar and download tab controls based on the provided flag.

            Parameters:
            - flag (bool): Flag to enable or disable the controls.

            Returns:
            - None
        """
        self.enable_download_tab_downloading_controls(flag)
        self.enable_navigation_bar_controls(flag)
        self.enable_download_tab_cancel_controls(flag)

        if flag:
            self.DDT_QualityBox.setEnabled(True)
            self.DDT_FormatBox.setEnabled(True)
            self.DDT_BitrateBox.setEnabled(True)
        else:
            self.DDT_QualityBox.setEnabled(False)
            self.DDT_FormatBox.setEnabled(False)
            self.DDT_BitrateBox.setEnabled(False)

    def enable_navigation_bar_controls(self, flag: bool):
        """
            Enable or disable the nav bar controls based on the provided flag.

            Parameters:
            - flag (bool): Flag to enable or disable the controls.

            Returns:
            - None
        """
        if flag:
            self.set_enabled_style_for_element(self.VideosTabButton)
            self.VideosTabButton.setEnabled(True)
            self.set_enabled_style_for_element(self.DownloadTabButton)
            self.DownloadTabButton.setEnabled(True)
        else:
            self.set_disabled_style_for_element(self.VideosTabButton)
            self.VideosTabButton.setEnabled(False)
            self.set_disabled_style_for_element(self.DownloadTabButton)
            self.DownloadTabButton.setEnabled(False)

    def switch_to_video_tab(self):
        """
            Switch the main widget to the video tab.

            Returns:
            - None
        """

        self.MainMenu.setCurrentWidget(self.VideoTab)

    def switch_to_download_tab(self):
        """
            Switch the main widget to the download tab.

            Returns:
            - None
        """

        self.MainMenu.setCurrentWidget(self.DownloadTab)

    def switch_to_download_details_tab(self, data: dict):
        """
            Switch the current widget to the download details tab and populate it with the provided data.

            Parameters:
            - data (dict): A dictionary containing the following keys:
                - 'resolutions': A list of available resolutions.
                - 'video_icon': The image for the video icon.
                - 'video_name': The name of the video.

            Returns:
            - None
        """

        self.MainMenu.setCurrentWidget(self.DownloadDetailsTab)
        self.display_available_resolutions(data['resolutions'])
        self.install_image_in_icon(self.DDT_VideoIcon, data['video_icon'])
        self.DDT_VideoName.setText(data['video_name'])

    def switch_to_delete_tab(self, msg: str):
        """
            Switch the main widget to the delete tab and display the provided message.

            Parameters:
            - msg (str): The message to display in the delete tab.

            Returns:
            - None
        """

        self.MainMenu.setCurrentWidget(self.DialogTab)
        self.DLG_DetailsLabel.setText(msg)

    def set_text_app_messenger(self, msg: str):
        """
            Set the text in the AppMessengerOutput to the provided message.

            Parameters:
            - msg (str): The message to set in the AppMessengerOutput.

            Returns:
            - None
        """

        self.AppMessengerOutput.setText(msg)

    def show_critical_error_window(self, error_message: str):
        """
            Show a critical error window with the provided error message.

            Parameters:
            - error_message (str): The error message to display in the window.

            Returns:
            - None
        """

        error_window = QMessageBox()
        error_window.setFixedSize(1000, 200)
        error_window.critical(self.window, 'Ошибка', error_message)
