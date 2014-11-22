
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QJSValue


class IceController(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.callback = []

    def dump(self):
        print("Dump was called")
        for c in self.callback:
            c.call([QJSValue("Data from Python")])
        self.callback[:] = []

    @pyqtSlot(str, "QJSValue")
    def enqueue(self, command, callback):
        print("Enqueuing function of %s" % command)
        self.callback.append(QJSValue(callback))

    @pyqtSlot()
    def processResponses(self):
        print("processing responses")
        self.dump()

    @pyqtSlot(str)
    def log(self, s):
        print(s)


print("Starting ICE Control GUI...")
app = QApplication(sys.argv)
view = QQuickView()
context = view.rootContext()

ice = IceController()
context.setContextProperty("PyConsole", ice)
context.setContextProperty("ice", ice)

view.setSource(QUrl("main.qml"))
