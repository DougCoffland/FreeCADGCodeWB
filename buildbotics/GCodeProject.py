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
import validator as VALID

class ViewGCode:
	def __init__(self,obj):
		obj.Proxy = self
		
	def attach(self,obj):
		return
		
	def getDefaultDisplayMode(self):
		return 'Shaded'
		
	def getIcon(self):
		return """
           /* XPM */
static char * cnc_xpm[] = {
"25 25 100 2",
"  	c None",
". 	c #E7E7E7",
"+ 	c #E8E8E8",
"@ 	c #C0C0C0",
"# 	c #313131",
"$ 	c #010101",
"% 	c #3E3E3E",
"& 	c #D4D4D4",
"* 	c #E6E6E6",
"= 	c #E5E5E5",
"- 	c #E4E4E4",
"; 	c #E3E3E3",
"> 	c #E9E9E9",
", 	c #EAEAEA",
"' 	c #0D0D0D",
") 	c #676767",
"! 	c #E2E2E2",
"~ 	c #E1E1E1",
"{ 	c #E0E0E0",
"] 	c #DFDFDF",
"^ 	c #EBEBEB",
"/ 	c #020202",
"( 	c #121212",
"_ 	c #C7C7C7",
": 	c #ECECEC",
"< 	c #A8A8A8",
"[ 	c #9C9C9C",
"} 	c #DEDEDE",
"| 	c #DDDDDD",
"1 	c #DCDCDC",
"2 	c #EDEDED",
"3 	c #202020",
"4 	c #484848",
"5 	c #F2F2F2",
"6 	c #F0F0F0",
"7 	c #EFEFEF",
"8 	c #EEEEEE",
"9 	c #DADADA",
"0 	c #D9D9D9",
"a 	c #DBDBDB",
"b 	c #030303",
"c 	c #F5F5F5",
"d 	c #F3F3F3",
"e 	c #131313",
"f 	c #D7D7D7",
"g 	c #D5D5D5",
"h 	c #757575",
"i 	c #919191",
"j 	c #F8F8F8",
"k 	c #7A7A7A",
"l 	c #D2D2D2",
"m 	c #161616",
"n 	c #C8C8C8",
"o 	c #C6C6C6",
"p 	c #C4C4C4",
"q 	c #C3C3C3",
"r 	c #565656",
"s 	c #AEAEAE",
"t 	c #B8B8B8",
"u 	c #B7B7B7",
"v 	c #B5B5B5",
"w 	c #B3B3B3",
"x 	c #373737",
"y 	c #363636",
"z 	c #353535",
"A 	c #181818",
"B 	c #2F2F2F",
"C 	c #303030",
"D 	c #D8D8D8",
"E 	c #6A6A6A",
"F 	c #D3D3D3",
"G 	c #1C1C1C",
"H 	c #6C6C6C",
"I 	c #5C5C5C",
"J 	c #A1A1A1",
"K 	c #6D6D6D",
"L 	c #ABABAB",
"M 	c #424242",
"N 	c #727272",
"O 	c #3A3A3A",
"P 	c #888888",
"Q 	c #AAAAAA",
"R 	c #616161",
"S 	c #646464",
"T 	c #070707",
"U 	c #B9B9B9",
"V 	c #0A0A0A",
"W 	c #0B0B0B",
"X 	c #F7F7F7",
"Y 	c #8F8F8F",
"Z 	c #F4F4F4",
"` 	c #D6D6D6",
" .	c #696969",
"..	c #F1F1F1",
"+.	c #444444",
"@.	c #A9A9A9",
"#.	c #050505",
"$.	c #414141",
"%.	c #0F0F0F",
"&.	c #717171",
". . + + @ # $ $ $ $ % & * = = = - - - ; ; ; ; ; ; ",
"> , . ' $ $ $ $ $ $ $ $ ) = - ; ; ! ~ ~ { { ] { ~ ",
"^ ^ / $ ( _ : ^ , > < $ $ [ - ; ! { ] } | 1 1 | } ",
"2 3 $ 4 5 6 7 8 : ^ > 9 $ $ ; ~ { ] | 1 9 0 0 9 a ",
"+ $ b c c d 5 6 8 : , + e $ { ~ ] | a 0 f g g f 0 ",
"h $ i j j $ e 5 6 8 ^ k $ $ $ 9 } 1 0 f $ $ l & f ",
"m $ c j j $ / n o p q r $ $ $ s t u v w $ $ l & f ",
"$ $ d c c $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ g f 0 ",
"$ $ 6 5 5 $ $ x y y z A $ $ $ B # # # C $ $ D 9 a ",
"/ $ 2 8 8 $ / ^ , > + E $ $ $ F ! ~ ] } $ $ 1 | } ",
"G $ + ^ ^ $ / > > + . H $ $ $ F ; ! ~ ~ $ $ ] { ~ ",
"I $ J + + $ / . . . * K $ $ $ & = - - - $ $ ; ; ; ",
"L $ M - = $ / = = = = N $ $ $ f = = = * $ $ * * * ",
"; $ / ~ ~ $ / ; ; ; - = O $ P . . . + > $ $ > > > ",
"~ $ $ 9 } $ / { ~ ! ; - q Q 9 . + > , ^ $ $ : : ^ ",
"] R $ S a $ / } { ~ ! ; = * . > , ^ : 8 $ $ 6 7 8 ",
"1 g $ / f $ / 1 } ] ~ ; - * . > ^ : 8 6 $ $ d 5 6 ",
"9 D T $ U $ $ V V W W W W W W W W W W W $ $ X c d ",
"0 f Y $ W $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ X X Z ",
"9 D ` $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ M c d ",
"1 9 D  .$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ ..6 ",
"} | 1 b $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ +.8 ",
"~ { @.$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ ^ ",
"; ! #.$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $.",
"- - %.$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ &."};
           """
	
class GCodeProject():
	def __init__(self):
		self.jobList = []
		self.defineJobUi =  FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + '/resources/ui/createjob.ui')
		self.defineJobUi.buttonBox.accepted.connect(self.accept)
		self.defineJobUi.buttonBox.rejected.connect(self.reject)
		self.defineJobUi.nameLE.textChanged.connect(self.validate)
		
		intValid = VALID.MyIntValidator()
		doubleValid = VALID.MyDoubleValidator()	

	def GetResources(self):
		return {'Pixmap'  : os.path.dirname(__file__) + '/resources/svg/cnc.svg', # the name of a svg file available in the resources
                'MenuText': "New GCode Project",
                'ToolTip' : "Sets up a new project for creating G-Code paths from FreeCAD Shapes"}

	def aGCodeJobIsSelected(self):
		mw = FreeCADGui.getMainWindow()
		tree = mw.findChildren(QtGui.QTreeWidget)[0]
		numberOfInstances = 0
		for item in tree.selectedItems():
			obj = FreeCAD.ActiveDocument.getObjectsByLabel(item.text(0))[0]
			try:
				if obj.ObjectType == "GCodeJob": numberOfInstances += 1
			except:
				continue
		if numberOfInstances != 1: return False
		return True	
		
	def validate(self):
		""" Check fields, turn label red if they are not complete or are invalid. Only enable OK if everything is
		complete and valid"""
		valid = True
		if VALID.setLineEditLabelBG(self.defineJobUi.nameLE, self.defineJobUi.nameLabel) is not True: valid = False
		name = self.defineJobUi.nameLE.text().strip()
		if len(FreeCAD.ActiveDocument.getObjectsByLabel(name)) > 0:
			self.defineJobUi.nameLabel.setStyleSheet("QLabel {background-color: red}")
			valid = False
			
		return valid
		
	def Activated(self):
		if self.aGCodeJobIsSelected():
			print "a job is selected"
		else:
			print "no job is selected"
		self.defineJobUi.show()       
		return
		
	def accept(self):
		self.defineJobUi.hide()
		obj = FreeCAD.ActiveDocument.addObject('App::DocumentObjectGroupPython', "GCodeJob")
		ViewGCode(obj.ViewObject)
		obj.addProperty("App::PropertyString","ObjectType").ObjectType = "GCodeJob"
		obj.setEditorMode("ObjectType",("ReadOnly",))
		obj.Label = self.defineJobUi.nameLE.text()
		FreeCAD.ActiveDocument.recompute()
		return True
		
	def reject(self):
		self.defineJobUi.hide()
		return False

	def IsActive(self):
		return True

FreeCADGui.addCommand('New_Project',GCodeProject())
