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

class ViewStraightTool(ViewTool):
	def getIcon(self):
		return """
/* XPM */
static char * straightTool_xpm[] = {
"9 25 42 1",
" 	c None",
".	c #D4A000",
"+	c #D8A000",
"@	c #D6A000",
"#	c #FFA000",
"$	c #FDA000",
"%	c #FBA000",
"&	c #FCA000",
"*	c #FA9D00",
"=	c #E49200",
"-	c #FB9E00",
";	c #CF8800",
">	c #E59300",
",	c #CD8700",
"'	c #E69300",
")	c #FC9E00",
"!	c #D08900",
"~	c #E79400",
"{	c #FC9F00",
"]	c #D18900",
"^	c #E29100",
"/	c #E89500",
"(	c #CE8700",
"_	c #F89D00",
":	c #FD9F00",
"<	c #DF9000",
"[	c #EA9500",
"}	c #F69B00",
"|	c #D28A00",
"1	c #DC8E00",
"2	c #EB9600",
"3	c #F39A00",
"4	c #FE9F00",
"5	c #D38A00",
"6	c #D98D00",
"7	c #EC9600",
"8	c #F19900",
"9	c #D48A00",
"0	c #D68B00",
"a	c #FEA000",
"b	c #ED9700",
"c	c #D58B00",
"  ...... ",
"  ...... ",
"  ...... ",
" +.....@ ",
"#$%%%%%&#",
"########*",
"########=",
"#######-;",
"#######>,",
"######-;,",
"######',,",
"#####)!,,",
"#####~,,;",
"####{],,^",
"####/,,(_",
"###:],,<#",
"###[,,,}#",
"##:|,,1##",
"##2,,,3##",
"#45,,6###",
"#7,,,8###",
"49,,0a###",
"b,,,b####",
"c,,54####",
"5,,2#####"};"""	

class ViewTaperedTool(ViewTool):
	def getIcon(self):
		return """
/* XPM */
static char * taperedBitPic_xpm[] = {
"16 25 59 1",
" 	c None",
".	c #D4A000",
"+	c #DE9700",
"@	c #DC9800",
"#	c #DD9800",
"$	c #DF9800",
"%	c #E89100",
"&	c #EA9300",
"*	c #EC9400",
"=	c #D98800",
"-	c #F09700",
";	c #FFA000",
">	c #E59200",
",	c #EE9800",
"'	c #CB8600",
")	c #F79C00",
"!	c #D08800",
"~	c #CA8500",
"{	c #FD9F00",
"]	c #FC9E00",
"^	c #D58B00",
"/	c #CD8700",
"(	c #F59900",
"_	c #FEA000",
":	c #DE8F00",
"<	c #EF9600",
"[	c #E89400",
"}	c #E79100",
"|	c #F19900",
"1	c #CE8700",
"2	c #F99D00",
"3	c #D18900",
"4	c #FB9D00",
"5	c #D88C00",
"6	c #E19100",
"7	c #EB9300",
"8	c #EB9600",
"9	c #F49A00",
"0	c #CE8800",
"a	c #E28F00",
"b	c #FA9E00",
"c	c #D38A00",
"d	c #EE9500",
"e	c #F69A00",
"f	c #FE9F00",
"g	c #DB8E00",
"h	c #E69300",
"i	c #E49200",
"j	c #D78900",
"k	c #DC8E00",
"l	c #FC9F00",
"m	c #F99C00",
"n	c #CC8700",
"o	c #C98500",
"p	c #C68200",
"q	c #C98300",
"r	c #ED9500",
"s	c #F29800",
"t	c #F29700",
"    ........    ",
"    ........    ",
"    ........    ",
"    ........    ",
"    ........    ",
"    ........    ",
"    +@@@@@#$%&*=",
"-;;;;;;;;;;;;;;>",
"&;;;;;;;;;;;;;,'",
" ;;;;;;;;;;;;)!~",
" {;;;;;;;;;;]^/ ",
" (;;;;;;;;;_:// ",
" <;;;;;;;;;[/// ",
" };;;;;;;;|1/// ",
"  ;;;;;;;23//// ",
"  4;;;;;{5///// ",
"  -;;;;;6/////  ",
"  7;;;;8/////1  ",
"   ;;;90////1a  ",
"   ;;bc/////8d  ",
"   efg/////h;&  ",
"   <i/////6;;   ",
"   j/////kf;;   ",
"    ////5l;;m   ",
"    nopqrsst}   "};
"""

class ViewConicalTool(ViewTool):
	def getIcon(self):
		return """
/* XPM */
static char * conicalBitPic_xpm[] = {
"17 25 48 1",
" 	c None",
".	c #D4A000",
"+	c #CE9B00",
"@	c #DF8C00",
"#	c #F69A00",
"$	c #F89C00",
"%	c #FB9D00",
"&	c #FD9F00",
"*	c #FDA000",
"=	c #FEA000",
"-	c #FFA000",
";	c #DA8B00",
">	c #E19100",
",	c #F49900",
"'	c #EA9500",
")	c #C78200",
"!	c #E58F00",
"~	c #F49A00",
"{	c #CE8800",
"]	c #FA9D00",
"^	c #FA9E00",
"/	c #D38A00",
"(	c #CB8600",
"_	c #EB9300",
":	c #FE9F00",
"<	c #DA8E00",
"[	c #CD8700",
"}	c #C88400",
"|	c #E59300",
"1	c #F19700",
"2	c #EF9800",
"3	c #F79C00",
"4	c #D08800",
"5	c #F69B00",
"6	c #D68B00",
"7	c #E89100",
"8	c #DF9000",
"9	c #FC9E00",
"0	c #E99500",
"a	c #ED9500",
"b	c #F39A00",
"c	c #CE8700",
"d	c #CC8600",
"e	c #D28A00",
"f	c #CA8400",
"g	c #C88300",
"h	c #C68100",
"i	c #CD8600",
"     ........    ",
"     ........    ",
"     ........    ",
"     ........    ",
"     .......+    ",
"@#$%&*******=--&;",
" --------------> ",
" ,------------') ",
" !-----------~{  ",
"  ]---------^/(  ",
"  _--------:<[}  ",
"   :-------|[[   ",
"   1------2[[[   ",
"    -----34[[[   ",
"    5---&6[[[    ",
"    7---8[[[[    ",
"     9-0[[[[     ",
"     abc[[[d     ",
"      e[[[[      ",
"      f[[[}      ",
"       [[[       ",
"       d[g       ",
"       h[        ",
"        i        ",
"                 "};
"""

class ViewBallTool(ViewTool):
	def getIcon(self):
		return """
/* XPM */
static char * ballBitPic_xpm[] = {
"25 25 39 1",
" 	c None",
".	c #D4A000",
"+	c #D5A000",
"@	c #F79B00",
"#	c #FFA000",
"$	c #FBA000",
"%	c #F7A000",
"&	c #F8A000",
"*	c #F9A000",
"=	c #FEA000",
"-	c #E89500",
";	c #FC9E00",
">	c #E09100",
",	c #CD8700",
"'	c #F79C00",
")	c #D68B00",
"!	c #EE9700",
"~	c #D08900",
"{	c #FD9F00",
"]	c #E39200",
"^	c #CE8700",
"/	c #F99D00",
"(	c #D98D00",
"_	c #F19900",
":	c #D28900",
"<	c #FE9F00",
"[	c #E79400",
"}	c #CE8800",
"|	c #FB9E00",
"1	c #DC8E00",
"2	c #D18900",
"3	c #F49A00",
"4	c #D48A00",
"5	c #EA9500",
"6	c #CF8800",
"7	c #E09000",
"8	c #E19100",
"9	c #E29100",
"0	c #D58B00",
"       ...........       ",
"       ...........       ",
"       ...........       ",
"       ...........       ",
"       ...........       ",
"       ...........       ",
"       ...........       ",
"       ...........       ",
"       ...........       ",
"       ...........       ",
"       ...........       ",
"       .....++++++       ",
"@#####$%%&&&&*****=####=-",
"######################;>,",
"#####################'),,",
"####################!~,,,",
" #################{]^,,,,",
" ################/(,,,,, ",
"  ##############_:,,,,,, ",
"  ############<[},,,,,^  ",
"   ##########|1,,,,,,2   ",
"    ########34,,,,,,)    ",
"     ######56,,,,,^1     ",
"       ##;7,,,,,,,       ",
"         5897106         "};
"""

class ViewTaperedBallTool(ViewTool):
	def getIcon(self):
		return """
/* XPM */
static char * taperedBallBitPic_xpm[] = {
"15 25 43 1",
" 	c None",
".	c #D4A000",
"+	c #EFA000",
"@	c #E3A000",
"#	c #E4A000",
"$	c #E6A000",
"%	c #FFA000",
"&	c #FD9F00",
"*	c #DA8D00",
"=	c #EC9600",
"-	c #D88C00",
";	c #D78C00",
">	c #F49A00",
",	c #CD8700",
"'	c #DF9000",
")	c #D68B00",
"!	c #FA9E00",
"~	c #CF8800",
"{	c #EA9500",
"]	c #E89400",
"^	c #D18900",
"/	c #FE9F00",
"(	c #D38A00",
"_	c #E39200",
":	c #EF9800",
"<	c #F69B00",
"[	c #D98D00",
"}	c #E99500",
"|	c #DC8E00",
"1	c #CE8800",
"2	c #F49B00",
"3	c #DD8F00",
"4	c #F19900",
"5	c #FB9E00",
"6	c #D28A00",
"7	c #EE9700",
"8	c #DE8F00",
"9	c #FEA000",
"0	c #E69300",
"a	c #F59B00",
"b	c #E79000",
"c	c #000000",
"d	c #E49200",
"     ......    ",
"     ......    ",
"     ......    ",
"     ......    ",
"    +@####$    ",
"%%%%%%%%%%%%%&*",
"%%%%%%%%%%%%%=-",
" %%%%%%%%%%%%; ",
" %%%%%%%%%%%>, ",
" %%%%%%%%%%%') ",
" %%%%%%%%%%!~{ ",
"  %%%%%%%%%]^& ",
"  %%%%%%%%/(_  ",
"  %%%%%%%%:,<  ",
"  %%%%%%%%[;%  ",
"  %%%%%%%>,}%  ",
"   %%%%%%|1!%  ",
"   %%%%%2,3%   ",
"   %%%%%*,4%   ",
"   %%%%:,)%%   ",
"    %%56,7%%   ",
"    %%8,;9%%   ",
"    %0,1a%%b   ",
"    },,}%%%    ",
"     ;d%%%     "};
"""
			
class Tool():
	def __init__(self):
		self.createToolUi = FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + "/resources/ui/tool.ui")
		
		self.straightToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/straightBitPic.png")				
		self.taperedToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/taperedBitPic.png")				
		self.conicalToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/conicalBitPic.png")				
		self.ballToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/ballBitPic.png")				
		self.taperedBallToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/taperedBallBitPic.png")	
					
		self.createToolUi.buttonBox.accepted.connect(self.accept)
		self.createToolUi.buttonBox.rejected.connect(self.reject)
		
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
		obj = FreeCAD.ActiveDocument.addObject('Part::FeaturePython', "Tool")
		i = self.createToolUi.toolTypeCB.currentIndex()
		obj.addProperty("App::PropertyString","ObjectType")
		if i == 1:
			ViewStraightTool(obj.ViewObject)
			obj.ObjectType = "StraightTool"
		elif i == 2:
			ViewTaperedTool(obj.ViewObject)
			obj.ObjectType = "TaperedTool"
		elif i == 3:
			ViewConicalTool(obj.ViewObject)
			obj.ObjectType = "ConicalTool"
		elif i == 4:
			ViewBallTool(obj.ViewObject)
			obj.ObjectType = "BallTool"
		elif i == 5:
			ViewTaperedBallTool(obj.ViewObject)
			obj.ObjectType = "TaperedBallTool"
		else:
			ViewTool(obj.ViewObject)
			obj.ObjectType = "Tool"
		obj.setEditorMode("ObjectType",("ReadOnly",))
		self.ToolTable.addObject(obj)
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
			if obj.ObjectType == "ToolTable": 
				numberOfInstances += 1
				self.ToolTable = obj
		if numberOfInstances != 1: return False
		return True

FreeCADGui.addCommand('New_Tool',Tool())
