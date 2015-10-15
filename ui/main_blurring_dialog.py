# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoHealth
                                 A QGIS plugin

                              -------------------
        begin                : 2014-08-20
        copyright            : (C) 2014 by Etienne Trimaille
        email                : etienne@trimaille.eu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from GeoHealth import *
from main_blurring import Ui_BlurringDialogBase
from os.path import join,dirname,abspath,isfile

class MainBlurringDialog(QDialog, Ui_BlurringDialogBase):
       
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self)
        self.setupUi(self)
        
        #Connect
        self.blur.signalAskCloseWindow.connect(self.hide)
        self.statistics.signalAskCloseWindow.connect(self.hide)
        
        self.setHelpWebView()
        
    def setHelpWebView(self):
        '''
        Set the help
        '''
        locale = QSettings().value("locale/userLocale")[0:2]
        locale = "." + locale
        helpFileBase = "main"
        helps = [helpFileBase + locale +".html", helpFileBase + ".html"]
        
        docPath = join(dirname(dirname(abspath(__file__))),'doc')
        for helpFileName in helps:
            fileHelpPath = join(docPath,helpFileName)
            if isfile(fileHelpPath):
                self.helpFile = fileHelpPath
                self.webview.load(QUrl(self.helpFile))
                break
        else:
            self.webview.setHtml("<h3>Help not available</h3>")
            
    def fillComboxboxLayers(self):
        self.statistics.fillComboxboxLayers()
        self.blur.fillComboxboxLayers()