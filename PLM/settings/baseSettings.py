# -*- coding: utf-8 -*-
"""

Script Name: 
Author: Do Trinh/Jimmy - 3D artist.

Description:


"""
# -------------------------------------------------------------------------------------------------------------
""" Import """
from PLM.types import DamgProperty


class ObjectGlb(object):


    key                                 = 'GlobalSettings'
    Type                                = 'DAMG GlobalSettings Setting'
    _name                               = 'DAMG GlobalSettings Setting'
    _copyright                          = 'Copyright (C) DAMGTEAM.'

    _cfgable                            = False
    _cfgAll                             = False

    def __init__(self):
        object.__init__(self)

        self.__dict__.update()

    @DamgProperty
    def name(self):
        return self._name

    @DamgProperty
    def copyright(self):
        return self._copyright

    @DamgProperty
    def cfgable(self):
        return self._cfgable

    @DamgProperty
    def cfgAll(self):
        return self._cfgAll

    # @cfgAll.setter
    # def cfgAll(self, val):
    #     self._cfgAll                    = val
    #
    # @cfgable.setter
    # def cfgable(self, val):
    #     self._cfgable                   = val


# -------------------------------------------------------------------------------------------------------------
""" Config global """


class ReportGlb(ObjectGlb):

    _printCfgInfo                       = True
    _printPthInfo                       = False
    _printPythonInfo                    = False
    _printAppInfo                       = False
    _printDirInfo                       = False
    _printAvatarInfo                    = False
    _printLogoInfo                      = False
    _printImgInfo                       = False
    _printIconInfo                      = False
    _printServerInfo                    = False
    _printEnvInfo                       = False
    _printUrlInfo                       = False
    _printTypeInfo                      = False
    _printFmtInfo                       = False
    _printPlmInfo                       = False
    _printPcInfo                        = False
    _printSettingInfo                   = False
    _printSignalReceive                 = False
    _printFontInfo                      = False


    def __init__(self):
        super(ReportGlb, self).__init__()



    @DamgProperty
    def printCfgInfo(self):
        return self._printCfgInfo

    @DamgProperty
    def printPthInfo(self):
        return self._printPthInfo

    @DamgProperty
    def printPythonInfo(self):
        return self._printPythonInfo

    @DamgProperty
    def printAppInfo(self):
        return self._printAppInfo

    @DamgProperty
    def printDirInfo(self):
        return self._printDirInfo

    @DamgProperty
    def printAvatarInfo(self):
        return self._printAvatarInfo

    @DamgProperty
    def printLogoInfo(self):
        return self._printLogoInfo

    @DamgProperty
    def printImgInfo(self):
        return self._printImgInfo

    @DamgProperty
    def saveImgInfo(self):
        return self._saveImgInfo

    @DamgProperty
    def printIconInfo(self):
        return self._printIconInfo

    @DamgProperty
    def printEnvInfo(self):
        return self._printEnvInfo

    @DamgProperty
    def saveEnvInfo(self):
        return self._saveEnvInfo

    @DamgProperty
    def printServerInfo(self):
        return self._printServerInfo

    @DamgProperty
    def printUrlInfo(self):
        return self._printUrlInfo

    @DamgProperty
    def printTypeInfo(self):
        return self._printTypeInfo

    @DamgProperty
    def printFmtInfo(self):
        return self._printFmtInfo

    @DamgProperty
    def saveFmtInfo(self):
        return self._saveFmtInfo

    @DamgProperty
    def printPlmInfo(self):
        return self._printPlmInfo

    @DamgProperty
    def printPcInfo(self):
        return self._printPcInfo

    @DamgProperty
    def printSettingInfo(self):
        return self._printSettingInfo

    @DamgProperty
    def printSignalReceive(self):
        return self._printSignalReceive

    @DamgProperty
    def printFontInfo(self):
        return self._printFontInfo

    # @printFontInfo.setter
    # def printFontInfo(self, val):
    #     self._printFontInfo             = val
    #
    # @printSignalReceive.setter
    # def printSignalReceive(self, val):
    #     self._printSignalReceive        = val
    #
    # @printSettingInfo.setter
    # def printSettingInfo(self, val):
    #     self._printSettingInfo          = val
    #
    # @printPcInfo.setter
    # def printPcInfo(self, val):
    #     self._printPcInfo               = val
    #
    # @printPlmInfo.setter
    # def printPlmInfo(self, val):
    #     self._printPlmInfo              = val
    #
    # @saveFmtInfo.setter
    # def saveFmtInfo(self, val):
    #     self._saveFmtInfo               = val
    #
    # @printFmtInfo.setter
    # def printFmtInfo(self, val):
    #     self._printFmtInfo              = val
    #
    # @printTypeInfo.setter
    # def printTypeInfo(self, val):
    #     self._printTypeInfo             = val
    #
    # @printUrlInfo.setter
    # def printUrlInfo(self, val):
    #     self._printUrlInfo              = val
    #
    # @printServerInfo.setter
    # def printServerInfo(self, val):
    #     self._printServerInfo           = val
    #
    # @saveEnvInfo.setter
    # def saveEnvInfo(self, val):
    #     self._saveEnvInfo               = val
    #
    # @printEnvInfo.setter
    # def printEnvInfo(self, val):
    #     self._printEnvInfo              = val
    #
    # @printIconInfo.setter
    # def printIconInfo(self, val):
    #     self._printIconInfo             = val
    #
    # @saveImgInfo.setter
    # def saveImgInfo(self, val):
    #     self._saveImgInfo               = val
    #
    # @printImgInfo.setter
    # def printImgInfo(self, val):
    #     self._printImgInfo              = val
    #
    # @printLogoInfo.setter
    # def printLogoInfo(self, val):
    #     self._printLogoInfo             = val
    #
    # @printAvatarInfo.setter
    # def printAvatarInfo(self, val):
    #     self._printAvatarInfo           = val
    #
    # @printDirInfo.setter
    # def printDirInfo(self, val):
    #     self._printDirInfo              = val
    #
    # @printAppInfo.setter
    # def printAppInfo(self, val):
    #     self.printAppInfo               = val
    #
    # @printPythonInfo.setter
    # def printPythonInfo(self, val):
    #     self._printPythonInfo           = val
    #
    # @printPthInfo.setter
    # def printPthInfo(self, val):
    #     self._printPthInfo              = val
    #
    # @printCfgInfo.setter
    # def printCfgInfo(self, val):
    #     self._printCfgInfo              = val



class RecordGlb(ReportGlb):

    _saveFontInfo                       = True
    _saveCfgInfo                        = True
    _savePthInfo                        = True
    _savePythonInfo                     = True
    _saveAppInfo                        = True
    _saveDirInfo                        = True
    _saveAvatarInfo                     = True
    _saveLogoInfo                       = True
    _saveImgInfo                        = True
    _saveIconInfo                       = True
    _saveServerInfo                     = True
    _saveEnvInfo                        = True
    _saveUrlInfo                        = True
    _saveTypeInfo                       = True
    _saveFmtInfo                        = True
    _savePlmInfo                        = True
    _savePcInfo                         = True
    _saveSettingInfo                    = True

    def __init__(self):
        super(RecordGlb, self).__init__()

        self.__dict__.update()

    @DamgProperty
    def saveServerInfo(self):
        return self._saveServerInfo

    @DamgProperty
    def saveCfgInfo(self):
        return self._saveCfgInfo

    @DamgProperty
    def savePthInfo(self):
        return self._savePthInfo

    @DamgProperty
    def savePythonInfo(self):
        return self._savePythonInfo

    @DamgProperty
    def saveAppInfo(self):
        return self._saveAppInfo

    @DamgProperty
    def saveDirInfo(self):
        return self._saveDirInfo

    @DamgProperty
    def saveAvatarInfo(self):
        return self._saveAvatarInfo

    @DamgProperty
    def saveLogoInfo(self):
        return self._saveLogoInfo

    @DamgProperty
    def saveUrlInfo(self):
        return self._saveUrlInfo

    @DamgProperty
    def saveTypeInfo(self):
        return self._saveTypeInfo

    @DamgProperty
    def savePlmInfo(self):
        return self._savePlmInfo

    @DamgProperty
    def savePcInfo(self):
        return self._savePcInfo

    @DamgProperty
    def saveIconInfo(self):
        return self._saveIconInfo

    @DamgProperty
    def saveFontInfo(self):
        return self._saveFontInfo

    @DamgProperty
    def saveSettingInfo(self):
        return self._saveSettingInfo

    # @saveFontInfo.setter
    # def saveFontInfo(self, val):
    #     self._saveFontInfo              = val
    #
    # @saveLogoInfo.setter
    # def saveLogoInfo(self, val):
    #     self._saveLogoInfo              = val
    #
    # @saveAvatarInfo.setter
    # def saveAvatarInfo(self, val):
    #     self._saveAvatarInfo            = val
    #
    # @saveDirInfo.setter
    # def saveDirInfo(self, val):
    #     self._saveDirInfo               = val
    #
    # @saveAppInfo.setter
    # def saveAppInfo(self, val):
    #     self._saveAppInfo               = val
    #
    # @saveIconInfo.setter
    # def saveIconInfo(self, val):
    #     self._saveIconInfo              = val
    #
    # @savePcInfo.setter
    # def savePcInfo(self, val):
    #     self._savePcInfo                = val
    #
    # @savePlmInfo.setter
    # def savePlmInfo(self, val):
    #     self._savePlmInfo               = val
    #
    # @saveTypeInfo.setter
    # def saveTypeInfo(self, val):
    #     self._saveTypeInfo              = val
    #
    # @saveUrlInfo.setter
    # def saveUrlInfo(self, val):
    #     self._saveUrlInfo               = val
    #
    # @saveServerInfo.setter
    # def saveServerInfo(self, val):
    #     self._saveServerInfo            = val
    #
    # @savePythonInfo.setter
    # def savePythonInfo(self, val):
    #     self._savePythonInfo            = val
    #
    # @savePthInfo.setter
    # def savePthInfo(self, val):
    #     self._savePthInfo               = val
    #
    # @saveCfgInfo.setter
    # def saveCfgInfo(self, val):
    #     self._saveCfgInfo               = val


# -------------------------------------------------------------------------------------------------------------
""" Mode global """


class ModesGlb(RecordGlb):

    _qtBinding                          = 'PyQt5'
    _qtVersion                          = '5.14.1'
    _formatSaving                       = 'json'

    loading_options                     = ['loading', 'progress']
    binding_options                     = ['PyQt5', 'PySide2']
    saving_options                      = ['json', 'yaml']

    def __init__(self):
        super(ModesGlb, self).__init__()

        self.__dict__.update()

    @DamgProperty
    def qtBinding(self):
        return self._qtBinding

    @DamgProperty
    def formatSaving(self):
        return self._formatSaving

    @DamgProperty
    def qtVersion(self):
        return self._qtVersion

    # @qtVersion.setter
    # def qtVersion(self, val):
    #     self._qtVersion                 = val
    #
    # @formatSaving.setter
    # def formatSaving(self, val):
    #     if val in self.saving_options:
    #         self._formatSaving          = val
    #
    # @qtBinding.setter
    # def qtBinding(self, val):
    #     if val in self.qtBinding:
    #         self._qtBinding             = val


# -------------------------------------------------------------------------------------------------------------
""" Error global """


class ErrorsGlb(ModesGlb):

    _allowAllErrors                     = True
    _actionRegisterError                = True

    def __init__(self):
        super(ErrorsGlb, self).__init__()

        self.__dict__.update()

    @property
    def allowAllErrors(self):
        return self._allowAllErrors

    @property
    def actionRegisterError(self):
        return self._actionRegisterError

    @actionRegisterError.setter
    def actionRegisterError(self, val):
        self._actionRegisterError       = val

    @allowAllErrors.setter
    def allowAllErrors(self, val):
        self._allowAllErrors            = val


# -------------------------------------------------------------------------------------------------------------
""" Signal global """


class SignalGlb(ErrorsGlb):

    _emittable                          = False
    _autoChangeEmittable                = True
    _trackRecieveSignal                 = False
    _trackBlockSignal                   = False
    _trackCommand                       = False
    _trackRegistLayout                  = False

    def __init__(self):
        super(SignalGlb, self).__init__()

        self.__dict__.update()

    @DamgProperty
    def emittable(self):
        return self._emittable

    @DamgProperty
    def autoChangeEmittable(self):
        return self._autoChangeEmittable

    @DamgProperty
    def trackRecieveSignal(self):
        return self._trackRecieveSignal

    @DamgProperty
    def trackBlockSignal(self):
        return self._trackBlockSignal

    @DamgProperty
    def trackCommand(self):
        return self._trackCommand

    @DamgProperty
    def trackRegistLayout(self):
        return self._trackRegistLayout

    # @trackRegistLayout.setter
    # def trackRegistLayout(self, val):
    #     self._trackRegistLayout         = val
    #
    # @trackCommand.setter
    # def trackCommand(self, val):
    #     self._trackCommand              = val
    #
    # @trackBlockSignal.setter
    # def trackBlockSignal(self, val):
    #     self._trackBlockSignal          = val
    #
    # @trackRecieveSignal.setter
    # def trackRecieveSignal(self, val):
    #     self._trackRecieveSignal        = val
    #
    # @autoChangeEmittable.setter
    # def autoChangeEmittable(self, val):
    #     self._autoChangeEmittable       = val
    #
    # @emittable.setter
    # def emittable(self, val):
    #     self._emittable                 = val


# -------------------------------------------------------------------------------------------------------------
""" Setting global """


class GlobalBase(SignalGlb):

    def __init__(self):
        super(GlobalBase, self).__init__()

        self.__dict__.update()

    def setCfgAll(self, val):
        self._cfgAll                    = val

    def setCfgAble(self, val):
        self._cfgable                   = val


# -------------------------------------------------------------------------------------------------------------
# Created by Trinh Do on 5/6/2020 - 3:13 AM
# © 2017 - 2020 DAMGteam. All rights reserved