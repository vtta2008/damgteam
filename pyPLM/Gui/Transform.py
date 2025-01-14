# -*- coding: utf-8 -*-
"""

Script Name: Transform.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

from PySide2.QtGui                          import QTransform


class Transform(QTransform):

    Type                        = 'DAMGTRANSFORM'
    key                         = 'Transform'
    _name                       = 'DAMG Transform'

    def __init__(self, *__args):
        super(Transform, self).__init__(*__args)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name              = val

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/12/2019 - 1:48 AM
# © 2017 - 2018 DAMGteam. All rights reserved