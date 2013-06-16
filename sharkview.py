#!/usr/bin/python
# -*- coding: utf-8 -*-
#-----Importar delsistema
import sys
import subprocess
import re
import os
#-----Importar de PyQt4
from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from PyKDE4.kdeui import KIcon

def toglear(u):
  print u
  if u==QSystemTrayIcon.Trigger:
    if web.isVisible():
      web.hide()
    else:
      web.show()
  if u==1:
    frame = web.page().currentFrame()
    collection = frame.findAllElements("a[id=\"play-pause\"]")
    #collection = frame.documentElement()
    for i in collection.toList ():
      print i.namespaceUri(), i.tagName(),i.toInnerXml().toUtf8(), i.attribute("class")
      #i.setAttribute("class","player-btn player-icon paused")
      pos = QPoint(i.geometry().center());
      event0 = QMouseEvent(QEvent.MouseButtonPress, pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
      app.sendEvent(web.page(), event0);
      event1 = QMouseEvent(QEvent.MouseButtonRelease, pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
      app.sendEvent(web.page(), event1);


app=QtGui.QApplication(sys.argv) 
web=QWebView()
web.settings().setAttribute(QWebSettings.PluginsEnabled, True)
web.load(QUrl("http://listen.grooveshark.com/"))
systray=QSystemTrayIcon()
systray.setIcon(KIcon("window-close"))
systray.show()
web.show()
app.connect(systray,SIGNAL("activated(QSystemTrayIcon::ActivationReason)"),toglear)


sys.exit(app.exec_())
