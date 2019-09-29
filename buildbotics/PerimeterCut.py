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

class ViewPerimeterCut(ViewCut):
	def getIcon(self):
		return """
/* XPM */
static char * perimeter_xpm[] = {
"25 24 57 1",
" 	c None",
".	c #000000",
"+	c #000100",
"@	c #007100",
"#	c #007B00",
"$	c #00A000",
"%	c #00A900",
"&	c #00B500",
"*	c #00CB00",
"=	c #00CF00",
"-	c #00E500",
";	c #00E600",
">	c #008D00",
",	c #00BE00",
"'	c #00E100",
")	c #00F300",
"!	c #00FE00",
"~	c #00F700",
"{	c #004C00",
"]	c #003300",
"^	c #00B000",
"/	c #00F200",
"(	c #00B100",
"_	c #006100",
":	c #00E900",
"<	c #00EB00",
"[	c #002F00",
"}	c #002B00",
"|	c #008500",
"1	c #00A300",
"2	c #00C900",
"3	c #00F000",
"4	c #003800",
"5	c #008F00",
"6	c #00F900",
"7	c #007D00",
"8	c #00F500",
"9	c #00BC00",
"0	c #00DE00",
"a	c #005000",
"b	c #002D00",
"c	c #00CC00",
"d	c #00ED00",
"e	c #00C000",
"f	c #00FD00",
"g	c #00D300",
"h	c #008800",
"i	c #00AD00",
"j	c #006B00",
"k	c #00FA00",
"l	c #004A00",
"m	c #00DD00",
"n	c #00BD00",
"o	c #008C00",
"p	c #00DC00",
"q	c #00C300",
"r	c #004000",
"              .......... ",
"        .................",
"     ......+@#$%&**=-;#..",
"   ....>,')!!!!!!!!!!~{. ",
"  ..]^/!!!!!!!!!!!!!!(.. ",
" .._:!!!!!!!!!!!!!!!<[.  ",
"..}<!!!!!!!!!!!!!!!!|..  ",
"..1!!!!!!!!!!!!!!!!2..   ",
"..*!!!!!!!!!!!!!!!34..   ",
"..*!!!!!!!!!!!!!!!5..    ",
"..#6!!!!!!!!!!!!!)_..    ",
" ..73!!!!!!!!!!!!!85..   ",
"  .._:!!!!!!!!!!!!!!9... ",
"   ..4'!!!!!!!!!!!!!!0a..",
"    ..bc!!!!!!!!!!!!!!d..",
"     ...e!!!!!!!!!!!!!;..",
"      ...%f!!!!!!!!!!!g..",
"        ..h6!!!!!!!!!!i..",
"         ..j3!!!!!!!!ka. ",
"          ..lm!!!!!!!n.. ",
"           ...op!!!!q... ",
"             ...r##a...  ",
"              ........   ",
"                ....     "};
"""

class PerimeterCut(Cut):	
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			print prop[1]
			print prop[2]
			print '\n'
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName
		ViewPerimeterCut(obj.ViewObject)
		for prop in obj.PropertiesList:
			obj.setEditorMode(prop,("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
		
	def run(self, ui, obj, outputUnits,fp):
		self.parent = obj.getParentGroup()
		self.fp = fp
		self.ui = ui
		self.outputUnits = outputUnits
		out = self.writeGCodeLine
		cut = self.cut
		self.updateActionLabel("Running Perimeter Cut")
		print "running perimeter cut"
