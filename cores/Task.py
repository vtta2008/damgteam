# -*- coding: utf-8 -*-
"""

Script Name: Task.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

from bin.data.damg import DAMG, DAMGDICT, DAMGTIMER

from PyQt5.QtCore import QDateTime, QDate, QTime, pyqtSignal

class duetime(DAMGDICT):

    Type = 'DAMGDUETIME'
    key = 'Duetime'
    _name = 'Duetime'

    def __init__(self, hour=0, minute=0, second=0):
        super(duetime, self).__init__(self)

        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)

        if self.hour > 24:
            raise IndexError('Expect hour smaller than 24: {0}'.format(self.hour))

        if self.minute > 60:
            raise IndexError('Expect minute smaller than 60: {0}'.format(self.minute))

        if self.second > 60:
            raise IndexError('Expect second smaller than 60: {0}'.format(self.second))

        self.add('hour', self.hour)
        self.add('minute', self.minute)
        self.add('second', self.second)

class duedate(DAMGDICT):

    Type = 'DAMGDUEDATE'
    key = 'Duedate'
    _name = 'Duedate'

    def __init__(self, day, month, year):
        super(duedate, self).__init__(self)

        self.year = int(year)
        self.month = int(month)
        self.day = int(day)

        if self.month > 12:
            raise IndexError('Expect month smaller than 12: {0}'.format(self.month))

        if self.day > 31:
            raise IndexError('Expect day smaller than 31: {0}'.format(self.day))

        self.add('year', self.year)
        self.add('month', self.month)
        self.add('day', self.day)

class TaskBase(DAMG):

    key = 'Task'
    Type = 'DAMGTASK'
    _name = 'Task Name'
    _status = 'status'
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    countdown = pyqtSignal(str, name='CountDown')

    def __init__(self):
        super(TaskBase, self).__init__(self)

        self.date = QDate()
        self.time = QTime()

        self.timer = DAMGTIMER()
        self.timer.setParent(self)

    def countter_format(self, format='sec'):
        if format in ['sec', 'second']:
            return 1000
        elif format in ['min', 'minute']:
            return 1000*60
        elif format in ['hr', 'hour']:
            return 1000*60*60
        else:
            return 1000

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, val):
        self._status = val

class Task(TaskBase):

    def __init__(self, taskID=None, taskName=None, project=None, duetime={}, duedate={}, details={}):
        super(Task, self).__init__()

        self.id         = taskID
        self.taskName   = taskName
        self.project    = project
        self.details    = details

        self.duetime    = QTime(duetime['hour'], duetime['minute'], duetime['second'])
        self.duedate    = QDate(duedate['year'], duedate['month'], duedate['day'])
        self.endDate    = QDateTime(self.duedate, self.duetime)

        self.update()

        format = self.countter_format()
        self.timer.timeout.connect(self.update)
        self.timer.start(format)

    def update(self):
        self.startDate = QDateTime(self.date.currentDate(), self.time.currentTime())
        self.days = self.startDate.daysTo(self.endDate)

        self.hours = self.endDate.time().hour() - self.startDate.time().hour()
        if self.hours <= 0:
            if self.days > 0:
                self.days = self.days - 1
                self.hours = self.hours + 24

        self.minutes = self.endDate.time().minute() - self.startDate.time().minute()
        if self.minutes <= 0:
            if self.hours > 0:
                self.hours = self.hours - 1
                self.minutes = self.minutes + 60

        self.seconds = self.endDate.time().second() - self.startDate.time().second()
        if self.seconds <= 0:
            if self.minutes > 0:
                self.minutes = self.minutes - 1
                self.seconds = self.seconds + 60

        self._status = self.get_status()

        if self.days != 0:
            hrs = self.hours + self.days*24
        else:
            hrs = self.hours

        countdown = '{0}:{1}:{2}'.format(hrs, self.minutes, self.seconds)
        self.countdown.emit(countdown)

        self._dateline = self.endDate.toString('dd/MM/yy - hh:mm:ss')
        self._enddate = self.endDate.date().toString('dd/MM/yy')
        self._endtime = self.endDate.time().toString('hh:mm:ss')

    def get_status(self):
        if self.days < 0:
            self._status = 'Overdued'
        elif self.days == 0:
            self._status = 'Urgent'
        elif self.days <= 2:
            self._status = 'Due Tomorrow'
        elif self.days > 2 and self.days < 7:
            self._status = 'Due Soon'
        elif self.days == 7:
            self._status = '1 Week'
        else:
            self._status = 'Counting'

        return self._status

    def dateline(self):
        return self._dateline

    def enddate(self):
        return self._enddate

    def endtime(self):
        return self._endtime

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 16/11/2019 - 7:00 PM
# © 2017 - 2018 DAMGteam. All rights reserved