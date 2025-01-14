# -*- coding: utf-8 -*-
"""

Script Name: {}.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import sys

# PyQt5
try:
    from PySide2.QtWebKitWidgets import QWebView as QWebEngineView
    from PySide2.QtWebKitWidgets import QWebPage as QWebEnginePage
except ImportError:
    from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

from PySide2.QtCore               import QFile, QIODevice, Qt, QTextStream, QUrl, Signal
from PySide2.QtWidgets            import (QAction, QApplication, QLineEdit, QMainWindow, QSizePolicy, QStyle, QTextEdit,
                                        QStatusBar)

from PySide2.QtNetwork            import QNetworkProxyFactory, QNetworkRequest

# PLM
from pyPLM.Widgets import Widget, VBoxLayout

# -------------------------------------------------------------------------------------------------------------
""" Pipeline Web browser """

class WebBrowser(QMainWindow):

    adjTitle                    = Signal(str)
    setProg                     = Signal(int)
    finishLoad                  = Signal(str)

    def __init__(self, url, parent=None):
        super(WebBrowser, self).__init__(parent)

        self.progress = 0

        fd = QFile(":/jquery.min.js")

        if fd.open(QIODevice.ReadOnly | QFile.Text):
            self.jQuery = QTextStream(fd).readAll()
            fd.close()
        else:
            self.jQuery = ''

        QNetworkProxyFactory.setUseSystemConfiguration(True)

        self.view = QWebEngineView(self)
        self.view.load(QUrl(url))
        self.view.loadFinished.connect(self.adjustLocation)
        self.view.titleChanged.connect(self.adjustTitle)
        self.view.loadProgress.connect(self.setProgress)
        self.view.loadFinished.connect(self.finishLoading)

        self.locationEdit = QLineEdit(self)
        self.locationEdit.setSizePolicy(QSizePolicy.Expanding, self.locationEdit.sizePolicy().verticalPolicy())
        self.locationEdit.returnPressed.connect(self.changeLocation)

        toolBar = self.addToolBar("Navigation")
        toolBar.addAction(self.view.pageAction(QWebEnginePage.Back))
        toolBar.addAction(self.view.pageAction(QWebEnginePage.Forward))
        toolBar.addAction(self.view.pageAction(QWebEnginePage.Reload))
        toolBar.addAction(self.view.pageAction(QWebEnginePage.Stop))
        toolBar.addWidget(self.locationEdit)

        viewMenu = self.menuBar().addMenu("&View")
        viewSourceAction = QAction("Page Source", self)
        viewSourceAction.triggered.connect(self.viewSource)
        viewMenu.addAction(viewSourceAction)

        effectMenu = self.menuBar().addMenu("&Effect")
        effectMenu.addAction("Highlight all links", self.highlightAllLinks)

        self.rotateAction = QAction(self.style().standardIcon(QStyle.SP_FileDialogDetailedView), "Turn images upside down",
                                    self, checkable=True) #, toggled=self.rotateImages)
        effectMenu.addAction(self.rotateAction)

        toolsMenu = self.menuBar().addMenu("&Tools")
        toolsMenu.addAction("Remove GIF images", self.removeGifImages)
        toolsMenu.addAction("Remove all inline frames",
                self.removeInlineFrames)
        toolsMenu.addAction("Remove all object elements",
                self.removeObjectElements)
        toolsMenu.addAction("Remove all embedded elements",
                self.removeEmbeddedElements)
        self.setCentralWidget(self.view)

    def viewSource(self):
        accessManager = self.view.page().networkAccessManager()
        request = QNetworkRequest(self.view.url())
        reply = accessManager.get(request)
        reply.finished.connect(self.slotSourceDownloaded)

    def slotSourceDownloaded(self):
        reply = self.sender()
        self.textEdit = QTextEdit()
        self.textEdit.setAttribute(Qt.WA_DeleteOnClose)
        self.textEdit.show()
        self.textEdit.setPlainText(QTextStream(reply).readAll())
        self.textEdit.resize(600, 400)
        reply.deleteLater()

    def adjustLocation(self):
        self.locationEdit.setText(self.view.url().toString())

    def changeLocation(self):
        url = QUrl.fromUserInput(self.locationEdit.text())
        self.view.load(url)
        self.view.setFocus()

    def adjustTitle(self):
        if 0 < self.progress < 100:
            self.setWindowTitle("{0} ({1}%%)".format(self.view.title(), self.progress))
        else:
            self.setWindowTitle(self.view.title())

    def setProgress(self, p):
        self.progress = p
        self.setProg.emit(self.progress)
        self.adjustTitle()

    def finishLoading(self):
        self.progress = 100
        self.adjustTitle()
        # self.view.page().mainFrame().evaluateJavaScript(self.jQuery)
        self.rotateImages(self.rotateAction.isChecked())

    def highlightAllLinks(self):
        code = """$('a').each(
                    function () {
                        $(this).scss('background-color', 'yellow') 
                    } 
                  )"""
        self.view.page().javaScriptPrompt(code)

    def rotateImages(self, invert):
        if invert:
            code = """
                $('img').each(
                    function () {
                        $(this).scss('-webkit-transition', '-webkit-transform 2s'); 
                        $(this).scss('-webkit-transform', 'rotate(180deg)') 
                    } 
                )"""
        else:
            code = """
                $('img').each(
                    function () { 
                        $(this).scss('-webkit-transition', '-webkit-transform 2s'); 
                        $(this).scss('-webkit-transform', 'rotate(0deg)') 
                    } 
                )"""

        # self.view.page().mainFrame().evaluateJavaScript(code)

    def removeGifImages(self):
        code = "$('[src*=gif]').remove()"
        self.view.page().runJavaScript(code)

    def removeInlineFrames(self):
        code = "$('iframe').remove()"
        self.view.page().runJavaScript(code)

    def removeObjectElements(self):
        code = "$('object').remove()"
        self.view.page().runJavaScript(code)

    def removeEmbeddedElements(self):
        code = "$('embed').remove()"
        self.view.page().runJavaScript(code)

# -------------------------------------------------------------------------------------------------------------
""" layout class """

class Browser(Widget):

    key = 'Browser'

    def __init__(self, url='vnexpress.net', parent=None):
        super(Browser, self).__init__(parent)

        self.url = url

        self.layout = VBoxLayout()
        self.buildUI()
        self.setLayout(self.layout)

    def buildUI(self):
        self.viewer = WebBrowser(self.url)
        self.viewer.setProg.connect(self.adjustTitle)
        self.layout.addWidget(self.viewer)

        self.statusBar = QStatusBar(self)
        self.layout.addWidget(self.statusBar)

    def setUrl(self, url):
        return self.viewer.view.load(QUrl(url))

    def adjustTitle(self, param):
        if 0 < param < 100:
            self.setWindowTitle("Browser ({0}%)".format(param))
        else:
            self.setWindowTitle("Browser")

def main():
    app = QApplication(sys.argv)
    browser = Browser(r'https://www.google.com.vn')
    browser.show()
    app.exec_()

if __name__ == '__main__':
    main()