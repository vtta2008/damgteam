#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Script Name: {[$]}.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import sys, os
from functools import partial

# PyQt5
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

# Plt
from utilities.localSQL import TimeLog
from ui import uirc as rc
from ui.lib.LayoutPreset import Action
from utilities.pUtils import get_layout_dimention

from appData import APPINFO, __plmWiki__, CONFIG_DIR, APP_ICON_DIR, SETTING_DIR, ROOT_DIR
from core.Specs import Specs
from core.Loggers import SetLogger

# -------------------------------------------------------------------------------------------------------------
""" Menu bar Layout """

class SubMenuBar(QMainWindow):

    key = 'subMenu'
    showLayout = pyqtSignal(str, str)
    executing = pyqtSignal(str)
    proceduring = pyqtSignal(str)
    addLayout = pyqtSignal(object)
    setSetting = pyqtSignal(str, str, str)
    openUrl = pyqtSignal(str)

    def __init__(self, parent=None):
        super(SubMenuBar, self).__init__(parent)

        self.specs = Specs(self.key, self)
        self.logger = SetLogger(self)
        self.appInfo = APPINFO
        self.url = __plmWiki__
        self.buildMenu()
        self.setMaximumHeight(20)

    def buildMenu(self):

        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addMenu("New Organisation")
        self.fileMenu.addMenu("New group/team")
        self.fileMenu.addSeparator()
        self.fileMenu.addMenu("New project")
        self.fileMenu.addSeparator()

        self.gotoMenu = self.menuBar().addMenu('Go to')
        self.gotoMenu.addAction(Action({'icon': 'ConfigFolder', 'txt': 'Config folder', 'trg':partial(self.executing.emit, CONFIG_DIR)}, self))
        self.gotoMenu.addAction(Action({'icon': 'IconFolder', 'txt': 'Icon folder', 'trg': partial(self.executing.emit, APP_ICON_DIR)}, self))
        self.gotoMenu.addAction(Action({'icon': 'SettingFolder', 'txt': 'Setting folder', 'trg': partial(self.executing.emit, SETTING_DIR)}, self))
        self.gotoMenu.addAction(Action({'icon': 'AppFolder', 'txt': 'Application folder', 'trg': partial(self.executing.emit, ROOT_DIR)}, self))



        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addMenu('Copy')
        self.editMenu.addMenu('Copy')
        self.editMenu.addMenu('Cut')
        self.editMenu.addMenu('Paste')

        self.viewMenu = self.menuBar().addMenu("&View")

        self.toolMenu = self.menuBar().addMenu("&Tools")

        self.toolMenu.addSeparator()

        self.toolMenu.addAction(rc.ActionProcess("CleanPyc", self))
        self.toolMenu.addAction(rc.ActionProcess("ReConfig", self))
        self.windowMenu = self.menuBar().addMenu("&Window")

    def on_exit_action_triggered(self):
        TimeLog("Log out")
        QApplication.instance().quit()

    @pyqtSlot(bool)
    def show_hide_subMenuBar(self, param):
        self.setVisible(param)

    def resizeEvent(self, event):
        sizeW, sizeH = get_layout_dimention(self)
        self.setSetting.emit('width', str(sizeW), self.objectName())
        self.setSetting.emit('height', str(sizeH), self.objectName())


def main():
    app = QApplication(sys.argv)
    subMenu = SubMenuBar()
    subMenu.show()
    app.exec_()


if __name__=='__main__':
    main()