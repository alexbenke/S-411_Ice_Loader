# -*- coding: utf-8 -*-
"""
/***************************************************************************
 S411_ICE_DATA
                                 A QGIS plugin
 Loads IHO S-411 Ice Data from BSH Server
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-11-02
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Noiromo / Alexander Benke
        email                : a.benke@noiromo.com
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
import ftplib
import os.path
import zipfile

from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
# Initialize Qt resources from file resources.py
# Import the code for the dialog
from .s411_ice_data_loader_dialog import S411_ICE_DATADialog
from qgis.utils import iface


class S411_ICE_DATA:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'S411_ICE_DATA_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&S-411 ICE DATA Loader (BSH)')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('S411_ICE_DATA', message)

    def add_action(
            self,
            icon_path,
            text,
            callback,
            enabled_flag=True,
            add_to_menu=True,
            add_to_toolbar=True,
            status_tip=None,
            whats_this=None,
            parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/s411_ice_data_loader/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'IHO S-411 Ice Data Loader'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&S-411 ICE DATA Loader (BSH)'),
                action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = S411_ICE_DATADialog()

        # Own Code
        fullIceDataSets = []
        with ftplib.FTP('ftp.bsh.de') as ftp:
            print(ftp.getwelcome())
            try:
                ftp.login()
                ftp.cwd('outgoing/eisbericht/S411')
                files = []
                ftp.retrlines('LIST', files.append)
                #fullIceDataSets.append("most recent")
                for fl in files:
                    if "S411_full" in fl:
                        tokens = fl.split(maxsplit=9)
                        fullIceDataSets.append(
                            str(tokens[8]).replace(".zip", ""))
                fullIceDataSets.sort(reverse=True)
                self.dlg.comboBox.addItems(fullIceDataSets)

                self.dlg.show()
                result = self.dlg.exec_()
                if result:
                    savedir = 'C:/temp/ice'
                    if not os.path.exists(savedir):
                        os.makedirs(savedir)
                        os.chdir(savedir)
                    else:
                        os.chdir(savedir)
                    comboBoxValue = str(self.dlg.comboBox.currentText())
                    iceDataSetName = comboBoxValue + '.zip'
                    localFile = savedir + '/' + iceDataSetName
                    print(iceDataSetName)
                    ftp.retrbinary('RETR ' + iceDataSetName, open(localFile, 'wb').write)
                    ftp.close()
                    localZipFile = zipfile.ZipFile(localFile)
                    localZipFile.extractall()
                    localZipFile.close()
                    os.remove(localFile)
                    
                    iceDataSetGmlPath = localFile.replace('.zip','/data/') + comboBoxValue + '.gml'
                    print (iceDataSetGmlPath)
                    
                    # get Style
                    dirname = os.path.dirname(__file__)
                    filename = os.path.join(dirname, 'SLD\\seaice_iceact.sld')
                    print (filename)
                    
                    vlayer = iface.addVectorLayer(iceDataSetGmlPath, comboBoxValue, "ogr")
                    vlayer.loadSldStyle(filename)
                    if not vlayer:
                      print("Layer failed to load!")
            except ftplib.all_errors as e:
                print('FTP error: ', e)

        # End Own Code