#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Script Name: TopTab3.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import sys, os

# PyQt5
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QGraphicsView, QGraphicsScene, QSizePolicy,
                             QPushButton, QGroupBox)

# Plt
import appData as app

from ui import uirc as rc
from ui import UserSetting
from utilities import localSQL as usql
from utilities import utils as func

# -------------------------------------------------------------------------------------------------------------
""" Configure the current level to make it disable certain log """

# logger = app.set_log()

# -------------------------------------------------------------------------------------------------------------
""" TopTab3 """

class TopTab3(QWidget):

    showPlt = pyqtSignal(bool)
    showLogin = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(TopTab3, self).__init__(parent)

        self.settings = app.APPSETTING
        self.layout = QGridLayout()
        self.buildUI()
        self.setLayout(self.layout)

    def buildUI(self):
        self.query = usql.QuerryDB()
        try:
            self.username, token, cookie, remember = self.query.query_table('curUser')
        except IndexError:
            self.username = 'DemoUser'

        avatarPth = func.getAvatar(self.username)
        avatar = QPixmap(avatarPth)
        self.avatarScene = QGraphicsScene()
        self.avatarScene.addPixmap(avatar)
        self.avatarView = QGraphicsView()
        self.avatarView.setScene(self.avatarScene)

        self.avatarView.scale(100 / avatar.width(), 100 / avatar.height())

        self.avatarView.aspectRatioMode = Qt.KeepAspectRatio
        self.avatarView.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.avatarView.setFixedSize(100, 100)

        btn1 = QPushButton('Account Setting')
        btn1.clicked.connect(self.on_userSettingBtn_clicked)

        btn2 = QPushButton('Log Out')
        btn2.clicked.connect(self.on_signOutBtn_clicked)

        btns = [btn1, btn2]

        sec1Grp = rc.AutoSectionBtnGrp(self.username, [self.avatarView], "ImageView")
        sec2Grp = rc.AutoSectionBtnGrp("Setting", btns, "BtnGrid")

        sec3Grp = QGroupBox("Messenger")
        sec3Grid = QGridLayout()
        sec3Grp.setLayout(sec3Grid)

        self.layout.addWidget(sec1Grp, 0, 0, 1, 1)
        self.layout.addWidget(sec2Grp, 1, 0, 1, 1)
        self.layout.addWidget(sec3Grp, 0, 1, 2, 2)

        self.applySetting()

    def update_avatar(self, param):
        print("get signal at final des {0}".format(param))

    def on_userSettingBtn_clicked(self):
        layout = UserSetting.Account_setting()
        layout.show()
        layout.updateAvatar.connect(self.update_avatar)
        layout.exec_()

    def on_signOutBtn_clicked(self):
        self.settings.setValue("showMain", False)
        self.settings.setValue("showLogin", True)
        self.showPlt.emit(False)
        self.showLogin.emit(True)

    def applySetting(self):
        pass


def main():
    app = QApplication(sys.argv)
    layout = TopTab3()
    layout.show()
    app.exec_()

if __name__ == '__main__':
    main()

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 25/05/2018