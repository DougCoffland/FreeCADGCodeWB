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

class ViewFaceCut(ViewCut):
	def getIcon(self):
		return """
/* XPM */
static char * face_xpm[] = {
"25 25 132 2",
"  	c None",
". 	c #000000",
"+ 	c #191100",
"@ 	c #584300",
"# 	c #785C00",
"$ 	c #856600",
"% 	c #896A00",
"& 	c #785D00",
"* 	c #1E1500",
"= 	c #574200",
"- 	c #997700",
"; 	c #B78E00",
"> 	c #BC9200",
", 	c #B88F00",
"' 	c #9E7A00",
") 	c #685000",
"! 	c #0E0800",
"~ 	c #8E6E00",
"{ 	c #BB9100",
"] 	c #9F7B00",
"^ 	c #2A1F00",
"/ 	c #A57F00",
"( 	c #181000",
"_ 	c #B18A00",
": 	c #856700",
"< 	c #382A00",
"[ 	c #B88E00",
"} 	c #3B2C00",
"| 	c #5D4700",
"1 	c #BB9200",
"2 	c #957300",
"3 	c #4B4A48",
"4 	c #51493B",
"5 	c #8A6A00",
"6 	c #947200",
"7 	c #7D6000",
"8 	c #765B01",
"9 	c #556C81",
"0 	c #718FAA",
"a 	c #617B93",
"b 	c #544628",
"c 	c #705601",
"d 	c #69849E",
"e 	c #81A2C1",
"f 	c #80A1C0",
"g 	c #576E83",
"h 	c #917000",
"i 	c #BA9100",
"j 	c #8E6D00",
"k 	c #AE8700",
"l 	c #485C6E",
"m 	c #5F778F",
"n 	c #3F454A",
"o 	c #7998B6",
"p 	c #634B00",
"q 	c #795D00",
"r 	c #AB8400",
"s 	c #51677B",
"t 	c #668099",
"u 	c #8D6D00",
"v 	c #4E432D",
"w 	c #7E9EBC",
"x 	c #7390AC",
"y 	c #735900",
"z 	c #9A7700",
"A 	c #AD8600",
"B 	c #B99000",
"C 	c #4E4431",
"D 	c #6D89A3",
"E 	c #7E9EBD",
"F 	c #7594B0",
"G 	c #424F5C",
"H 	c #AC8500",
"I 	c #9D7A00",
"J 	c #424951",
"K 	c #5D758C",
"L 	c #5B738A",
"M 	c #474540",
"N 	c #AB8500",
"O 	c #B18900",
"P 	c #050300",
"Q 	c #B38B00",
"R 	c #846600",
"S 	c #604901",
"T 	c #755A00",
"U 	c #A68000",
"V 	c #B68D00",
"W 	c #A07C00",
"X 	c #A37E00",
"Y 	c #423200",
"Z 	c #5A4500",
"` 	c #5C4600",
" .	c #725700",
"..	c #6C5300",
"+.	c #634C00",
"@.	c #A78100",
"#.	c #927100",
"$.	c #1C1400",
"%.	c #AF8800",
"&.	c #0D0800",
"*.	c #745900",
"=.	c #A78200",
"-.	c #AA8400",
";.	c #6E5400",
">.	c #614A00",
",.	c #7D6100",
"'.	c #221800",
").	c #150F00",
"!.	c #1D1500",
"~.	c #211700",
"{.	c #866700",
"].	c #BA9000",
"^.	c #453400",
"/.	c #5B4500",
"(.	c #B58D00",
"_.	c #977500",
":.	c #826400",
"<.	c #B48C00",
"[.	c #967400",
"}.	c #3E2E00",
"|.	c #140D00",
"1.	c #735800",
"2.	c #070400",
"3.	c #6B5200",
"4.	c #B28A00",
"5.	c #2E2200",
"6.	c #644D00",
"7.	c #816400",
"8.	c #896900",
"9.	c #7E6100",
"0.	c #564100",
"a.	c #060400",
"              . . . . . . . . .                   ",
"          . . + @ # $ % $ & @ * . .               ",
"      . . = - ; > > > > > > > , ' ) . .           ",
"    . ! ~ { > > > > > > > > > > > > ] ^ .         ",
"    . % > > > > > > > > > > > > > > > / ( .       ",
"  . . _ > > > > > > > > > > > > > > > > : .       ",
"  . < > > > > > > > > > > > > > > > > > [ } .     ",
"  . | > > > 1 ' % 2 , > > > [ # 3 4 5 { > 6 .     ",
"  . 7 > > > 8 9 0 a b , > > c d e f g h > i } .   ",
"  . j > > k l e e e m 2 > > n e e e o p > > q .   ",
"  . ] > > r s e e e t u > > v w e e x y > > z .   ",
"  . A > > B C D E F G H > > I J K L M N > > O . . ",
". P , > > > Q R S T U > > > > V W X , > > > > < . ",
". Y > > > > > > > > > > > > > > > > > > > > > Z . ",
". ` > > > > > > > > > > > > > > > > > > > > >  .. ",
". & > > > > > > > > > > > > > > > > > > > > > 7 . ",
". ..> > > > > Q +.@.> > > > > > #..., > > > > 7 . ",
". $.%.> > > > @.} &.*.=.{ > -.;.. >.; > > > > ... ",
"  . = , > > > > V ,.'.. ).!.. ~.{.].> > > > > ^.. ",
"    . /.Q > > > > > (._.R :.6 <.> > > > > > [..   ",
"      . }.W > > > > > > > > > > > > > > > 6 |..   ",
"        . . ..H > > > > > > > > > > > <.1.. .     ",
"            . 2.3.' B > > > > > > 4.$ 5.. .       ",
"              . . . ^ 6.7.{.8.9.0.a.. .           ",
"                    . . . . . . .                 "};
"""

class FaceCut(Cut):	
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName		
		ViewFaceCut(obj.ViewObject)
		for prop in obj.PropertiesList:
			obj.setEditorMode(prop,("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
		
	def runZigZag(self):
		pass
		
	def runCircular(self,obj):
		offset = -self.bitWidth/2
		self.updateActionLabel("Getting Boundaries")
		polys = self.getBoundaries(obj.CutArea, self.getOrigin(obj),obj.Depth.Value)
		self.updateActionLabel("Getting Offsets")
		offsetPolys = self.getOffset(polys, offset)
		polyList = offsetPolys
		while len(offsetPolys) > 0:
			offset = offset - obj.StepOver.Value
			offsetPolys = self.getOffset(polys, offset)
			polyList = polyList + offsetPolys
		currentDepth = obj.StartHeight.Value
		while currentDepth >= -obj.Depth.Value:
			self.updateActionLabel("Writing G-code for z = " + str(currentDepth))
			currentList = polyList[:]
			while len(currentList) > 0:
				poly = self.shortestPoly(currentList)
				outerArea = self.areaOfPoly(poly)
				outerLength = self.lengthOfPoly(poly)
				lengthTimesWidth = outerLength * obj.StepOver.Value
				self.rapid(z=self.safeHeight)
				self.rapid(poly[0][0],poly[0][1])
				self.cut(z=currentDepth)
				if obj.MillingMethod != "Climb": self.cutPolyInsideClimb(poly)
				else: self.cutPolyInsideConventional(poly)
				currentList.remove(poly)
				poly = self.nextPoly(poly[0][0],poly[0][1],currentList,self.bitWidth)
				while poly != None:
					if outerArea - lengthTimesWidth > self.areaOfPoly(poly): break
					if obj.MillingMethod != "Climb": self.cutPolyInsideClimb(poly)
					else: self.cutPolyInsideConventional(poly)
					outerArea = self.areaOfPoly(poly)
					outerLength = self.lengthOfPoly(poly)
					lengthTimesWidth = outerLength * obj.StepOver.Value
					currentList.remove(poly)
					poly = self.nextPoly(poly[0][0],poly[0][1],currentList,self.bitWidth)
			if currentDepth == -obj.Depth.Value: break
			if currentDepth - obj.StepDown.Value <= -obj.Depth.Value: currentDepth = -obj.Depth.Value
			else: currentDepth = currentDepth - obj.StepDown.Value
			
		self.rapid(z = self.safeHeight)
	
	def runCircularOld(self,obj):
		offset = -self.bitWidth/2
		self.updateActionLabel("Getting Boundaries at offset: " + str(offset))
		polys = self.getBoundaries(obj.CutArea, self.getOrigin(obj),obj.Depth.Value)
		offsetPolys = self.getOffset(polys, offset)
		polyList = offsetPolys
		while len(offsetPolys) > 0:
			self.updateActionLabel("Writing G-Code Cuts for offset: " + str(offset))
			for poly in offsetPolys:
				self.rapid(z=self.safeHeight)
				if obj.MillingMethod == "Climb":
					i = len(poly) - 1
					self.rapid(poly[i][0],poly[i][1])
					self.cut(z=-obj.Depth.Value)
					i = i-1
					while (i >= 0):
						self.cut(poly[i][0],poly[i][1])
						i = i - 1
				else:
					self.rapid(poly[0][0],poly[0][1])
					self.cut(z=-obj.Depth.Value)
					i = 1
					while i < len(poly):
						self.cut(poly[i][0],poly[i][1])
						i = i + 1
			self.rapid(z = self.safeHeight)
			offset = offset - self.bitWidth/2
			offsetPolys = self.getOffset(polys, offset)
			polyList = polyList + offsetPolys
		print str(len(polyList)) + " polys"
		
	def run(self, ui, obj, outputUnits, fp):		
		self.parent = obj.getParentGroup()
		self.fp = fp
		self.ui = ui
		self.outputUnits = outputUnits
		out = self.writeGCodeLine
		self.safeHeight = obj.SafeHeight.Value
		tool = str(obj.ToolNumber)
		rapid = self.rapid
		cut = self.cut
		self.setBitWidth(obj)
		out("(Starting " + obj.CutName + ')')
		self.setUserUnits()
		self.setOffset(self.parent.XOriginValue.Value, self.parent.YOriginValue.Value, self.parent.ZOriginValue.Value)
		self.updateActionLabel("Setting feeds and speeds")
		out('F' + str(self.toOutputUnits(obj.FeedRate,'velocity')))
		rapid(z=obj.ZToolChangeLocation.Value)
		rapid(obj.XToolChangeLocation.Value,obj.YToolChangeLocation.Value)
		out('T' + tool + 'M6')
		out('S' + str(obj.SpindleSpeed).split()[0])
		if obj.FacingPattern == "Circular": self.runCircular(obj)
		elif obj.FacingPattern == "Zig Zag": self.runZigZag()
		rapid(z=self.safeHeight)
		self.updateActionLabel("Cut completed")

