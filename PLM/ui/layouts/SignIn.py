#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Script Name: SignIn.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

    Sign In layout.

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import sys, requests
from functools                  import partial

# PLM
from PLM import __localServerAutho__, APP_LOG
from PLM.configs import configPropText
p = configPropText()
from PLM.cores import sqlUtils
from pyPLM.loggers import DamgLogger
from pyPLM.Widgets import (Widget, GridLayout, LineEdit, CheckBox, Button, user_pass_label, Label, MessageBox, GroupGrid, )
from pyPLM.Gui import AppIcon
from pyPLM.models import DamgSignals
from PLM.utils import bool2str


# -------------------------------------------------------------------------------------------------------------
""" Sign In Layout """

class SignIn(Widget):

    key = 'SignIn'
    _login = False

    def __init__(self, parent=None):
        super(SignIn, self).__init__(parent)

        self.setWindowIcon(AppIcon(32, "SignIn"))
        self.setFixedSize(400, 300)
        self.setWindowTitle('Sign In')
        self.logger             = DamgLogger(self, filepth=APP_LOG)
        self.signals            = DamgSignals(self)
        self.layout             = GridLayout()
        self.db                 = sqlUtils()
        self.buildUI()
        self.setLayout(self.layout)

    def buildUI(self):

        loginGrp                = GroupGrid('Sign in')
        loginGrid               = loginGrp.layout

        self.userTF             = LineEdit()
        self.pwTF               = LineEdit({'fn': 'password'})
        self.userCB             = CheckBox('Remember me?')

        forgot_pw_btn           = Button({'txt': 'Forgot your password?', 'cl': partial(self.signals.emit, 'showLayout', 'ForgotPassword', 'show')})
        login_btn               = Button({'txt': 'Log in', 'cl': self.signInClicked})
        cancel_btn              = Button({'txt': 'Cancel', 'cl': sys.exit})

        signupGrp               = GroupGrid('Sign up')
        signupGrid              = signupGrp.layout
        signupBtn               = Button({'txt':'Sign up', 'cl': partial(self.signals.emit, 'showLayout', 'SignUp', 'show')})

        usernameLabel, passwordLabel = user_pass_label()

        loginGrid.addWidget(usernameLabel, 0, 0, 1, 2)
        loginGrid.addWidget(passwordLabel, 1, 0, 1, 2)
        loginGrid.addWidget(self.userTF, 0, 2, 1, 4)
        loginGrid.addWidget(self.pwTF, 1, 2, 1, 4)
        loginGrid.addWidget(self.userCB, 2, 1, 1, 2)
        loginGrid.addWidget(login_btn, 2, 3, 1, 3)
        loginGrid.addWidget(forgot_pw_btn, 3, 0, 1, 3)
        loginGrid.addWidget(cancel_btn, 3, 3, 1, 3)

        signupGrid.addWidget(Label({'txt': p['SIGNUP']}), 0, 0, 1, 6)
        signupGrid.addWidget(signupBtn, 1, 0, 1, 6)

        self.layout.addWidget(loginGrp, 0, 0, 1, 1)
        self.layout.addWidget(signupGrp, 1, 0, 1, 1)

    def forgetPwClicked(self):
        if __name__ == '__main__':
            from PLM import ForgotPassword
            self.forgotPW = ForgotPassword()
            self.forgotPW.show()
        else:
            self.signals.showLayout('ForgotPassword', 'show')

    def signInClicked(self):
        self.logger.info('login clicked')
        username = str(self.userTF.text())
        pass_word = str(self.pwTF.text())

        if username == "" or username is None:
            MessageBox(self, 'Login Failed', 'critical', p['USER_BLANK'])
            return
        elif pass_word == "" or pass_word is None:
            MessageBox(self, 'Login Failed', 'critical', p['PW_BLANK'])
            return

        password = str(pass_word)
        self.logger.info('send request to server to check account')
        r = requests.post(__localServerAutho__, verify=False, data={'user': username, 'pwd': password})

        if r.status_code == 200:
            for i in r.headers['set-cookie'].split(";"):
                if 'connect.sid=' in i:
                    cookie = i.split('connect.sid=')[-1]
                    break
                else:
                    cookie="No value"
                    continue

            token = r.json()['token']
            check = bool2str(self.userCB.checkState())

            self.db.remove_data("curUser")
            self.db.update_user_login(username, token, cookie, bool2str(check))
            self.signals.loginChangedSig.emit(True)
        else:
            self.db.remove_data("curUser")
            MessageBox(self, 'Login Failed', 'critical', p['PW_WRONG'])
            return

    def loginChanged(self, login):
        self._login = login

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, newVal):
        self._login = newVal