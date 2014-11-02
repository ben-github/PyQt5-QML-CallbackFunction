import QtQuick 2.0
import "application.js" as App

Rectangle {
    id: appWindow
    width: 825
    height: 600
    color: '#000000'
    Component.onCompleted: App.onLoad()
}
