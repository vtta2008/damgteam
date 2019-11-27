# -*- coding: utf-8 -*-
"""

Script Name: GroupBox.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __buildtins__ import __copyright__, settings, signals

""" Import """

# PyQt5
from PyQt5.QtWidgets                        import QGroupBox

# PLM
from toolkits.Widgets                       import AutoPreset3, AutoPreset2, AutoPreset1, GridLayout, HBoxLayout, Label, VBoxLayout
from appData                                import WAIT_LAYOUT_COMPLETE

# -------------------------------------------------------------------------------------------------------------
""" Groupbox presets """

class GroupBoxBase(QGroupBox):

    Type                                    = 'DAMGGROUPBOX'
    key                                     = 'GroupBoxBase'
    _name                                   = 'DAMG Group Box Base'
    _copyright                              = __copyright__()

    def __init__(self, parent=None):
        QGroupBox.__init__(self)

        self.parent                         = parent
        self.settings                       = settings
        self.signals                        = signals
        self.settings.changeParent(self)
        self.signals.changeParent(self)

    def sizeHint(self):
        size = super(GroupBoxBase, self).sizeHint()
        size.setHeight(size.height())
        size.setWidth(max(size.width(), size.height()))
        return size

    def setValue(self, key, value):
        return self.settings.initSetValue(key, value, self.key)

    def getValue(self, key):
        return self.settings.initValue(key, self.key)

    def moveEvent(self, event):
        if self.settings._settingEnable:
            self.setValue('x', self.x())
            self.setValue('y', self.y())

    def resizeEvent(self, event):
        if self.settings._settingEnable:
            self.setValue('w', self.width())
            self.setValue('h', self.height())

    def closeEvent(self, event):
        if __name__=='__main__':
            self.close()
        else:
            self.signals.emit('showLayout', self.key, 'hide')

    def hideEvent(self, event):
        if __name__=='__main__':
            self.hide()
        else:
            if self.settings._settingEnable:
                for key, value in self.values.items():
                    self.setValue(key, value)
            self.signals.emit('showLayout', self.key, 'hide')

    def showEvent(self, event):

        if self.settings._settingEnable:
            w = self.getValue('w')
            h = self.getValue('h')
            x = self.getValue('x')
            y = self.getValue('x')

            vals = [w, h, x, y]

            for i in range(len(vals)):
                if vals[i] is None:
                    key = [k for k in self.values.keys()]
                    value = self.values[key[i]]
                    for index, element in enumerate(vals):
                        if element == vals[i]:
                            vals[index] = value
                    self.setValue(key[i], self.values[key[i]])

            for v in vals:
                if not type(v) in [int]:
                    v = int(v)

            self.resize(vals[0]-1, vals[1]-1)
            self.resize(vals[0], vals[1])
            self.move(vals[2], vals[3])

        if __name__=='__main__':
            self.show()
        else:
            self.signals.emit('showLayout', self.key, 'show')

    @property
    def copyright(self):
        return self._copyright

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name                      = newName

class GroupBox(GroupBoxBase):

    key                                     = 'GroupBox'
    _name                                   = 'DAMG Group Box'

    def __init__(self, title="Section Title", layouts=None, mode=None, parent=None):
        super(GroupBox, self).__init__(parent)

        self._title                         = title
        self.parent                         = parent
        self.layouts                        = layouts
        self.mode                           = mode
        self.setTitle(self._title)

        if not self.mode is None:
            self.buildUI()

    def buildUI(self):
        if self.mode == "IconGrid":
            self.setLayout(AutoPreset1(self.layouts))
        elif self.mode == "BtnGrid":
            self.setLayout(AutoPreset2(self.layouts))
        elif self.mode == "ImageView":
            self.setLayout(AutoPreset3(self.layouts[0]))
        elif self.mode == "setLayout":
            for layout in self.layouts:
                self.setLayout(layout)
        elif self.mode == "qmainLayout":
            self.layout = HBoxLayout({'addWidget': [self.layouts]})
            self.setLayout(self.layout)
        elif self.mode == "autoGrid":
            self.subLayout = self.layouts
            if self.subLayout is None:
                self.layout = GridLayout()
                self.layout.addWidget(Label({'txt': WAIT_LAYOUT_COMPLETE}), 0, 0, 1, 1)
            else:
                self.layout = self.subLayout
            self.setLayout(self.layout)
        elif self.mode == "groupGrid":
            self.layout = GridLayout()
            self.setLayout(self.layout)
        else:
            print("Unrecognise mode: {}".format(self.mode))

    def changeTitle(self, title):
        if not title is None or not title:
            self.setTitle(title)

class GroupGrid(GroupBoxBase):

    key = 'GroupGrid'

    def __init__(self, title="", parent=None):
        super(GroupGrid, self).__init__(parent)

        self._title = title
        self.setTitle(self._title)
        self.layout = GridLayout(self)
        self.setLayout(self.layout)

class GroupVBox(GroupBoxBase):

    key = 'GroupVBox'

    def __init__(self, parent=None):
        super(GroupVBox, self).__init__(parent)

        self.layout = VBoxLayout(self)
        self.setLayout(self.layout)

class GroupHBox(GroupBoxBase):

    key = 'GroupHBox'

    def __init__(self, parent=None):
        super(GroupHBox, self).__init__(parent)

        self.layout = HBoxLayout(self)
        self.setLayout(self.layout)

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 18/07/2018 - 8:32 AM
# © 2017 - 2018 DAMGteam. All rights reserved