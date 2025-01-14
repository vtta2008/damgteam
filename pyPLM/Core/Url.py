# -*- coding: utf-8 -*-
"""

Script Name: Url.py
Author: Do Trinh/Jimmy - 3D artist.

Description:
    

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """


from PySide2.QtCore                 import QUrl


class Url(QUrl):

    Type                                = 'DAMGURL'
    key                                 = 'Timer'
    _name                               = 'DAMG Timer'

    def __init__(self, *__args):
        super(Url, self).__init__(*__args)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name                      = val

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 5/5/2020 - 9:10 PM
# © 2017 - 2019 DAMGteam. All rights reserved