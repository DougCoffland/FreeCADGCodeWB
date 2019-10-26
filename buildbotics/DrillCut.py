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
from pivy import coin
import os
from Cut import Cut, ViewCut
import validator as VAL

class ViewDrillCut(ViewCut):
	def getIcon(self):
		return """
/* XPM */
static char * drill_xpm[] = {
"25 20 44 1",
" 	c None",
".	c #000000",
"+	c #716100",
"@	c #AB9400",
"#	c #B49D00",
"$	c #C3A900",
"%	c #AE9700",
"&	c #816F00",
"*	c #AD9600",
"=	c #D7BB00",
"-	c #BEA500",
";	c #706000",
">	c #C2A900",
",	c #5D5000",
"'	c #675900",
")	c #B59D00",
"!	c #CBB100",
"~	c #423800",
"{	c #A58F00",
"]	c #D3B800",
"^	c #A18C00",
"/	c #2E2700",
"(	c #272828",
"_	c #B9BDBE",
":	c #BCC0C1",
"<	c #AAADAE",
"[	c #707273",
"}	c #868989",
"|	c #989B9C",
"1	c #444546",
"2	c #B5B9BA",
"3	c #A7ABAC",
"4	c #606263",
"5	c #7F8283",
"6	c #8C8F90",
"7	c #3A3C3C",
"8	c #AFB3B4",
"9	c #B2B6B6",
"0	c #474949",
"a	c #393A3A",
"b	c #AAAEAF",
"c	c #A5A8A9",
"d	c #999C9D",
"e	c #393A3B",
" ...........             ",
".+@#$$$$$%@&..           ",
".*==========-;.          ",
".>============, ....     ",
".$============'    .     ",
".$============'    ......",
".$============'   ..     ",
".)===========!~ ...      ",
".{=========]^/.          ",
" ............            ",
"   ......                ",
"   (_::<. ..             ",
"  .[:::}....             ",
"  .|:::1 ..              ",
"  .2::3....              ",
" .4:::5.                 ",
" .6:::7                  ",
" .8::90.                 ",
" abbbcde                 ",
"........                 "};
"""

class DrillCut(Cut):	
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName
		ViewDrillCut(obj.ViewObject)
		for prop in obj.PropertiesList:
			obj.setEditorMode(prop,("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
				
	def drill(self,x,y,zed,safeHeight,peckDepth):
		self.rapid(z=safeHeight)
		self.rapid(x,y)
		depth = 0
		while depth + peckDepth < zed:
			depth = depth + peckDepth
			self.cut(z=-depth)
			self.rapid(z=safeHeight)
		self.cut(z = -zed)
		
	def run(self, ui, obj, outputUnits,fp):
		self.obj = obj
		self.parent = obj.getParentGroup()
		self.fp = fp
		self.ui = ui
		out = self.writeGCodeLine
		self.outputUnits = outputUnits
		safeHeight = obj.SafeHeight.Value
		tool = str(obj.ToolNumber)
		rapid = self.rapid
		out("(Starting " + obj.CutName + ')')
		self.setUserUnits()

		rapid(z=obj.ZToolChangeLocation.Value)
		rapid(obj.XToolChangeLocation.Value,obj.YToolChangeLocation.Value)
		out('T' + tool + 'M6')
		for point in obj.DrillPointList:
			x = point[0]
			y = point[1]
			z = point[2]
			s = obj.SafeHeight.Value
			p = obj.PeckDepth.Value
			self.drill(x,y,z,s,p)
		rapid(z=safeHeight)
		
