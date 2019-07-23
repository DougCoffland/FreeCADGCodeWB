
# FreeCAD init script of buildbotics workbench  

#***************************************************************************
#*   Copyright (c) 2019 Buildbotics LLC                              *   
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/
import FreeCAD,FreeCADGui
from PySide import QtGui, QtCore
import os

from Tool import Tool
import validator as VAL

class CutGui():
	def __init__(self):
		self.createCutUi = FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + "/resources/ui/cut.ui")
		
		ui = self.createCutUi
		ui.logoL.setPixmap(QtGui.QPixmap(os.path.dirname(__file__) + "/resources/ui/logo side by side.png"))				
		ui.cutTypeCB.currentIndexChanged.connect(self.onToolTypeChanged)
		
	def GetResources(self):
		return {'Pixmap'  : os.path.dirname(__file__) +  "/resources/svg/cutsymbol.svg", # the name of a svg file available in the resources
                'MenuText': "New Cut",
                'ToolTip' : "Sets up a new cut that can be added to a g-code job"}

	def onToolTypeChanged(self):
		ui = self.createCutUi
		ui.stackedWidget.setCurrentIndex(ui.cutTypeCB.currentIndex())
	
	def Activated(self):
		self.createCutUi.show()
		
	def IsActive(self):
		return True


FreeCADGui.addCommand('New_Cut',CutGui())
