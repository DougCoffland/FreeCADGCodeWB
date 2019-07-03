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
from PySide import QtGui, QtCore, QtWebKit
import os

class ViewTool:
	def __init__(self,obj):
		obj.Proxy = self
		
	def attach(self,obj):
		return
		
	def getDefaultDisplayMode(self):
		return 'Shaded'
		
	def getIcon(self):
		return """
/* XPM */
static char * tool_xpm[] = {
"16 16 45 1",
" 	c None",
".	c #FFFFFF",
"+	c #FFFFFD",
"@	c #E2E2E0",
"#	c #E6E6E6",
"$	c #FDFDFD",
"%	c #FEFEFE",
"&	c #B7B4B3",
"*	c #D3D3D1",
"=	c #FCFCFC",
"-	c #B6B2B1",
";	c #D3D1CF",
">	c #B1AFAD",
",	c #D0D0CE",
"'	c #FDFDFC",
")	c #FEFEFD",
"!	c #AEAFAD",
"~	c #D3D3D3",
"{	c #AEADAC",
"]	c #CDCCCB",
"^	c #817F80",
"/	c #ADADAE",
"(	c #FDFCFB",
"_	c #FBFBFB",
":	c #6B6B70",
"<	c #B3B6BC",
"[	c #FCFCFB",
"}	c #8F8F93",
"|	c #B9BCC3",
"1	c #FAFAF9",
"2	c #A6A5AA",
"3	c #ABAEB3",
"4	c #8A8A8E",
"5	c #AEB0B6",
"6	c #FFFFFE",
"7	c #868386",
"8	c #A8A8AC",
"9	c #88858A",
"0	c #A6A7AD",
"a	c #FAFAFA",
"b	c #AAA8A9",
"c	c #A4A3A8",
"d	c #B3B3B5",
"e	c #9D9B9C",
"f	c #FEFDFC",
" .....+@#$..... ",
".....%$&*=..... ",
"......%-;$..... ",
"......%>,'..... ",
"......)!~$..... ",
"......${]'..... ",
"......=^/(..... ",
"......_:<[..... ",
"......_}|1..... ",
".......23%..... ",
".......45...... ",
"......678...... ",
".......90...... ",
"......abc=..... ",
"......_def..... ",
"                "};
"""
		
class Tool():
	def __init__(self):
		self.createToolUi = FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + "/resources/ui/tool.ui")
		
		self.straightToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/straightBitPic.png")				
		self.taperedToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/taperedBitPic.png")				
		self.conicalToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/conicalBitPic.png")				
		self.ballToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/ballBitPic.png")				
		self.taperedBallToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/taperedBallBitPic.png")				
		
	def GetResources(self):
		return {'Pixmap'  : os.path.dirname(__file__) +  "/resources/svg/tool.svg", # the name of a svg file available in the resources
                'MenuText': "New Tool",
                'ToolTip' : "Sets up a new tool that can be added to a tool table"}
                
	def changeToolTypeWidget(self):
		i = self.createToolUi.toolTypeCB.currentIndex()
		self.createToolUi.stackedWidget.setCurrentIndex(i)
		if i == 1: self.createToolUi.imageLabel.setPixmap(self.straightToolPic)
		elif i == 2: self.createToolUi.imageLabel.setPixmap(self.taperedToolPic)
		elif i == 3: self.createToolUi.imageLabel.setPixmap(self.conicalToolPic)
		elif i == 4: self.createToolUi.imageLabel.setPixmap(self.ballToolPic)
		elif i == 5: self.createToolUi.imageLabel.setPixmap(self.taperedBallToolPic)
		else: self.createToolUi.imageLabel.setPixmap(None)

	def Activated(self):
		self.createToolUi.toolTypeCB.currentIndexChanged.connect(self.changeToolTypeWidget) 
		self.createToolUi.stackedWidget.setCurrentIndex(0)       
		self.createToolUi.show()       
		return
        
	def accept(self):
		self.createToolUi.hide()
		obj = FreeCAD.ActiveDocument.addObject('App::DocumentObjectGroupPython', "Tool")
		ViewTool(obj.ViewObject)
		FreeCAD.ActiveDocument.recompute()
		return True
		
	def reject(self):
		self.createToolUi.hide()
		return False

	def IsActive(self):
		"""Here you can define if the command must be active or not (greyed) if certain conditions
		are met or not. This function is optional."""
		mw = FreeCADGui.getMainWindow()
		tree = mw.findChildren(QtGui.QTreeWidget)[0]
		numberOfInstances = 0
		for item in tree.selectedItems():
			obj = FreeCAD.ActiveDocument.getObjectsByLabel(item.text(0))[0]
			if obj.ObjectType == "ToolTable": numberOfInstances += 1
		if numberOfInstances != 1: return False
		return True

FreeCADGui.addCommand('New_Tool',Tool())
