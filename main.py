
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView

class iceController(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.callback = None

    def dump(self):
        print('Callback is %s' % self.callback)
        print('Callback is callable %s' % self.callback.isCallable)
        print('Callback is callable %s' % self.callback.isCallable())
        self.callback.call()

    @pyqtSlot(str, 'QJSValue')
    def enqueue(self, command, callback):
        print('Enqueuing function of %s' % command)
        self.callback = callback
        self.dump()

    @pyqtSlot()
    def processResponses(self):
        print('processing responses')
        self.dump()

    @pyqtSlot(str)
    def log(self, s):
        print(s)

print('Starting ICE Control GUI...')        
app = QApplication(sys.argv)
view = QQuickView()
context = view.rootContext()

ice = iceController()
context.setContextProperty('PyConsole', ice)
context.setContextProperty('ice', ice)

view.setSource(QUrl("main.qml"))
