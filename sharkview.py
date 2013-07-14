#!/usr/bin/python
# -*- coding: utf-8 -*-
#-----Importar delsistema
import sys
import subprocess
import re
import os
#-----Importar de PyQt4
from PyQt4 import QtCore, QtGui, QtWebKit, QtNetwork
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *
from PyKDE4.kdeui import KIcon
import time, threading


def open_signin(u):
  """
  Si la página fue cargada, busca el letrero de Sign In, cuando lo encuentra hace click en él y ejecuta logear
  En cualquier caso, muestra la ventana.
  """
  global started,frame
  #print open_signin.__doc__
  if u==True:
    #frame2 = web.page().currentFrame()
    
    logbuton1 = frame.findFirstElement("a[id=\"header-login-btn\"]")
    #print logbuton1.tagName()
    tiempo=time.time()
    while (logbuton1.tagName()=="" and started==0) and time.time()-tiempo<25:
      ##time.sleep(3)
      logbuton1 = frame.findFirstElement("a[id=\"header-login-btn\"]")
      
    print "logbuton1"+logbuton1.tagName()
    if logbuton1.tagName()=="":started+=1
    started+=1
    logbuton1.evaluateJavaScript("click()")
    pos2 = QPoint(logbuton1.geometry().center());
    event0 = QMouseEvent(QEvent.MouseButtonPress, pos2, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
    app.sendEvent(web.page(), event0);
    event1 = QMouseEvent(QEvent.MouseButtonRelease, pos2, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
    app.sendEvent(web.page(), event1)
    
    #threading.Timer(15, logear(u)).start()
    logear(u)
    #threading.Timer(17, web.show()).start()
    #web.show()
    #systray.show()
    
    
    #timeLine.setFrameRange(0, 1)
    #timeLine.start

    #toglear(u)
  #web.show()

def logear(u):
  global started,frame
  #open_signin(1)
  #print u
  if u==1:
    #frame = web.page().currentFrame()

    collection3 = frame.findFirstElement("input[id=\"login-password\"]")
    #collection3.toList().setAttribute("type","text")
    #collection3.evaluateJavaScript("this.type = 'text'")
    ##print collection3.toOuterXml(),collection3.toInnerXml()
    ##collection3.setFocus()
    ##collection3.setOuterXml("""<input type="text" class="login-text placeholder-input" id="login-password" name="password" value='clave'>""")
    collection3.evaluateJavaScript("this.value = 'clave'")
    #collection3.setAttribute("value","clave")

    collection2 = frame.findFirstElement("input[id=\"login-username\"]")
    #collection2.toList().setAttribute("value","usuario")
    ##print collection2.toOuterXml(),collection2.toInnerXml()
    collection2.evaluateJavaScript("this.value = 'usuario'")
    #collection = frame.documentElement()
    ##for i in collection2.toList ():
      ###print i.namespaceUri(), i.tagName(),i.toInnerXml().toUtf8(), i.attribute("class")
      ##i.setAttribute("value","usuario")
    
    logbuton2 = frame.findFirstElement("""a[data-translate-text="SIGN_IN"][class="btn btn-large btn-primary submit"]""")
    print started
    tiempo=time.time()
    while (logbuton2.tagName()=="" and started==1) and time.time()-tiempo<15:
      logbuton2 = frame.findFirstElement("""a[data-translate-text="SIGN_IN"][class="btn btn-large btn-primary submit"]""")
      #print logbuton2.tagName(),started
    started+=1
    print "logbuton2"+logbuton2.tagName()
    #logbuton2.evaluateJavaScript("this.click()")
    pos = QPoint(logbuton2.geometry().center());
    event0 = QMouseEvent(QEvent.MouseButtonPress, pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
    app.sendEvent(web.page(), event0);
    event1 = QMouseEvent(QEvent.MouseButtonRelease, pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
    app.sendEvent(web.page(), event1)
    web.show()


def toglear(u):
  #open_signin(1)
  global frame
  
  #for c in cookie.allCookies ():
     #print c.toRawForm ()
  
  #print u,web.isVisible()
  if u==QSystemTrayIcon.Trigger:
    if web.isVisible():
      web.hide()
    else:
      web.show()
  if u==1 or u==4:
    
    #frame = web.page().currentFrame()
    #logbuton2 = frame.findFirstElement("""a[data-translate-text="SIGN_IN"][class="btn btn-large btn-primary submit"]""")
    #print "logbuton2"+logbuton2.tagName()
    
    
    playpause_button = frame.findFirstElement("a[id=\"play-pause\"]")
    pos = QPoint(playpause_button.geometry().center());
    event0 = QMouseEvent(QEvent.MouseButtonPress, pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
    app.sendEvent(web.page(), event0);
    event1 = QMouseEvent(QEvent.MouseButtonRelease, pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
    app.sendEvent(web.page(), event1)
    
    #collection = frame.findAllElements("a[id=\"play-pause\"]")
    #collection = frame.documentElement()
    #for i in collection.toList ():
      ##print i.namespaceUri(), i.tagName(),i.toInnerXml().toUtf8(), i.attribute("class")
      ##i.setAttribute("class","player-btn player-icon paused")
      ##i.evaluateJavaScript("click()")
      #pos = QPoint(i.geometry().center());
      #event0 = QMouseEvent(QEvent.MouseButtonPress, pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
      #app.sendEvent(web.page(), event0);
      #event1 = QMouseEvent(QEvent.MouseButtonRelease, pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier);
      #app.sendEvent(web.page(), event1)
      
      #for j in cookie.allCookies():
         ##print j.name(),j.path(),j.value()
         #print j.toRawForm()


	
  #if u==4:
    #web.setUrl(QUrl(""))
    ##open_signin(1)
    
def save_settings():
  global cookie
  #settings.setValue("cookie", cookie.allCookies()[0].value());
  #print cookie.allCookies()[cookie.allCookies().indexOf("PHPSESSID")].value()
  settings.beginGroup("cookie")
  #print cookie.allCookies().index("PHPSESSID")
  for c in cookie.allCookies ():
    if c.name()=="PHPSESSID":
      print c.toRawForm()
      settings.setValue("cookie", c.value());

app=QtGui.QApplication(sys.argv) 
web=QWebView()
#started=0
started=5
#web.settings().setAttribute(QWebSettings.JavaEnabled, True)
#web.settings().setAttribute(QWebSettings.JavascriptEnabled, True)
web.settings().setAttribute(QWebSettings.PluginsEnabled, True)
url = QUrl("http://listen.grooveshark.com/")
settings=QSettings("sharkview", "sharkview")
#url.setUserInfo( "usuario:clave" );

cookie=QNetworkCookieJar()
settings.beginGroup("cookie")
cookieval = settings.value("cookie").toByteArray()
#print cookieval
if not cookieval.isEmpty():
  #print cookieval
  onecookie=QNetworkCookie("PHPSESSID",cookieval)
  onecookie.setDomain(".grooveshark.com")
  onecookie.setPath("/")
  cookie.setAllCookies ( [onecookie,] )
settings.endGroup();

#for c in cookie.allCookies ():
  #print c.toRawForm ()
web.page().networkAccessManager().setCookieJar( cookie )

#def openandclick(u):
  #open_signin(u)
  #toglear(u)

web.load(url)
frame = web.page().currentFrame()
logbuton1 = frame.findFirstElement("a[id=\"header-login-btn\"]")
logbuton2 = frame.findFirstElement("""a[data-translate-text="SIGN_IN"][class="btn btn-large btn-primary submit"]""")
#settings=QSettings("sharkview", "sharkview")
#settings.setValue("size", 44);
#for c in cookie.allCookies ():
  #print c.toRawForm ()


#open_signin(1)
systray=QSystemTrayIcon()
systray.setIcon(KIcon("window-close"))
systray.show()
web.show()
#timeLine = QTimeLine(10000)
app.connect(systray,SIGNAL("activated(QSystemTrayIcon::ActivationReason)"),toglear)
app.connect(app,SIGNAL("lastWindowClosed ()"),save_settings)
#app.connect(web,SIGNAL("loadFinished(bool)"),open_signin)
#app.connect(timeLine, SIGNAL("frameChanged(int)"),toglear );

sys.exit(app.exec_())
