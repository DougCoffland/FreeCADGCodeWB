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

class ViewToolTable:
	def __init__(self,obj):
		obj.Proxy = self
		
	def attach(self,obj):
		return
		
	def getDefaultDisplayMode(self):
		return 'Shaded'
		
	def getIcon(self):
		return """
           /* XPM */
static char * tooltable_xpm[] = {
"25 25 124 2",
"  	c None",
". 	c #A0A0A0",
"+ 	c #A1A1A1",
"@ 	c #9F9F9F",
"# 	c #9A9A9A",
"$ 	c #868686",
"% 	c #7D7D7D",
"& 	c #717171",
"* 	c #8F8F8F",
"= 	c #6D6D6D",
"- 	c #5B5B5B",
"; 	c #5E5E5E",
"> 	c #7B7B7B",
", 	c #646464",
"' 	c #666666",
") 	c #797979",
"! 	c #7C7C7C",
"~ 	c #7A7A7A",
"{ 	c #949494",
"] 	c #808080",
"^ 	c #31312F",
"/ 	c #909090",
"( 	c #212120",
"_ 	c #080808",
": 	c #828282",
"< 	c #40403F",
"[ 	c #0C0C0C",
"} 	c #4A4A4A",
"| 	c #848484",
"1 	c #0A0A09",
"2 	c #0D0D0D",
"3 	c #747474",
"4 	c #414141",
"5 	c #0A0A0A",
"6 	c #10100F",
"7 	c #050505",
"8 	c #020202",
"9 	c #353534",
"0 	c #616161",
"a 	c #5B5B59",
"b 	c #585855",
"c 	c #525252",
"d 	c #5C5C5B",
"e 	c #3E3E3C",
"f 	c #4F4F4C",
"g 	c #474746",
"h 	c #545452",
"i 	c #595956",
"j 	c #42423F",
"k 	c #0E0E0D",
"l 	c #393937",
"m 	c #2D2D2C",
"n 	c #6C6C6C",
"o 	c #3F3F3E",
"p 	c #3C3C3A",
"q 	c #767675",
"r 	c #575756",
"s 	c #444442",
"t 	c #555555",
"u 	c #696968",
"v 	c #333332",
"w 	c #373735",
"x 	c #7B7B7A",
"y 	c #5E5E5D",
"z 	c #434340",
"A 	c #363635",
"B 	c #0D0D0C",
"C 	c #0E0E0E",
"D 	c #565653",
"E 	c #1F1F1E",
"F 	c #393938",
"G 	c #313130",
"H 	c #2C2C2B",
"I 	c #4A4A48",
"J 	c #242422",
"K 	c #151514",
"L 	c #2B2B2A",
"M 	c #4A4A47",
"N 	c #161616",
"O 	c #1B1B1A",
"P 	c #262625",
"Q 	c #0B0B0B",
"R 	c #444441",
"S 	c #4E4E4C",
"T 	c #41413F",
"U 	c #50504D",
"V 	c #52524F",
"W 	c #575754",
"X 	c #222222",
"Y 	c #040404",
"Z 	c #090909",
"` 	c #141413",
" .	c #0F0F0E",
"..	c #141414",
"+.	c #101010",
"@.	c #0B0B0A",
"#.	c #151515",
"$.	c #1B1B1B",
"%.	c #4C4C4C",
"&.	c #929292",
"*.	c #979797",
"=.	c #939393",
"-.	c #8E8E8E",
";.	c #707070",
">.	c #6A6A6A",
",.	c #5F5F5F",
"'.	c #696969",
").	c #737373",
"!.	c #606060",
"~.	c #787878",
"{.	c #8D8D8D",
"].	c #969696",
"^.	c #898989",
"/.	c #999999",
"(.	c #7F7F7F",
"_.	c #767676",
":.	c #8B8B8B",
"<.	c #6E6E6E",
"[.	c #5A5A5A",
"}.	c #626262",
"|.	c #6B6B6B",
"1.	c #777777",
"2.	c #989898",
"3.	c #9E9E9E",
"                                                  ",
"              .     .       .     .               ",
"              .     .       +     .               ",
"              .     .       +     .               ",
"              .     @       .     #               ",
"              $     %     & *     =               ",
"              -     ;     > ,     '               ",
"              )     $ !   + ~     { ]             ",
"            ^ / ( _ : < [ } | 1 2 3 4 5 [ 6 7 8   ",
"          [ 9 0 a b ; c b d ' e f ; g h i j k     ",
"        [ l m n o p q r s t u v w x y z A B       ",
"      C z D E F G e H ( I J K L M N O P Q         ",
"    [ R i i S T D i U V i i i i i W X             ",
"  Y 5 5 5 Q Z `  .B ..+.@.#...5 Q $.%.            ",
"              &.    *.      =.    -.              ",
"              ;.    >.    ;.!     0               ",
"              ,.    '.).    !.    ~.&             ",
"              {.    ].)     ^.    /.              ",
"              (.    !     _.:.    <.              ",
"              [.    }.      ,.    |.&             ",
"              ]     :.;.    1.    2.3             ",
"              .     .       3.    .               ",
"              .     .       @     +               ",
"                                                  ",
"                                                  "};
		"""
		

class ToolTable():
	def __init__(self):
		self.createTTUi =  FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + "/resources/ui/tooltable.ui")
		self.createTTUi.buttonBox.accepted.connect(self.accept)
		self.createTTUi.buttonBox.rejected.connect(self.reject)

	def GetResources(self):
		return {'Pixmap'  : os.path.dirname(__file__) +  "/resources/svg/tooltable.svg", # the name of a svg file available in the resources
                'MenuText': "New Tool Table",
                'ToolTip' : "Sets up a new tool table that an be used for creating G-Code paths from FreeCAD Shapes"}

	def Activated(self):        
		self.createTTUi.show()       
		return
        
	def accept(self):
		self.createTTUi.hide()
		obj = FreeCAD.ActiveDocument.addObject('App::DocumentObjectGroupPython', "ToolTable")
		ViewToolTable(obj.ViewObject)
		obj.addProperty("App::PropertyString","ObjectType")
		obj.ObjectType = "ToolTable"
		obj.setEditorMode("ObjectType",("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
		return True
		
	def reject(self):
		self.createTTUi.hide()
		return False

	def IsActive(self):
		"""Here you can define if the command must be active or not (greyed) if certain conditions
		are met or not. This function is optional."""
		return True

FreeCADGui.addCommand('New_Tooltable',ToolTable())
