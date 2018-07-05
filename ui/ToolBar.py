#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Script Name: ToolBar.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import sys

# PyQt5
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QApplication

# Plt
from appData import CONFIG_TDS, CONFIG_VFX, CONFIG_ART, APPINFO
from ui import uirc as rc
from utilities import utils as func
from core.Settings import Settings

from appData.Loggers import SetLogger
logger = SetLogger()

# -------------------------------------------------------------------------------------------------------------
""" ToolBar """

class ToolBar(QMainWindow):

    def __init__(self, parent=None):

        super(ToolBar, self).__init__(parent)

        # from core.Settings import Settings
        self.settings = Settings(self)
        self.appInfo = APPINFO
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.tdToolBar = self.make_toolBar("TD", CONFIG_TDS)
        self.compToolBar = self.make_toolBar("VFX", CONFIG_VFX)
        self.artToolBar = self.make_toolBar("ART", CONFIG_ART)

        self.showTDToolBar = func.str2bool(self.settings.value("showTDToolbar", True))
        self.showCompToolBar = func.str2bool(self.settings.value("showCompToolbar", True))
        self.showArtToolBar = func.str2bool(self.settings.value("showArtToolbar", True))

        self.tdToolBar.setVisible(self.showTDToolBar)
        self.compToolBar.setVisible(self.showCompToolBar)
        self.artToolBar.setVisible(self.showArtToolBar)

    def make_toolBar(self, name="", apps=[]):
        toolBar = self.addToolBar(name)
        for key in apps:
            if key in self.appInfo:
                toolBar.addAction(rc.ActionProcess(key, self))
        return toolBar

    def show_td(self, param):
        self.settings.setValue("tbTD", func.bool2str(param))
        self.tdToolBar.setVisible(func.str2bool(param))

    def show_comp(self, param):
        self.settings.setValue("tbComp", func.bool2str(param))
        self.compToolBar.setVisible(func.str2bool(param))

    def show_art(self, param):
        self.settings.setValue("tbArt", func.bool2str(param))
        self.artToolBar.setVisible(func.str2bool(param))

def main():
    app = QApplication(sys.argv)
    toolBar = ToolBar()
    toolBar.show()
    app.exec_()

if __name__=='__main__':
    main()