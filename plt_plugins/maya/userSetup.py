# coding=utf-8

"""
Script Name: userSetup.py
Author: Do Trinh/Jimmy - TD artist
"""

# -------------------------------------------------------------------------------------------------------------
""" About Plt """

__appname__ = "Pipeline Tool"
__module__ = "Plt"
__version__ = "13.0.1"
__organization__ = "DAMG team"
__website__ = "www.dot.damgteam.com"
__email__ = "dot@damgteam.com"
__author__ = "Trinh Do, a.k.a: Jimmy"
__root__ = "PLT_RT"
__db__ = "PLT_DB"
__st__ = "PLT_ST"

# -------------------------------------------------------------------------------------------------------------

import json
import logging
import os
import sys

# -------------------------------------------------------------------------------------------------------------
# IMPORT MAYA PYTHON MODULES
# -------------------------------------------------------------------------------------------------------------
from maya import cmds, mel

from plt_plugins.maya.modules import MayaVariables as var

# ------------------------------------------------------
# VARIALBES ARE USED BY ALL CLASSES
# ------------------------------------------------------
# We can configure the current level to make it disable certain logs when we don't want it.
NAMES = var.MAINVAR
SCRPTH = os.path.join(os.getenv(__root__), 'appData', 'config')
MESSAGE = var.MESSAGE
ID = 'UserSetup'
KEY = 'PYTHONPATH'

logging.basicConfig()
logger = logging.getLogger('userSetup.py')
logger.setLevel(logging.DEBUG)

# ----------------------------------------------------------------------------------------------------------- #
"""                                      USER SETUP - UPDATE ALL PATHS                                      """
# ----------------------------------------------------------------------------------------------------------- #

class InitUserSetup(object):

    """
    This class is to make a menu in main layout for whenever you want to load the UI
    """

    def __init__(self):

        super(InitUserSetup, self).__init__()
        # First greeting to user
        # self.greetings()

        # var.createLog('maya')
        #
        # SCR = os.path.join( SCRPTH, NAMES['os'][0] )
        #
        # if os.path.exists( SCR ):
        #     # logger.info( 'Start updateing sys path' )
        #     self.updatePathFromUser(SCR)

        # Create menu in Maya Layout
        self.makePipelineMenu()

        # Create port for Vray material presets pro
        try:
            cmds.commandPort(n = "localhost:7088")

        except RuntimeError:
            logger.debug('port:7088 already activated')

        else:
            pass

        # Load pipeline tool custom layout
        self.loadLayout()
        # Load pipeline tool UI dockable
        self.mayaMainUI()
        # Load timeline color marker script
        self.loadTimelineColorMarker()

    def makePipelineMenu(self):
        # Make menu in main Maya layout
        mainMenu = cmds.menu(l='Pipeline Tool', p='MayaWindow')
        # Menu item of main menu
        cmds.menuItem(l='Load Pipeline Tool', p=mainMenu, c=self.mayaMainUI)
        cmds.menuItem(l='Change layout', p=mainMenu, c=self.loadLayout)
        cmds.menuItem(l='About', p=mainMenu, c=self.aboutMainUI)

        info = {}

        for key in sorted(os.environ.keys()):
            info[key] = os.getenv(key)

        sysPth = ""

        for pth in sys.path:
            sysPth += pth

        info['sysPth'] = sysPth

        filePth = os.path.join(os.getenv(__root__), 'appData', 'maya_config.json')

        with open(filePth, 'w') as f:
            json.dump(info, f, indent=4)

        # logger.info('saving data to %s' % filePth)

    def updatePathFromUser(self, scr):

        with open(scr, 'r') as f:
            env = json.load(f)

        for k in env:
            lnks = str(env[k]).split(';')
            for lnk in lnks:
                if os.path.exists(lnk):
                    if not lnk in sys.path:
                        sys.path.append(lnk)
                        # logger.info('Updated system path: %s' % lnk)

    def mayaMainUI(self, *args):
        from plt_plugins.maya import InitTool
        reload(InitTool)
        InitTool.initilize()

    def aboutMainUI(self, *args):
        aboutWindow = 'aboutWindow'

        if cmds.window(aboutWindow, q=True, exists=True):
            cmds.deleteUI(aboutWindow)

        cmds.window(aboutWindow, t='About')
        cmds.rowColumnLayout(nc=3, cw=[(1,25),(2,250),(3,25)])
        cmds.text(l='')
        cmds.text(l=var.MESSAGE['mainUIabout'])
        cmds.text(l='')
        cmds.showWindow(aboutWindow)

    def loadLayout(self, *args):
        # Get list current layout
        listLayout = cmds.workspaceLayoutManager(lul=True)

        # Check Layout exists, if not, import pipeline layout from source data
        if not 'PipelineTool' in listLayout:
            # Path of layout file from source data by default
            layoutPth = os.path.join(os.getenv(__root__), 'maya/layout/pipelineTool.json')

            # Check if it is not there, it may happen because the file might be moved or deleted
            if os.path.exists(layoutPth):
               cmds.workspaceLayoutManager(i = layoutPth)
               mel.eval('onSetCurrentLayout "pipelineTool";')
            else:
                logger.info('%s is not exists' % layoutPth)
                pass
        # If the file is already there, dont need to import, change layout then.
        else:
            mel.eval('onSetCurrentLayout "pipelineTool";')

    def loadTimelineColorMarker(self, *args):
        from plt_plugins.maya.modules import TimelineMarker
        reload(TimelineMarker)
        TimelineMarker.initialize()

    def greetings(self):

        hello = 'Hello %s' % NAMES['user']

        welcomeID = 'welcomeID'
        welcomeTitle = 'Welcome'

        if cmds.window(welcomeID, q=True, exists=True):
            cmds.deleteUI(welcomeID)

        cmds.window(welcomeID, t=welcomeTitle)

        cmds.rowColumnLayout(nc=3, cw=[(1, 25), (2, 150), (3, 25)])
        cmds.text(l='')
        cmds.text(l=hello)
        cmds.text(l='')

        cmds.showWindow(welcomeID)


cmds.evalDeferred('InitUserSetup()')

# ----------------------------------------------------------------------------------------------------------- #
"""                                                 END OF CODE                                             """
# ----------------------------------------------------------------------------------------------------------- #