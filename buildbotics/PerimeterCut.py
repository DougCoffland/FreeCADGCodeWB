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
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName
		ViewPerimeterCut(obj.ViewObject)
		for prop in obj.PropertiesList:
			obj.setEditorMode(prop,("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
		
	def run(self, ui, obj, outputUnits,fp):
		self.obj = obj
		self.parent = obj.getParentGroup()
		self.fp = fp
		self.ui = ui
		self.outputUnits = outputUnits
		self.error = obj.MaximumError.Value
		self.cuttingDirection = None
		out = self.writeGCodeLine
		self.updateActionLabel("Running " + obj.CutName)
		self.safeHeight = obj.SafeHeight.Value
		tool = str(obj.ToolNumber)
		rapid = self.rapid
		cut = self.cut
		self.setBitWidth(obj)
		out("(Starting " + obj.CutName + ')')
		self.setUserUnits()
		self.setOffset(self.parent.XOriginValue.Value, self.parent.YOriginValue.Value, self.parent.ZOriginValue.Value)
		self.updateActionLabel("Setting feeds and speeds for " + obj.CutName)

		rapid(z=obj.ZToolChangeLocation.Value)
		rapid(obj.XToolChangeLocation.Value,obj.YToolChangeLocation.Value)
		out('T' + tool + 'M6')
		out('S' + str(obj.SpindleSpeed).split()[0])
		
		self.updateActionLabel("Getting Boundaries for " + obj.CutName)
		polys = self.getPolysAtSlice(obj.ObjectToCut,"XY",self.parent.ZOriginValue.Value - obj.Depth.Value)
		polys = self.moveOrigin2D(polys)
		polyList =[]
		offset = 0
		self.updateActionLabel("Getting offset polygons for " + obj.CutName)
		while offset < obj.WidthOfCut.Value:
			offset = offset + obj.StepOver.Value
			if  offset >= obj.WidthOfCut.Value: offset = obj.WidthOfCut.Value
			offsetPolys = self.getOffset(polys,offset)
			for poly in offsetPolys: polyList.append(poly)
		self.updateActionLabel("Generating cuts for " + obj.CutName)
		currentDepth = obj.StartHeight.Value
		while currentDepth >= -obj.Depth.Value:
			currentList = polyList[:]
			while len(currentList) > 0:
				self.rapid(z=self.safeHeight)
				if obj.Side == "Inside":
					poly = self.shortestPoly(currentList)
					self.rapid(poly[0][0],poly[0][1])
					self.cut(z=currentDepth)
					area = self.areaOfPoly(poly)
					reducedPoly = self.smoothePoly(poly)
					if obj.MillingMethod == "Climb": self.cutPolyInsideClimb(reducedPoly)
					else: self.cutPolyInsideConventional(reducedPoly)
					currentList.remove(poly)
					poly = self.nextPoly(poly[0][0],poly[0][1],currentList,self.bitWidth)
					while poly != None:
						length = self.lengthOfPoly(poly)
						lengthTimesWidth = length * obj.StepOver.Value
						if self.areaOfPoly(poly) - lengthTimesWidth > area: break
						reducedPoly = self.smoothePoly(poly)
						if obj.MillingMethod == "Climb": self.cutPolyInsideClimb(reducedPoly)
						else: self.cutPolyInsideConventional(reducedPoly)
						area = self.areaOfPoly(poly)
						currentList.remove(poly)
						poly = self.nextPoly(poly[0][0],poly[0][1],currentList,self.bitWidth)
				else:
					poly = self.longestPoly(currentList)
					self.rapid(poly[0][0],poly[0][1])
					self.cut(z=currentDepth)
					area = self.areaOfPoly(poly)
					length = self.lengthOfPoly(poly)
					lengthTimesWidth = length * obj.StepOver.Value
					
					reducedPoly = self.smoothePoly(poly)
					
					if obj.MillingMethod == "Climb": self.cutPolyOutsideClimb(reducedPoly)
					else: self.cutPolyOutsideConventional(reducedPoly)
					currentList.remove(poly)
					poly = self.nextPoly(poly[0][0],poly[0][1],currentList,self.bitWidth)
					while poly != None:
						if area - lengthTimesWidth > self.areaOfPoly(poly): break
						reducedPoly = self.smoothePoly(poly)
						if obj.MillingMethod == "Climb": self.cutPolyOutsideClimb(reducedPoly)
						else: self.cutPolyOutsideConventional(reducedPoly)
						area = self.areaOfPoly(poly)
						currentList.remove(poly)
						poly = self.nextPoly(poly[0][0],poly[0][1],currentList,self.bitWidth)
					
			if currentDepth == -obj.DepthOfCut.Value: break
			if currentDepth - obj.StepDown.Value <= -obj.DepthOfCut.Value: currentDepth = -obj.DepthOfCut.Value
			else: currentDepth = currentDepth - obj.StepDown.Value
		self.rapid(z = self.safeHeight)
			
