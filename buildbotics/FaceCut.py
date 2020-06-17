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
import validator as VAL
import math

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
		
	def getBoundBox(self,polys):
		xMin = xMax = polys[0][0][0]
		yMin = yMax = polys[0][0][1]
		for poly in polys:
			for p in poly:
				if p[0] < xMin: xMin = p[0]
				if p[0] > xMax: xMax = p[0]
				if p[1] < yMin: yMin = p[1]
				if p[1] > yMax: yMax = p[1]
		return xMin,xMax,yMin,yMax
		
	def orientation(self,p,q,r):
		xp,yp = p
		xq,yq = q
		xr,yr = r
		val = (yq - yp) * (xr - xq) - (xq - xp) * (yr - yq)
		if val == 0: return 0
		elif val > 0: return 1
		return 2
		
	def onSegment(self,p,q,r):
		xp,yp = p
		xq,yq = q
		xr,yr = r
		if xq <= max(xp, xr) and xq >= min(xp,xr) and yq <= max(yp,yr) and yq >= min(yp,yr): return True
		return False
		
	def intersects(self,p1,q1,p2,q2):
		o1 = self.orientation(p1,q1,p2)
		o2 = self.orientation(p1,q1,q2)
		o3 = self.orientation(p2,q2,p1)
		o4 = self.orientation(p2,q2,q1)
		if (o1 != o2 and o3 != o4): return True
		if o1 == 0 and self.onSegment(p1,p2,q1): return True
		if o2 == 0 and self.onSegment(p1,q2,q1): return True
		if o3 == 0 and self.onSegment(p2,p1,q2): return True
		if o4 == 0 and self.onSegment(p2,q1,q2): return True
		return False
		
	def getIntersections(self,seg,polys):
		polySegs = []
		for poly in polys:
			i = 0
			while i < len(poly) -1:
				if self.intersects(seg[0],seg[1],poly[i],poly[i+1]) == True:
					polySegs.append([poly[i],poly[i+1]])
				i = i + 1
			if self.intersects(seg[0],seg[1],poly[i],poly[0]) == True:
				polySegs.append([poly[i],poly[0]])
		return polySegs
	
	def getSegDirection(self,seg):
		x1,y1 = seg[0]
		x2,y2 = seg[1]
		if x1 == x2:
			if y1 >= y2: a = -math.pi/2
			else: a = math.pi/2
		else:
			a = math.atan((y2-y1)/(x2-x1))
		return a
		
	def getIntersectingPoint(self,seg,polySeg):
		a_s = self.getDirection(seg)
		a_p = self.getDirection(polySeg)
		
	def getPointsOfInterest(self,seg,polySegs):
		pointDataList = []
		m0 = self.getSegDirection(seg)
		for polySeg in polySegs:
			m1 = self.getSegDirection(polySeg)
			if m1 == m0 or m1 == -m0:
				pointDataList.append({"type": "ON_SEG", "point": polySeg[0], "otherPoint": polySeg[1], "angle": m1})
			else:
				x1,y1 = seg[0]
				x2,y2 = seg[1]
				x3,y3 = polySeg[0]
				x4,y4 = polySeg[1]
				d = (x4 - x3)*(y1 - y2) - (x1 - x2)*(y4 - y3)
				if d == 0.:
					print "Error: getPointsOfInterest: divide by zero"
					return
				t = ((y3 - y4)*(x1 - x3) + (x4 - x3)*(y1 - y3))/d
				p = (x1 + t * (x2 - x1),y1 + t * (y2 - y1))
				if p == polySeg[0] or p == polySeg[1]:
					if p == polySeg[0]: p2 == polySeg[1]
					else: p2 = polySeg[0]
					pointDataList.append({"type": "END", "point": p, "otherPoint": p2,  "angle": m1})
				else:
					pointDataList.append({"type": "CROSS_POINT", "point": p})
		return pointDataList
		
	def getConnectingSeg(self, segs, p):
		i = 0
		while i < len(segs):
			if seg[i][0] == p or seg[i][1] == p: return i
			i = i + 1
		
	def getNearestPoint(self,p,pList):
		i = 0
		closestDistance = None
		index = None
		x1,y1 = p
		while i < len(pList):
			x2,y2 = pList[i]["point"]
			d = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
			if closestDistance == None:	
				closestDistance = d
				index = i
			elif d < closestDistance:
				closestDistance = d
				index = i
			i = i + 1
		return index
		
	def getNearestCut(self,p,cutList):
		nearestCut = None
		shortestDistance = None
		end = None
		i = 0
		while i < len(cutList):
			x,y = p
			x1,y1 = cutList[i][0]
			d1 = math.sqrt((x1 - x) * (x1 - x) + (y1 - y) * (y1 -y))
			x2,y2 = cutList[i][1]
			d2 = math.sqrt((x2 - x) * (x2 - x) + (y2 - y) * (y2 -y))
			if d1 <= d2: d = d1
			else: d = d2
			if shortestDistance == None or d < shortestDistance:
				shortestDistance = d
				nearestCut = i
				if d1 <= d2: end = "START"
				else: end = "END"
			i = i + 1
			return nearestCut,shortestDistance,end
					
	def cutZigZags(self,obj,cutList,depth):
		if obj.MillingMethod == "Either":
			cut = cutList.pop(0)
			self.rapid(z = obj.SafeHeight.Value)
			self.rapid(cut[0][0],cut[0][1])
			self.cut(z=depth)
			self.cut(cut[1][0],cut[1][1])
			lastPoint = cut[1]
			while len(cutList) > 0:
				nearestCut,shortestDistance,end = self.getNearestCut(lastPoint,cutList)
				cut = cutList.pop(nearestCut)
				if end == "START":
					p1 = cut[0]
					p2 = cut[1]
				else:
					p1 = cut[1]
					p2 = cut[0]
				if shortestDistance >= self.bitWidth * .75:
					self.rapid(z=obj.SafeHeight.Value)
					self.rapid(p1[0],p1[1])
					self.cut(z=depth)
				else:
					self.cut(p1[0],p1[1])
				self.cut(p2[0],p2[1])
				lastPoint = p2
			self.rapid(z=obj.SafeHeight.Value)			
		for cut in cutList:
			self.rapid(z=obj.SafeHeight.Value)
			if obj.MillingMethod == "Climb":
				self.rapid(cut[0][0],cut[0][1])
				self.cut(z=depth)
				self.cut(cut[1][0],cut[1][1])
			elif obj.MillingMethod == "Conventional":
				self.rapid(cut[1][0],cut[1][1])
				self.cut(z=depth)
				self.cut(cut[0][0],cut[0][1])
			self.rapid(z=obj.SafeHeight.Value)				
					
	def getSide(self, seg, p):
		x = p[0]
		y = p[1]
		x1 = seg[0][0]
		y1 = seg[0][1]
		x2 = seg[1][0]
		y2 = seg[1][1]
		d = (x - x1)(y2 - y1) - (y - y2)(x2 - x1)
		if d < 0: return -1
		elif d > 0: return 1
		else: return 0
	
	def runLinear(self, obj, direction, cutPerimeter):
		if direction == "DIAGONAL": self.updateActionLabel("Getting Boundaries for Zig Zag facing")
		elif direction == "ALONGX": self.updateActionLabel("Getting Boundaries for Along X facing")
		else: self.updateActionLabel("Getting Boundaries for Along Y facing")
		polys = self.getPolysAtSlice(obj.CutArea,"XY",self.parent.ZOriginValue.Value - obj.Depth.Value)
		polys = self.moveOrigin2D(polys)
		if len(polys) == 0: return
		root2 = math.sqrt(2)
		xMin,xMax,yMin,yMax = self.getBoundBox(polys)
		x1 = xMin
		y1 = yMin
		x2 = xMin
		y2 = yMin
		segList = []
		if direction == "DIAGONAL":
			xStep = obj.StepOver.Value * root2
			yStep = obj.StepOver.Value * root2
			while x1 < xMax or y1 < yMax:
				if x1 > xMax: x1 = xMax
				if y1 > yMax: y1 = yMax
				segList.append([[x1,y1],[x2,y2]])
				if x1 < xMax:
					x1 = x1 + obj.StepOver.Value * root2
				else:
					y1 = y1 + obj.StepOver.Value * root2
				if y2 < yMax:
					y2 = y2 + obj.StepOver.Value * root2
				else:
					x2 = x2 + obj.StepOver.Value * root2
		elif direction == "ALONGX":
			xStep = 0
			yStep = obj.StepOver.Value
			while y1 < yMax:
				segList.append([[xMin,y1],[xMax,y1]])
				y1 = y1 + yStep		
		else:
			xStep = obj.StepOver.Value
			yStep = 0
			while x1 < xMax:
				segList.append([[x1,yMin],[x1,yMax]])
				x1 = x1 + obj.StepOver.Value
		offsetPolys = self.getOffset(polys,-(self.bitWidth)/2)
		cutList = []
		for seg in segList:
			intersectingPolySegs = self.getIntersections(seg,offsetPolys)
			pointsOfInterest = self.getPointsOfInterest(seg,intersectingPolySegs)
			cutting = False
			cuttingOnSegment = False
			startPoint = None
			endPoint = None
			while len(pointsOfInterest) > 0:
				i = self.getNearestPoint(seg[0],pointsOfInterest)
				p = pointsOfInterest.pop(i)
				if p["type"] == 'CROSS_POINT':
					if cuttingOnSegment == True:
						print "Warning: invalid polygon"
						cuttingOnSegment = False
					if cutting == False:
						startPoint = p['point']
						cutting = True
					else:
						endPoint = p['point']
						cutList.append([startPoint,endPoint])
						cutting = False
						startPoint = None
						endPoint = None
				elif p["type"] == "END_POINT":
					side1 = self.getSide(seg,p["otherPoint"])
					i = self.getConnectingSeg(pointsOfInterest,p["point"])
					p2 = pointsOfInterest.pop(i)
					while p2["type"] == "ON_SEG":
						i = self.getConnectingSeg(pointsOfInterest,p2["otherPoint"])
						p2 = pointsOfInterest.pop(i)
					endPoint = p2["point"]
					side2 = self.getSide(seg,p2["otherPoint"])
					if side1 == side2:
						if cutting == False:
							startPoint = p["point"]
							endPoint = p2["point"]
							cutList.append([startPoint,endPoint])
							startPoint = None
							endPoint = None
					else:
						if cutting == True:
							endPoint = p2
							cutList.append([startPoint,endPoint])
							cutting = False
						else:
							startPoint = p["point"]
							cutting = True
				elif p["type"] == "ON_SEG":
					i = self.getConnectingSeg(pointsOfInterest,p["point"])
					p1 = pointsOfInterest.pop(i)
					side1 = self.getSide(seg,p1["otherPoint"])
					i = self.getConnectingSeg(pointsOfInterest,p["otherPoint"])
					p2 = pointsOfInterest.pop(i)
					while p2["type"] == "ON_SEG":
						i = self.getConnectingSeg(pointsOfInterest,p2["otherPoint"])
						p2 = pointsOfInterest.pop(i)
					endPoint = p2["point"]
					side2 = self.getSide(seg,p2["otherPoint"])
					if side1 == side2:
						if startPoint == endPoint: pass
						elif cutting == False:
							startPoint = p["point"]
							endPoint = p2["point"]
							cutList.append([startPoint,endPoint])
						else: pass
					else:
						if cutting == False:
							startPoint = p["point"]
							cutting = True
						else:
							endPoint = p2["point"]
							cutList.append([startPoint,endPoint])
							startPoint = None
							endPoint = None
							cutting = False								
		depth = obj.StartHeight.Value
		while depth > -obj.Depth.Value:
			if cutPerimeter == True:
				for poly in offsetPolys:
					self.rapid(z=obj.SafeHeight.Value)
					self.rapid(poly[0][0],poly[0][1])
					self.cut(z=depth)
					if obj.MillingMethod == "Conventional":
						self.cutPolyInsideConventional(poly)
					else: self.cutPolyInsideClimb(poly)				
					self.rapid(z=obj.SafeHeight.Value)
			self.cutZigZags(obj,cutList[:],depth)
			depth = depth - obj.StepDown.Value
		if depth + obj.StepDown.Value > -obj.Depth.Value:
			depth = -obj.Depth.Value
			if cutPerimeter == True:
				for poly in offsetPolys:
					self.rapid(z=obj.SafeHeight.Value)
					self.rapid(poly[0][0],poly[0][1])
					self.cut(z=depth)
					if obj.MillingMethod == "Conventional":
						self.cutPolyInsideConventional(poly)
					else: self.cutPolyInsideClimb(poly)				
					self.rapid(z=obj.SafeHeight.Value)
			self.cutZigZags(obj,cutList[:],depth)		
		
	def runCircular(self,obj):
		offset = -self.bitWidth/2
		self.updateActionLabel("Getting Boundaries for circular facing")
		polys = self.getPolysAtSlice(obj.CutArea,"XY",self.parent.ZOriginValue.Value - obj.Depth.Value)
		polys = self.moveOrigin2D(polys)
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

	def run(self, ui, obj, outputUnits, fp):
		self.obj = obj		
		self.parent = obj.getParentGroup()
		self.fp = fp
		self.ui = ui
		self.outputUnits = outputUnits
		out = self.writeGCodeLine
		self.safeHeight = obj.SafeHeight.Value
		self.cuttingDirection = None
		tool = str(obj.ToolNumber)
		rapid = self.rapid
		cut = self.cut
		self.setBitWidth(obj)
		out("(Starting " + obj.CutName + ')')
		self.setUserUnits()
		self.setOffset(self.parent.XOriginValue.Value, self.parent.YOriginValue.Value, self.parent.ZOriginValue.Value)
		self.updateActionLabel("Setting feeds and speeds")

		rapid(z=obj.ZToolChangeLocation.Value)
		rapid(obj.XToolChangeLocation.Value,obj.YToolChangeLocation.Value)
		out('T' + tool + 'M6')
		out('S' + str(obj.SpindleSpeed).split()[0])
		if obj.FacingPattern == "Circular": self.runCircular(obj)
		elif obj.FacingPattern == "Zig Zag": self.runLinear(obj, 'DIAGONAL', False)
		elif obj.FacingPattern == "Perimeter then Zig-Zag": self.runLinear(obj, 'DIAGONAL', True)
		elif obj.FacingPattern == "Along X": self.runLinear(obj, 'ALONGX', False)
		elif obj.FacingPattern == "Perimeter then Along X": self.runLinear(obj, 'ALONGX', True)
		elif obj.FacingPattern == "Along Y": self.runLinear(obj, 'ALONGY', False)
		elif obj.FacingPattern == "Perimeter then Along Y": self.runLinear(obj, 'ALONGY', True)
		rapid(z=self.safeHeight)
		self.updateActionLabel("Cut completed")
