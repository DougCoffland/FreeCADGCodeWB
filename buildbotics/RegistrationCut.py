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
from pivy import coin
import os
from Cut import Cut, ViewCut

class ViewRegistrationCut(ViewCut):
	def getIcon(self):
		return """
/* XPM */
static char * registration_xpm[] = {
"25 25 20 1",
" 	c None",
".	c #170017",
"+	c #3A003A",
"@	c #7F007F",
"#	c #700070",
"$	c #720072",
"%	c #7C007C",
"&	c #7B007B",
"*	c #000000",
"=	c #100010",
"-	c #0A000A",
";	c #710071",
">	c #7E007E",
",	c #790079",
"'	c #740074",
")	c #7D007D",
"!	c #230023",
"~	c #520052",
"{	c #6F006F",
"]	c #180018",
"           .+.           ",
"           +@+           ",
"           +@+           ",
"           +@+           ",
"           .+.           ",
"           #$#           ",
"           %@%           ",
"           &@&           ",
"            @            ",
"            @            ",
"            &            ",
"***=-;&           >,.+++.",
"+@@@+'@@@@)   %@@@@@+@@@+",
"!~~~!'>>         ))@.+++.",
"            &            ",
"            @            ",
"            @            ",
"            @&           ",
"           %@%           ",
"           #${           ",
"           ]+.           ",
"           +@+           ",
"           +@+           ",
"           +@+           ",
"           .+.           "};"""

class RegistrationCut(Cut):	
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName
		ViewRegistrationCut(obj.ViewObject)
		for prop in obj.PropertiesList:
			obj.setEditorMode(prop,("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
		
	def setParameters(self,ui, obj, outputUnits,fp):
		self.setCommonProperties(ui, obj, outputUnits,fp)
		self.out = self.writeGCodeLine
		self.cuttingDirection = None

	def drill(self,x,y,safeHeight,drillDepth,peckDepth):
		self.rapid(z=safeHeight)
		self.rapid(x,y)
		depth = 0
		while depth + peckDepth < drillDepth:
			depth = depth + peckDepth
			self.cut(z=-depth)
			self.rapid(z=safeHeight)
		self.cut(z=-drillDepth)
				
	def run(self, ui, obj, outputUnits, fp):
		self.setParameters(ui, obj, outputUnits, fp)
		self.out("(Starting " + obj.CutName + ')')
		self.changeTool()
		self.out('M3 S' + self.speed)
		self.drill(obj.FirstX.Value,obj.FirstY.Value,self.safeHeight,obj.DrillDepth.Value,obj.PeckDepth.Value)
		self.drill(obj.SecondX.Value,obj.SecondY.Value,self.safeHeight,obj.DrillDepth.Value,obj.PeckDepth.Value)
		self.rapid(z=self.safeHeight)
		

