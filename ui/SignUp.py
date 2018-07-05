#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Script Name: {}.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import os, sys, json

# PyQt5
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLineEdit, QLabel, QPushButton, QMessageBox, QGroupBox,
                             QCheckBox, QFileDialog, QComboBox, QDialog)

# -------------------------------------------------------------------------------------------------------------
""" Plt tools """
from appData import WAIT_LAYOUT_COMPLETE, PW_UNMATCH, TIT_BLANK, USER_CHECK_REQUIRED, QUESTIONS

from ui import uirc as rc
from utilities import utils as func
from core.Settings import Settings
from appData.Loggers import SetLogger
logger = SetLogger()

# -------------------------------------------------------------------------------------------------------------
""" Sign up ui """

class SignUp(QDialog):

    showSignup = pyqtSignal(bool)
    showPlt = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(SignUp, self).__init__(parent)

        self.setWindowTitle("Sign Up")
        self.setWindowIcon(rc.IconPth(32, "SignUp"))
        self.setFixedSize(450, 900)
        # from core.Settings import Settings
        self.settings = Settings(self)

        self.layout = QGridLayout()
        self.buildUI()
        self.setLayout(self.layout)

    def buildUI(self):
        self.avatar_section()
        self.account_section()
        self.profile_section()
        self.location_section()
        self.security_section()
        self.buttons_section()

        self.layout.addWidget(rc.Label("ALL FIELD ARE REQUIRED!!!"), 0, 0, 1, 6)
        self.layout.addWidget(self.avaSection, 1, 0, 1, 2)
        self.layout.addWidget(self.accSection, 1, 2, 1, 4)
        self.layout.addWidget(self.prfSection, 2, 0, 1, 6)
        self.layout.addWidget(self.conSection, 3, 0, 1, 6)
        self.layout.addWidget(self.serSection, 4, 0, 1, 6)
        self.layout.addWidget(self.btnSection, 5, 0, 1, 6)

    def avatar_section(self):
        self.avaSection = QGroupBox("Avatar")
        avatar_grid = QGridLayout()
        self.avaSection.setLayout(avatar_grid)

        defaultImg = QPixmap.fromImage(QImage(func.getAvatar('default')))
        self.userAvatar = QLabel()
        self.userAvatar.setPixmap(defaultImg)
        self.userAvatar.setScaledContents(True)
        self.userAvatar.setFixedSize(100, 100)

        set_avatarBtn = QPushButton("Set Avatar")
        set_avatarBtn.clicked.connect(self.on_set_avatar_btn_clicked)

        avatar_grid.addWidget(self.userAvatar, 0, 0, 2, 2)
        avatar_grid.addWidget(set_avatarBtn, 2, 0, 1, 2)

    def account_section(self):
        self.accSection = QGroupBox("Account")
        account_grid = QGridLayout()
        self.accSection.setLayout(account_grid)

        account_grid.addWidget(rc.Label('User Name'), 0, 0, 1, 2)
        account_grid.addWidget(rc.Label('Password'), 1, 0, 1, 2)
        account_grid.addWidget(rc.Label('Confirm Password'), 2, 0, 1, 2)

        self.userField = QLineEdit()
        self.pwField = QLineEdit()
        self.cfpwField = QLineEdit()

        self.pwField.setEchoMode(QLineEdit.Password)
        self.cfpwField.setEchoMode(QLineEdit.Password)

        account_grid.addWidget(self.userField, 0, 3, 1, 4)
        account_grid.addWidget(self.pwField, 1, 3, 1, 4)
        account_grid.addWidget(self.cfpwField, 2, 3, 1, 4)

    def profile_section(self):
        self.prfSection = QGroupBox("Profile")
        profile_grid = QGridLayout()
        self.prfSection.setLayout(profile_grid)

        profile_grid.addWidget(rc.Label('First Name'), 0, 0, 1, 2)
        profile_grid.addWidget(rc.Label('Last Name'), 1, 0, 1, 2)
        profile_grid.addWidget(rc.Label('Your Title'), 2, 0, 1, 2)
        profile_grid.addWidget(rc.Label('Email'), 3, 0, 1, 2)
        profile_grid.addWidget(rc.Label('Phone Number'), 4, 0, 1, 2)

        self.titleField = QLineEdit()
        self.firstnameField = QLineEdit()
        self.lastnameField = QLineEdit()
        self.emailField = QLineEdit()
        self.phoneField = QLineEdit()

        profile_grid.addWidget(self.firstnameField, 0, 2, 1, 4)
        profile_grid.addWidget(self.lastnameField, 1, 2, 1, 4)
        profile_grid.addWidget(self.titleField, 2, 2, 1, 4)
        profile_grid.addWidget(self.emailField, 3, 2, 1, 4)
        profile_grid.addWidget(self.phoneField, 4, 2, 1, 4)

    def location_section(self):
        self.conSection = QGroupBox("Location")
        conGrid = QGridLayout()
        self.conSection.setLayout(conGrid)

        conGrid.addWidget(rc.Label("Address Line 1"), 0, 0, 1, 2)
        conGrid.addWidget(rc.Label("Address Line 2"), 1, 0, 1, 2)
        conGrid.addWidget(rc.Label("Postal"), 2, 0, 1, 2)
        conGrid.addWidget(rc.Label("City"), 3, 0, 1, 2)
        conGrid.addWidget(rc.Label("Country"), 4, 0, 1, 2)

        self.addressLine1 = QLineEdit()
        self.addressLine2 = QLineEdit()
        self.postalCode = QLineEdit()
        self.city = QLineEdit()
        self.country = QLineEdit()

        conGrid.addWidget(self.addressLine1, 0, 2, 1, 4)
        conGrid.addWidget(self.addressLine2, 1, 2, 1, 4)
        conGrid.addWidget(self.city, 2, 2, 1, 4)
        conGrid.addWidget(self.postalCode, 3, 2, 1, 4)
        conGrid.addWidget(self.country, 4, 2, 1, 4)

    def security_section(self):

        self.serSection = QGroupBox("Security Question")
        questions_grid = QGridLayout()
        self.serSection.setLayout(questions_grid)

        self.ques1 = QComboBox()
        self.answ2 = QLineEdit()
        self.ques2 = QComboBox()
        self.answ1 = QLineEdit()

        questions = QUESTIONS

        for i in questions:
            self.ques1.addItem(str(i[0]))
            if i != 0:
                self.ques2.addItem(str(i[0]))

        questions_grid.addWidget(rc.Label('Question 1'), 0, 0, 1, 3)
        questions_grid.addWidget(rc.Label('Answer 1'), 1, 0, 1, 3)
        questions_grid.addWidget(rc.Label('Question 2'), 2, 0, 1, 3)
        questions_grid.addWidget(rc.Label('Answer 2'), 3, 0, 1, 3)

        questions_grid.addWidget(self.ques1, 0, 3, 1, 6)
        questions_grid.addWidget(self.answ1, 1, 3, 1, 6)
        questions_grid.addWidget(self.ques2, 2, 3, 1, 6)
        questions_grid.addWidget(self.answ2, 3, 3, 1, 6)

    def buttons_section(self):
        self.btnSection = QGroupBox()
        btn_grid = QGridLayout()
        self.btnSection.setLayout(btn_grid)

        self.user_agree_checkBox = QCheckBox(USER_CHECK_REQUIRED)
        btn_grid.addWidget(self.user_agree_checkBox, 0, 0, 1, 6)

        okBtn = QPushButton('Create Account')
        okBtn.clicked.connect(self.on_create_btn_clicked)
        btn_grid.addWidget(okBtn, 1, 0, 1, 2)

        cancelBtn = QPushButton('Cancel')
        cancelBtn.clicked.connect(self.on_cancel_btn_clicked)
        btn_grid.addWidget(cancelBtn, 1, 2, 1, 2)

        quitBtn = QPushButton('Quit')
        quitBtn.clicked.connect(QApplication.quit)
        btn_grid.addWidget(quitBtn, 1,4,1,2)

    def on_set_avatar_btn_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        self.rawAvatarPth, _ = QFileDialog.getOpenFileName(self, "Your Avatar", os.path.join('imgs', 'avatar'),
                                                           "All Files (*);;Img Files (*.jpg)", options=options)

        if self.rawAvatarPth:
            self.userAvatar.setPixmap(QPixmap.fromImage(QImage(self.rawAvatarPth)))
            self.userAvatar.update()

    def on_create_btn_clicked(self):
        if self.check_all_conditions():
            data = self.generate_user_data()
            # usql.create_new_user_data(data)
            QMessageBox.information(self, "Failed", WAIT_LAYOUT_COMPLETE, QMessageBox.Ok)
            # self.showPlt.emit(True)
            return

    def on_cancel_btn_clicked(self):
        self.close()
        self.showSignup.emit(True)

    def collect_input(self):
        username = str(self.userField.text())
        password = str(self.pwField.text())
        confirm = str(self.cfpwField.text())
        firstname = str(self.firstnameField.text())
        lastname = str(self.lastnameField.text())
        email = str(self.emailField.text())
        phone = str(self.phoneField.text())
        address1 = str(self.addressLine1.text())
        address2 = str(self.addressLine2.text())
        postal = str(self.postalCode.text())
        city = str(self.city.text())
        country = str(self.country.text())
        answer1 = str(self.answ1.text())
        answer2 = str(self.answ2.text())
        return [username, password, confirm, firstname, lastname, email, phone, address1, address2, postal, city,
                country, answer1, answer2]

    def check_all_conditions(self):
        if self.check_all_field_blank():
            if self.check_user_agreement():
                if self.check_pw_matching():
                    return True
        else:
            return False

    def check_all_field_blank(self):
        regInput = self.collect_input()
        secName = ["Username", "Password", "Confirm Password", "Firstname", "Lastname", "Email", "Phone",
                   "Address line 1", "Address line 2", "Postal", "City", "Country", "Answer 1", "Answer 2"]
        for section in regInput:
            if func.check_blank(section):
                return True
            else:
                QMessageBox.information(self, "Fail", secName[regInput.index(section)] + "Blank", QMessageBox.Ok)
                break

    def check_user_agreement(self):
        return self.user_agree_checkBox.checkState()

    def generate_user_data(self):
        regInput = self.collect_input()
        question1 = str(self.ques1.currentText())
        question2 = str(self.ques2.currentText())
        title = str(self.titleField.text()) or "Guess"

        token = func.get_token()
        timelog = func.get_time()
        sysInfo = func.get_local_pc()
        productID = sysInfo['Product ID']
        ip, cityIP, countryIP = func.get_pc_location()
        unix = func.get_unix()
        datelog = func.get_date()
        pcOS = sysInfo['os']
        pcUser = sysInfo['pcUser']
        pcPython = sysInfo['python']

        if not os.path.exists(self.rawAvatarPth):
            avatar = func.getAvatar('default')
        else:
            avatar = self.rawAvatarPth

        data = [regInput[0], regInput[1], regInput[3], regInput[4], title, regInput[5], regInput[6], regInput[7],
                regInput[8], regInput[9], regInput[10], regInput[11], token, timelog, productID, ip, cityIP, countryIP, unix, question1, regInput[12], question2,
                regInput[13], datelog, pcOS, pcUser, pcPython, avatar]
        return data

    def check_pw_matching(self):
        password = str(self.pwField.text())
        confirm = str(self.cfpwField.text())
        check_pass = func.check_match(password, confirm)
        if not check_pass:
            QMessageBox.information(self, "Warning", PW_UNMATCH, QMessageBox.Retry)
            return False
        return True

    def closeEvent(self, event):
        self.on_cancel_btn_clicked()

def main():
    app = QApplication(sys.argv)
    layout = SignUp()
    layout.show()
    app.exec_()

if __name__ == '__main__':
    main()