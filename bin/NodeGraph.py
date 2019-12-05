# -*- coding: utf-8 -*-
"""

Script Name: pNodeGraph.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import sys

# PyQt5
from PyQt5.QtWidgets import QApplication, QGridLayout

# Plt
from appData                                        import ANTIALIAS, UPDATE_FULLVIEW, KEY_DEL
from toolkits.Widgets.Widget                        import Widget, AppIcon
from plugins.NodeGraph.NodeGraphMenuBar import NodeGraphMenuBar
from bin.Node import Node, Edge
from bin.Scene import Scene
from bin.View import View

from utils import getUnix

# -------------------------------------------------------------------------------------------------------------
""" NoderViewer """

class NodeGraph(Widget):

    key = 'NodeGraph'

    def __init__(self, parent=None):
        super(NodeGraph, self).__init__(parent)
        self.mtd                    = {}
        self.Nodes                  = []
        self.setWindowIcon(AppIcon(32, 'NodeGraph'))
        self.menuBar                = NodeGraphMenuBar(self)

        self.view                   = View()
        self.sceneView              = Scene(self)                                         # Setup scene.
        self.view.setScene(self.sceneView)
        self.view.setRenderHint(ANTIALIAS)
        self.view.setViewportUpdateMode(UPDATE_FULLVIEW)

        sceneWidth = 1000
        sceneHeight = 500

        self.sceneView.nodeMoved.connect(self.view.nodeMoved)                # Connect scene node moved signal_cpu
        self.sceneView.selectionChanged.connect(self.view._returnSelection)  # Connect signals.
        self.sceneView.setSceneRect(0, 0, sceneWidth, sceneHeight)

        node1 = self.createNode({'name': 'Node1', 'pos': [0, 0]})
        node2 = self.createNode({'name': 'Node2', 'pos': [20, 20]})

        self.layout = QGridLayout()
        self.layout.addWidget(self.menuBar, 0, 0, 1, 1)
        self.layout.addWidget(self.view, 1, 0, 1, 1)
        self.setLayout(self.layout)
        self.resize(1000, 500)

        self.mtd['objName'] = '{0} {1}'.format(self.key, str(1))
        self.mtd['unix'] = getUnix()
        self.mtd['nodes'] = self.view.getNodes()

    def createNode(self, nodeData):
        return self.view.createNode(nodeData)

    def clearScene(self):
        pass

    def addSceneMenuAction(self, menu):
        pass

    def loadScene(self):
        pass

    def mergeScene(self):
        pass

    def storeCurrentScene(self):
        pass

    def createEdge(self, sourceNode, sourceAttr, targetNode, targetAttr):

        plug = self.scene().nodes[sourceNode].plugs[sourceAttr]
        socket = self.scene().nodes[targetNode].sockets[targetAttr]

        edge = Edge(plug.center(), socket.center(), plug, socket)

        edge.plugNode = plug.parentItem().name
        edge.plugAttr = plug.attribute
        edge.socketNode = socket.parentItem().name
        edge.socketAttr = socket.attribute
        plug.connect(socket, edge)
        socket.connect(plug, edge)
        edge.updatePath()
        self.scene().addItem(edge)

    def keyPressEvent(self, event):
        if event.key() == KEY_DEL:
            selectedNodes = [i for i in self.scene.selectedItems() if isinstance(i, Node)]
            for node in selectedNodes:
                node.destroy()
        super(NodeGraph, self).keyPressEvent(event)

    def contextMenuEvent(self, event):
        pass

def main():
    nodeGrahp = QApplication(sys.argv)
    layout = NodeGraph()
    layout.show()
    nodeGrahp.exec_()


if __name__ == '__main__':
    main()

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 5/07/2018 - 7:07 AM
# © 2017 - 2018 DAMGteam. All rights reserved