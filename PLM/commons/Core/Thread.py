# -*- coding: utf-8 -*-
"""

Script Name: Thread.py
Author: Do Trinh/Jimmy - 3D artist.

Description:
    

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# PyQt5
from PyQt5.QtCore                       import QThread

# PLM
from PLM                                import __copyright__


class Thread(QThread):

    Type                                = 'DAMGTHREAD'
    key                                 = 'BaseThread'
    _name                               = 'DAMG Thread'
    _copyright                          = __copyright__()

    def __init__(self, *args, **kwargs):
        QThread.__init__(self)

        self.args = args
        self.kwargs = kwargs

    @property
    def copyright(self):
        return self._copyright

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name                          = val


# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/20/2020 - 6:23 AM
# © 2017 - 2019 DAMGteam. All rights reserved