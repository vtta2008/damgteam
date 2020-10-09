# -*- coding: utf-8 -*-
"""

Script Name: StyleSheet.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import platform

# PLM
from bin import settings
from PLM.options import COLOR_BACKGROUND_NORMAL
from bin.damg import DAMG, DAMGDICT
from bin.Core import TextStream, File, QssFile
from PLM.loggers import Loggers


# def set_register(obj, stylesheet=None, update=True):
#     observer = _StyleSheetObserver(obj, stylesheet, update)
#     observer.register()


def _render_stylesheet(stylesheet):
    pass



class StyleSheet(DAMG):

    key                                 = 'StylesSheet'
    _filename                           = None
    _stylesheet                         = None
    filenames                           = DAMGDICT()

    def __init__(self, app=None):
        super(StyleSheet, self).__init__()

        self.logger                     = Loggers()
        self.app                        = app

    def getStyleSheet(self, style):
        if style == 'dark':
            # self.logger.info("Loading darkstyle_rc")
            pass
        else:
            if settings.qtBindingMode == 'PyQt5':
                # self.logger.info("Loading pyqt5_style_rc")
                pass
            elif settings.qtBindingMode == 'PySide2':
                # self.logger.info("Loading pyside2_style_rc")
                pass
            else:
                # self.logger.info("Loading pyqtgraph_style_rc")
                pass

        self._filename                  = QssFile(style)
        self._filename.open(File.ReadOnly | File.Text)
        ts                              = TextStream(self._filename)
        stylesheet                      = ts.readAll()
        self._stylesheet                = self.fixStyleSheet(stylesheet)

        return stylesheet

    def fixStyleSheet(self, style):
        stylesheet                  = style
        if platform.system().lower() == 'darwin':
            mac_fix = '''
            QDockWidget::title
            {
                background-color: {0};
                text-align: center;
                height: 12px;
            }
            '''.format(COLOR_BACKGROUND_NORMAL)
            stylesheet += mac_fix
        return stylesheet

    def removeStyleSheet(self):
        self._filename                  = ''
        self._stylesheet                = ''

    @classmethod
    def progressBar(self):
        qssPth                          = QssFile('progressBar')
        qssPth.open(File.ReadOnly | File.Text)
        ts                              = TextStream(qssPth)
        return ts.readAll()

    @property
    def filename(self):
        return self._filename

    @property
    def stylesheet(self):
        return self._stylesheet

    @filename.setter
    def filename(self, val):
        self._filename                  = val

    @stylesheet.setter
    def stylesheet(self, val):
        self._stylesheet                = val



# -------------------------------------------------------------------------------------------------------------
# Created by panda on 22/06/2018 - 3:51 AM
# © 2017 - 2018 DAMGteam. All rights reserved