# -*- coding: utf-8 -*-
"""

Script Name: Label.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals
""" Import """

# PyQt5
from PyQt5.QtWidgets                        import QLabel
from PyQt5.QtGui                            import QFont, QPixmap, QImage

# PLM
from appData                                import SETTING_FILEPTH, ST_FORMAT, __copyright__, PRS
from cores.Loggers                          import Loggers
from cores.Settings                         import Settings
from cores.SignalManager                    import SignalManager
from ui.uikits.Pixmap                       import Pixmap
from ui.uikits.Image                        import Image
from ui.uikits.uiUtils                      import check_preset


class Label(QLabel):

    Type                                    = 'DAMGUI'
    key                                     = 'Label'
    _name                                   = 'DAMG Label'
    _copyright                              = __copyright__
    _data                                   = dict()

    def __init__(self, preset={}, parent=None):
        super(Label, self).__init__(parent)

        self.parent                         = parent
        self.signals                        = SignalManager(self)
        self.logger                         = Loggers(self.__class__.__name__)
        self.settings                       = Settings(SETTING_FILEPTH['app'], ST_FORMAT['ini'], self)
        self.preset                         = preset

        if check_preset(self.preset):
            self.buildUI()

    def buildUI(self):
        for key, value in self.preset.items():
            if key == 'txt':
                self.setText(value)
            elif key == 'fnt':
                self.setFont(QFont(value))
            elif key == 'alg':
                self.setAlignment(PRS[value])
            elif key == 'wmin':
                self.setMinimumWidth(value)
            elif key == 'hmin':
                self.setMinimumHeight(value)
            elif key == 'smin':
                self.setMinimumSize(value[0], value[1])
            elif key == 'sizePolicy':
                self.setSizePolicy(PRS[value[0]], PRS[value[1]])
            elif key == 'pxm':
                self.setPixmap(Pixmap.fromImage(Image(value)))
            elif key == 'scc':
                self.setScaledContents(value)
            elif key == 'sfs':
                self.setFixedSize(value[0], value[1])
            elif key == 'setBuddy':
                self.setBuddy(value)
            elif key == 'link':
                self.setOpenExternalLinks(value)
            elif key == 'minimumSize':
                self.setMinimumSize(value[0], value[1])
            else:
                print("PRESETKEYERROR: No such key registed in preset: {0}: {1}".format(key, value))

    def setValue(self, key, value):
        return self.settings.initSetValue(key, value, self.key)

    def getValue(self, key):
        return self.settings.initValue(key, self.key)

    def showEvent(self, event):
        sizeX = self.getValue('width')
        sizeY = self.getValue('height')

        if not sizeX is None and not sizeY is None:
            self.resize(int(sizeX), int(sizeY))

        posX = self.getValue('posX')
        posY = self.getValue('posY')

        if not posX is None and not posX is None:
            self.move(posX, posY)

        if __name__ == '__main__':
            self.show()
        else:
            self.signals.showLayout.emit(self.key, 'show')
            event.ignore()

    def moveEvent(self, event):
        self.setValue('posX', self.x())
        self.setValue('posY', self.y())

    def resizeEvent(self, event):
        self.setValue('width', self.frameGeometry().width())
        self.setValue('height', self.frameGeometry().height())

    def sizeHint(self):
        size = super(Label, self).sizeHint()
        size.setHeight(size.height())
        size.setWidth(max(size.width(), size.height()))
        return size

    def closeEvent(self, event):
        if __name__=='__main__':
            self.close()
        else:
            self.signals.showLayout.emit(self.key, 'hide')
            event.ignore()

    def hideEvent(self, event):
        if __name__=='__main__':
            self.hide()
        else:
            self.signals.showLayout.emit(self.key, 'hide')
            event.ignore()

usernameLabel = Label({'txt': 'Username'})
passwordLabel = Label({'txt': 'Password'})

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 27/10/2019 - 6:40 PM
# © 2017 - 2018 DAMGteam. All rights reserved