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
import math
import Mesh, MeshPart, Part
from FreeCAD import Base
import pyclipper

class ViewCut:
	def __init__(self,obj):
		obj.Proxy = self
		
	def attach(self,obj):
		self.ViewObject = obj
		self.Object = obj.Object
		return
		
	def attach(self, vobj):
		self.standard = coin.SoGroup()
		vobj.addDisplayMode(self.standard,"Standard");
		
	def getDisplayModes(self,obj):
		return ["Standard"]
	
	def getDefaultDisplayMode(self):
		return "Standard"
	
	def __getstate__(self):
		return None
		
	def __setstate__(self,state):
		return

	def getIcon(self):
		return ""
					
class Cut:
	def __init__(self,selectedObject):
		obj = FreeCAD.ActiveDocument.addObject('App::FeaturePython', "Cut")
		obj.Proxy = self
		self.obj = obj
		selectedObject.addObject(self.obj)
		self.outputUnits = ""
		self.currentCut = None
		self.ui = None
		self.cuttingDirection = None
		self.error = 0.25
		
	def getObject(self):
		return self.obj
	
	def writeGCodeLine(self,line):
		self.fp.write(line + '\n')
		try:
			lc = int(self.ui.lcL.text())
		except:
			lc = 0
		self.ui.lcL.setText(str(lc + 1))		
		
	def run(self):
		print "overide run program in derived cut type"

	def cut(self,x=None,y=None,z=None):
		obj = self.obj
		line = 'G1'
		if x != None: line = line + 'X' + str(round(self.toOutputUnits(x,'length'),4))
		if y != None: line = line + 'Y' + str(round(self.toOutputUnits(y,'length'),4))
		if z != None: line = line + 'Z' + str(round(self.toOutputUnits(z,'length'),4))
		if x != None or y != None:
			if self.cuttingDirection != "cutting":
				feedString = 'F' + str(self.toOutputUnits(obj.FeedRate,'velocity'))
				self.cuttingDirection = "cutting"
			else: feedString = ""
		else:
			if self.cuttingDirection != "plunging":
				feedString = 'F' + str(self.toOutputUnits(obj.PlungeRate,'velocity'))
				self.cuttingDirection = "plunging"
			else: feedString = ""
		self.writeGCodeLine(line + ' ' + feedString)

	def rapid(self,x=None,y=None,z=None):
		line = 'G0'
		if x != None: line = line + 'X' + str(round(self.toOutputUnits(x,'length'),4))
		if y != None: line = line + 'Y' + str(round(self.toOutputUnits(y,'length'),4))
		if z != None: line = line + 'Z' + str(round(self.toOutputUnits(z,'length'),4))
		self.writeGCodeLine(line)
		
	def cutWire(self,wire):
		self.rapid(z=self.safeHeight)
		self.rapid(wire[0][0],wire[0][1])
		self.cut(z = wire[0][2])
		i = 1
		while i < len(wire):
			x,y,z = wire[i]
			self.cut(x,y,z)
			i = i + 1
		self.rapid(z = self.safeHeight)
		
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName

		ViewCut(obj.ViewObject)

		for prop in obj.PropertiesList:
			obj.setEditorMode(prop,("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
		
	def setUserUnits(self):
		userPref = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema")
		def setUnits(l,t,v):
			self.userLengthUnit = l
			self.userTimeUnit = t
			self.userVelocityUnit = v
		if userPref in [0,1]: setUnits('mm','s','mm/s')
		elif userPref == 2: setUnits('m', 's', 'm/s')
		elif userPref in [3,4]: setUnits('in','min','ipm')
		elif userPref == 6: setUnits('mm','min','mm/min')
		else:
			print "WARNING: units unknown"
			setUnits('mm','s','mm/s')
			
	def toOutputUnits(self,s,form):
		if hasattr(s,"UserString") == False:
			if self.outputUnits == 'METRIC': return s
			return s/25.4
		s = s.UserString
		sUnit = s.lstrip('-+0123456789.e\ ')
		sValue = eval(s[:len(s) - len(sUnit)])
		sUnit = sUnit.strip()
		if sUnit == "":
			if form == 'velocity': sUnit = self.userVelocityUnit
			elif form == 'length': sUnit = self.userLengthUnit
			elif form == 'time': sUnit = self.userTimeUnit
		if self.outputUnits == 'METRIC':
			if form == 'length':
				if sUnit in ['"','in']: sValue = sValue * 25.4
				elif sUnit in ["'",'f','ft']: sValue = sValue * 25.4 * 12
				elif sUnit == 'm': sValue = SValue * 1000
			elif form == 'velocity':
				if sUnit in ['mm/sec', 'mm/s', 'mmps']: sValue = sValue / 60
				elif sUnit in ['m/min', 'm/m', 'mpm']: sValue = sValue * 1000
				elif sUnit in ['m/s', 'm/sec', 'mps']: sValue = sValue * 1000 * 60
				elif sUnit in ['in/m','in/min', '"/m','"/min', 'ipm']: sValue = sValue * 25.4
				elif sUnit in ['in/sec','in/s','"/s','"/sec', 'ips']: sValue = sValue * 25.4 * 60
				elif sUnit in ['f/s', 'ft/sec', 'fps']: sValue = sValue * 12 * 25.4 * 60
				elif sUnit in ['ft/m', 'ft/min', 'fpm']: sValue = sValue * 12 * 25.4
				elif sUnit == 'kph': sValue = sValue * 1,000,000 / 60
				elif sUnit == 'mph': sValue = sValue * 5280 * 12 * 25.4 / 60
		else:
			if form == 'length':
				if sUnit == 'mm': sValue = sValue / 25.4
				elif sUnit == 'm': sValue = sValue * 39.37
				elif sUnit in ['f', 'ft', "'"]: sValue = sValue * 12
			elif form == 'velocity':
				if sUnit in ['mm/min','mm/m','mmpm']: sValue = sValue / 25.4
				elif sUnit in ['mm/sec', 'mm/s', 'mmps']: sValue = sValue / 25.4 * 60
				elif sUnit in ['m/min', 'm/m', 'mpm']: sValue = sValue * 39.37
				elif sUnit in ['m/s', 'm/sec', 'mps']: sValue = sValue * 39.37 * 60
				elif sUnit in ['in/sec','in/s','"/s','"/sec', 'ips']: sValue = sValue * 60
				elif sUnit in ['f/s', 'ft/sec', 'fps']: sValue = sValue * 12 * 60
				elif sUnit in ['ft/m', 'ft/min', 'fpm']: sValue = sValue * 12
				elif sUnit == 'kph': sValue = sValue * 1000 * 39.37 / 60
				elif sUnit == 'mph': sValue = sValue * 5280 * 12 / 60
		if form == 'time':
			if sUnit in ['s', 'sec']: sValue = sValue / 60
			if sUnit in ['hr', 'hour']: sValue = sValue * 60			
		elif form == 'angularVelocity':
			if sUnit in ['rps', 'r/s', 'r/sec', 'rev/s', 'rev/sec']: sValue = sValue / 60
		elif form == 'angle':
			if sUnit in ['rad', 'r', 'radian', 'radians']: sValue = sValue / math.pi
		return sValue

	def setOffset(self, x,y,z):
		self.xOff = x
		self.yOff = y
		self.zOff = z			
	
	def updateActionLabel(self,s):
		self.ui.actionL.setText(s)
		FreeCADGui.updateGui()		
	
	def getOrigin(self,obj):
		x = self.toOutputUnits(obj.getParentGroup().XOriginValue,'length')
		y = self.toOutputUnits(obj.getParentGroup().YOriginValue,'length')
		z = self.toOutputUnits(obj.getParentGroup().ZOriginValue,'length')
		return (x,y,z)
	
	def setBitWidth(self,obj):
		tool = FreeCAD.ActiveDocument.getObjectsByLabel(obj.Tool)[0]
		if hasattr(tool,'Diameter'): self.bitWidth = tool.Diameter.Value
		else: self.bitWidth = 0.0	
		return
		
	def setToolParams(self,obj):
		tool = FreeCAD.ActiveDocument.getObjectsByLabel(obj.Tool)[0]
		if tool.ToolType == "Ball":
			self.toolParams = {'type':'Ball', 'ballDiameter': tool.BallDiameter.Value}
		elif tool.ToolType == "Straight":
			self.toolParams = {'type': 'Straight', 'diameter': tool.Diameter.Value}
		elif tool.ToolType == 'Conical':
			self.toolParams = {'type': 'Conical', 'cutLength': tool.CutLength.Value, 'topDiameter': tool.TopDiameter.Value}
		else:
			print "Error: " + tool.ToolType + 'not implemented'
			self.toolParams = None
		return
		
	
	def getLabel(self,s):
		i = 0
		while len(FreeCAD.ActiveDocument.getObjectsByLabel(s)) > 0:
			i = i + 1
			s = s + str(i)
		if i == 0: return s
		return s + str(i)
		
	def scalePolyToClipper(self,poly,sf):
		scaledPoly = []
		for point in poly:
			x = int(round(point[0] * sf))
			y = int(round(point[1] * sf))
			scaledPoly.append((x,y))
		return scaledPoly
		
	def scaleToClipper(self,polys,sf):
		scaledPolys = []
		for poly in polys:
			scaledPoly = []
			for point in poly:
				x = int(round(point[0] * sf))
				y = int(round(point[1] * sf))
				scaledPoly.append((x,y))
			scaledPolys.append(scaledPoly)
		return scaledPolys
			
	def scaleFromClipper(self,polys,sf):
		scaledPolys = []
		for poly in polys:
			scaledPoly = []
			for point in poly:
				x = float(point[0] * sf)
				y = float(point[1] * sf)
				scaledPoly.append((x,y))
			scaledPolys.append(scaledPoly)
		return scaledPolys
		
	def areaOfPoly(self,poly):
		sum1 = 0.
		sum2 = 0.
		for i in range(len(poly) - 1):
			sum1 = sum1 + poly[i][0] * poly[i+1][1]
			sum2 = sum2 + poly[i][1] * poly[i+1][0]
		return (sum1 - sum2) / 2
					
	def lengthOfPoly(self,poly):
		l = 0.
		for i in range(len(poly) - 1):
			x1 = poly[i][0]
			y1 = poly[i][1]
			x2 = poly[i+1][0]
			y2 = poly[i+1][1]
			l = l + math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1))
		return l
		
	def shortestPoly(self,polys):
		shortest = polys[0]
		shortestLength = self.lengthOfPoly(shortest)
		for poly in polys:
			l = self.lengthOfPoly(poly)
			if l < shortestLength:
				shortestLength = l
				shortest = poly
		return shortest
		
	def longestPoly(self,polys):
		longest = polys[0]
		longestLength = self.lengthOfPoly(longest)
		for poly in polys:
			l = self.lengthOfPoly(poly)
			if l > longestLength:
				longestLength = l
				longest = poly
		return longest
		
	def nextPoly(self,x,y,polys,delta):
		nearestPoly = None
		for poly in polys:
			d = math.sqrt((x - poly[0][0]) * (x - poly[0][0]) + (y - poly[0][1]) * (y - poly[0][1]))
			if d <= delta:
				nearestPoly = poly
				delta = d
		return nearestPoly
				
	def sortPolysByLength(self,polys):
		for poly in polys:
			print 'length = ' + str(self.lengthOfPoly(poly)) + ' mm, area = ' + str(self.areaOfPoly(poly))
		
	def cutPolyInsideClimb(self,poly):
		i = 0
		while i < len(poly):
			self.cut(poly[i][0],poly[i][1])
			i = i + 1
		
	def cutPolyInsideConventional(self,poly):
		i = len(poly) - 1
		while (i >= 0):
			self.cut(poly[i][0],poly[i][1])
			i = i - 1
		
	def cutPolyOutsideClimb(self,poly):
		i = len(poly) - 1
		while (i >= 0):
			self.cut(poly[i][0],poly[i][1])
			i = i - 1
		
	def cutPolyOutsideConventional(self,poly):
		i = 0
		while i < len(poly):
			self.cut(poly[i][0],poly[i],[1])
			i = i + 1
	
	def getClipSolutions(self,clip,subj):
		pc = pyclipper.Pyclipper()
		pc.AddPath(pyclipper.scale_to_clipper(clip), pyclipper.PT_CLIP, True)
		pc.AddPaths(pyclipper.scale_to_clipper(subj), pyclipper.PT_SUBJECT, True)
		solution = pyclipper.scale_from_clipper(pc.Execute(pyclipper.CT_XOR, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD))
		return solution
				
	def ensurePolyOrientation(self,poly,polys,xMin,xMax):
		pass

	def getOffset(self, polys, offset):
		pco = pyclipper.PyclipperOffset()
		bigPolys = self.scaleToClipper(polys,100000.)
		pco.AddPaths(bigPolys, pyclipper.JT_MITER, pyclipper.ET_CLOSEDPOLYGON)
		offsetPolys = self.scaleFromClipper(pco.Execute(offset * 100000.),1/100000.)
		for poly in offsetPolys:
			poly.append(poly[0])
		return offsetPolys

	def getSegDir(self,seg):
		x1 = seg[0][0]
		x2 = seg[1][0]
		y1 = seg[0][1]
		y2 = seg[1][1]
		length = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
		return math.acos((x2-x1)/length)
		
	def line(self, p1,p2):
		""" returns line defined by p1 and p2 in A,B,C form """
		if p1 == p2: return 0,0,0
		(x1,y1),(x2,y2) = p1,p2
		""" first solve for x and b in y=mx+b"""
		if x2 == x1:
			A = 1
			B = 0
			C = -x1
		else:
			A = (y2 - y1)/(x2 - x1)
			B = -1
			C = y1 - A * x1
		return A,B,C
		
	def ptl(self,A,B,C,p):
		""" returns distance from line in ABC form to point p"""
		if A==0 and B==0 and C==0: return 0
		return abs(A * p[0] + B * p[1] + C)/math.sqrt(A*A + B*B)
		
	def smoothePoly(self,poly):
		error = self.error / 3
		i = 0
		reducedPoly = [poly[0]]
		while i < len(poly) - 1:
			startPoint = poly[i]
			A,B,C = self.line(startPoint,poly[i + 1])
			if error < self.ptl(A,B,C,poly[i+1]):
				reducedPoly.append(poly[i+1])
				i = i + 1
				continue
			while error > self.ptl(A,B,C,poly[i+1]):
				i = i + 1
				if i < len(poly) - 1: continue
				else: break
			reducedPoly.append(poly[i])
		if reducedPoly[0] != reducedPoly[len(reducedPoly) - 1]: reducedPoly.append(poly[0])
		return reducedPoly

	def moveOrigin2D(self,polys):
		xOff = self.parent.XOriginValue.Value
		yOff = self.parent.YOriginValue.Value
		zOff = self.parent.ZOriginValue.Value
		for poly in polys:
			for point in poly:
				point = (point[0] - xOff,point[1] - yOff)
		return polys
		
	def getUniqueName(self,base):
		i = 1
		name = base + str(i)
		while hasattr(FreeCAD.ActiveDocument,name) == True:
			i = i + 1
			name = base + str(i)
		return name
		
	def intersectionOfShapes(self,mask,polys):
		pc = pyclipper.Pyclipper()
		pc.AddPaths(pyclipper.scale_to_clipper(mask), pyclipper.PT_CLIP, True)
		pc.AddPaths(pyclipper.scale_to_clipper(polys), pyclipper.PT_SUBJECT, True)
		solution = pyclipper.scale_from_clipper(pc.Execute(pyclipper.CT_INTERSECTION, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD))
		return solution		
		
	def differenceOfShapes(self,name1,name2):
		fc = FreeCAD.ActiveDocument
		base = fc.getObjectsByLabel(name1)[0]
		cut = fc.getObjectsByLabel(name2)[0]
		nameOfNewShape = self.getUniqueName("Cut")
		fc.addObject("Part::Cut",nameOfNewShape)
		mold = fc.getObjectsByLabel(nameOfNewShape)[0]
		mold.Base = base
		mold.Tool = cut
		fc.recompute()
		return mold
		
	def dtp(self,v1,v2):
		x = v1[0] - v2[0]
		y = v1[1] - v2[1]
		z = v1[2] - v2[2]
		return math.sqrt(x*x + y*y + z*z)
		
	def reversePath(self,p):
		newP = []
		i = len(p) - 1
		while i >= 0:
			newP.append(p[i])
			i = i - 1
		return newP

	def getWire(self,objectToSlice,direction,depth,position):
		print "getting wire at: ",position
		if hasattr(self.obj,"MaximumError") == False: error = .1
		else: error = self.obj.MaximumError.Value
		fv = FreeCAD.Base.Vector
		if direction == 'AlongX': vec = fv(0,1,0)
		elif direction == 'AlongY': vec = fv(1,0,0)
		else: vec = fv(1,1,0)
		wires = list()
		wires = objectToSlice.Shape.slice(vec,position)
		if len(wires) == 0: return None
		else: wire = wires[0]

		segList = list()
		for e in wire.Edges: segList.append(e.discretize(QuasiDeflection = error/3.))
		print "length of segList is: ",len(segList)
		for seg in segList:
			i = 0
			while i < len(seg):
				seg[i] = fv(round(seg[i][0],5),round(seg[i][1],5),round(seg[i][2],5))
				i = i + 1
		poly = list()
		poly = poly + segList.pop(0)
		while len(segList) > 0:
			i = 0
			end = poly[len(poly)-1]
			while i < len(segList):
				seg = segList[i]
				if seg[0] == end:
					poly = poly + seg[1:]
					segList.pop(i)
					break
				elif seg[len(seg)-1] == end:
					seg.reverse()
					poly = poly + seg[1:]
					segList.pop(i)
					break
				else: i = i + 1
		poly.pop()
		print "length of poly is: ", len(poly)
		
		wireAboveDepth = list()
		lastPoint = poly[len(poly) - 1]
		while len(poly) > 0:
			p = poly.pop(0)
			print "p[2] is: ",p[2]," depth is: ",depth
			if p[2] >= depth:
				if lastPoint[2] < depth:
					if direction in ['AlongX','Diagonal']:
						if lastPoint[1] == p[1]:
							lastPoint = (lastPoint[0],lastPoint[1],depth)
						else:
							m = (lastPoint[2] - p[2])/(lastPoint[1] - p[1])
							lastPoint = (lastPoint[0],round(lastPoint[1] + m * (p[1] - lastPoint[1]),5), depth)
					elif direction == 'AlongY':
						if lastPoint[0] == p[0]:
							lastPoint = (lastPoint[0],lastPoint[1],depth)
						else:
							m = (lastPoint[2] - p[2])/(lastPoint[0] - p[0])
							lastPoint = (round(lastPoint[0] + m * (p[0] - lastPoint[0]),5), lastPoint[1], depth)
						
					wireAboveDepth.append(lastPoint)
				wireAboveDepth.append(p)
			else:
				if lastPoint[2] >= depth:
					if direction in ['AlongX','Diagonal']:
						if lastPoint[1] == p[1]:
							lastPoint = (lastPoint[0],lastPoint[1],depth)
						else:
							m = (lastPoint[2] - p[2])/(lastPoint[1] - p[1])
							lastPoint = (lastPoint[0],round(lastPoint[1] + m * (p[1] - lastPoint[1]),5), depth)
					elif direction == 'AlongY':
						if lastPoint[0] == p[0]:
							lastPoint = (lastPoint[0],lastPoint[1],depth)
						else:
							m = (lastPoint[2] - p[2])/(lastPoint[0] - p[0])
							lastPoint = (round(lastPoint[0] + m * (p[0] - lastPoint[0]),5),lastPoint[1], depth)
						
					wireAboveDepth.append(lastPoint)				
			lastPoint = p
		print "length of wireAboveDepth is: ",len(wireAboveDepth)
		if len(wireAboveDepth) == 0: return None

		def mySort(e):
			if direction in ['AlongX','Diagonal']: return 100 * e[0] + e[2]
			else: return 100 * e[1] + e[2]
		wireAboveDepth.sort(key=mySort)
		
		w = wireAboveDepth[:]
		l = len(w)
		if direction in ['AlongX', 'Diagonal'] and w[l-1][0] == w[l-2][0]:
			if w[l-1][2] > w[l-2][2]:
				wireAboveDepth.pop()
				wireAboveDepth.insert(l-2,w[l-1])
		elif direction == 'AlongY' and w[l-1][1] == w[l-2][1]:
			if w[l-1][2] > w[l-2][2]:
				wireAboveDepth.pop()
				wireAboveDepth.insert(l-2,w[l-1])

		i = 0
		while i < len(wireAboveDepth):
			x = round(wireAboveDepth[i][0] - self.parent.XOriginValue.Value,5)
			y = round(wireAboveDepth[i][1] - self.parent.YOriginValue.Value,5)
			z = round(wireAboveDepth[i][2] - self.parent.ZOriginValue.Value,5)
			wireAboveDepth[i] = fv(x,y,z)
			i = i + 1
			
		return wireAboveDepth
	
	def getSlice(self,obj,plane,offset):
		fc = FreeCAD.ActiveDocument
		shape = obj.Shape
		bb = shape.BoundBox
		if plane == "Horizontal":
			vec = Base.Vector(0,0,1)
		elif plane == "AlongX":
			vec = Base.Vector(0,1,0)
		elif plane == "AlongY":
			vec = Base.Vector(1,0,0)
		elif plane == "Diagonal":
			vec = Base.Vector(.7071,.7071,0)
		else: 
			vec = Base.Vector(0,0,1)
		wires = list()
		wires = shape.slice(vec,offset)
		ds = list()
		for w in wires:
			ds = ds + self.wireToDiscreteSegments(w)
		del shape,wires,bb
		return ds	

	def discretizeWire(self,wire):
		if hasattr(self.obj,"MaximumError") == False: error = .1
		else: error = self.obj.MaximumError.Value
		segList = []
		for edge in wire.OrderedEdges:
			segList = segList + edge.discretize(QuasiDeflection=error/3.)
		return segList
	
	def wireToDiscreteSegments(self,wire):		
		if hasattr(self.obj,"MaximumError") == False: error = .1
		else: error = self.obj.MaximumError.Value
		segList = []
		for edge in wire.OrderedEdges:
			vertexes = edge.discretize(QuasiDeflection = error/3)
			i = 0
			while i < len(vertexes) - 1:
				segList.append([vertexes[i],vertexes[i+1]])
				i = i + 1
		return segList	

	def sortPoly(self,point):
		return point[0]
		
	def getTopSegs(self,seg1,seg2):
		x11,y11,x12,y12 = seg1[0][0],seg1[0][2],seg1[1][0],seg1[1][2]
		if x11 > x12: x11,y11,x12,y12 = x12,y12,x11,y11
		if x11 == x12: m1 = None
		else: m1 = (y12 - y11)/(x12 - x11)
		x21,y21,x22,y22 = seg2[0][0],seg2[0][2],seg2[1][0],seg2[1][2]
		if x21 > x22: x21,y21,x22,y22 = x22,y22,x21,y21
		if x21 == x22: m2 = None
		else: m2 = (y22 - y21)/(x22 - x21)
		newSegs = list()
		if x12 <= x21 or x11 >= x22:
			newSegs.append((x11,y11),(x12,y12))
			newSegs.append((x21,y21),(x22,y22))
			return newSegs
		if x11 < x21:
			newSeg = (x11,y11),(x21,y11 + m1*(x21 - x11))
			newSegs.append(newSeg)
			x11,y11 = newSeg[1]
		elif x21 < x11:
			newSeg = (x21,y21),(x11, y21 + m2* (x11,x21))
			newSegs.append(newSeg)
			x21,y21 = newSeg[1]
		if x22 > x12:
			newSeg = (x12,y21 + m2 *(x22 - x12)),(x22,y22)
			newSegs.append(newSeg)
			x22,y22 = newSeg[0]
		elif x12 > x22:
			newSeg = (x22,y12 + m1 * (x12 - x22)),(x12,y12)
			newSegs.append(newSeg)
			x12,y12 = x22,y12 + m1 * (x22 - x11)
		if y11 > y21 or y12 > y22: newSeg = (x11,y11),(x12,y12)
		elif y21 > y11 or y22 > y12: newSeg = (x21,y21),(x22,y22)
		else: newSeg = (x11,y11),(x21,y21)
		newSegs.append(newSeg)
		return newSegs
		
		 					
	def normalizePolyToClipper(self,wire,obj):
		direction = obj.Direction
		depth = obj.MaximumDepth.Value
		parent = obj.getParentGroup()
		xOff = parent.XOriginValue.Value
		yOff = parent.YOriginValue.Value
		zOff = parent.ZOriginValue.Value
		clipperPoly = []
		if direction == 'AlongX':
			for vertex in wire:
				clipperPoly.append((round(vertex[0] - xOff,3),round(vertex[2] - zOff,3)))
				
		print clipperPoly
		print "sorting"
		print clipperPoly.sort(key=self.sortPoly)		

		return clipperPoly	
					
	def getPolysAtSlice(self,objectToCut,plane,height):
		fc = FreeCAD.ActiveDocument
		obj = fc.getObjectsByLabel(objectToCut)[0]
		shape = obj.Shape
		if hasattr(self.obj,"MaximumError") == False: error = .1
		else: error = self.obj.MaximumError.Value
		FreeCADGui.ActiveDocument.getObject(obj.Name).Deviation = error / 3.
		wires = list()
		for i in shape.slice(Base.Vector(0,0,1),height):
			wires.append(i)
		polys = []
		for wire in wires:
			segList = []
			for edge in wire.OrderedEdges:
				segList.append(edge.discretize(QuasiDeflection=error/3.))
			newWire = segList.pop()
			while len(segList) > 0:
				for seg in segList:
					if self.dtp(seg[0],newWire[len(newWire)-1]) < 0.00001:
						newWire = newWire + seg[1:]
						segList.remove(seg)
						break
					elif self.dtp(seg[len(seg)-1],newWire[len(newWire)-1]) < 0.00001:
						temp = []
						i = len(seg) - 2
						while i>=0:
							temp.append(seg[i])
							i = i-1
						newWire = newWire + temp
						segList.remove(seg)
						break
			poly = []
			for v in newWire:
				poly.append([v[0],v[1]])
			polys.append(poly)
			
		if hasattr(self,"lastSlice"):
			if self.lastSlice != None:
				scaledLastSlice = pyclipper.SimplifyPolygons(self.scaleToClipper(self.lastSlice,100000.))
				scaledPolys = pyclipper.SimplifyPolygons(self.scaleToClipper(simplePolys,100000.))
				pc = pyclipper.Pyclipper()
				pc.AddPath(scaledPolys,pyclipper.PT_CLIP,True)
				pc.AddPaths([scaledLastSlice],pyclipper.PT_SUBJECT,True)
				solution = pc.Execute(pyclipper.CT_UNION, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD)
				simplePolys = self.scaleFromClipper(pyclipper.SimplifyPolygons(solutions,1/100000.))
			else:
				simplePolys = self.scaleFromClipper(pyclipper.SimplifyPolygons(self.scaleToClipper(polys,100000.)),1/100000.)
			return simplePolys
		else:
			return self.scaleFromClipper(pyclipper.SimplifyPolygons(self.scaleToClipper(polys,100000.)),1/100000.)
	
	def __getstate__(self):
		state = {}
		state["props"] = []
		return state
		
	def __setstate__(self, state):
		return		
	
	def IsActive(self):
		return True
		
	def execute(self,obj):
		return True
